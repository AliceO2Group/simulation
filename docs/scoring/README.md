---
sort: 9
title: Geant4 scoring
---

# Geant4 scoring

Geant4 can accumulate radiation maps — fluence, dose, 1 MeV neutron equivalent
fluence, hadron fluence above 20 MeV — on a mesh laid over the ALICE geometry,
without any change to detector code. The mesh is configured with Geant4 macro
commands, the same way FLUKA users configure `USRBIN` cards, and the result is
written as a text file at the end of the run.

This page explains how to switch it on in `o2-sim`, how to write the macro, and
how to read the output. The [FLUKA counterpart](flukacomparison.md) page gives
the card-by-card translation and the differences you have to know about before
comparing numbers.

## Quick start

Write a macro file `scoring.in`:

```
/score/create/cylinderMesh fine
/score/mesh/cylinderSize 10. 30. cm
/score/mesh/nBin 100 60 1
/score/quantity/cellFlux flux percm2
/score/quantity/doseDeposit dose Gy
/score/close
```

Append it to the standard ALICE Geant4 configuration and run:

```bash
cat $O2_ROOT/share/Detectors/gconfig/g4config.in scoring.in > g4scoring.in

o2-sim-serial -e TGeant4 -g pythia8pp -n 100 \
  --configKeyValues "G4.g4scoring=true;G4.configMacroFile=$PWD/g4scoring.in"
```

The run writes `fine.worker<pid>.txt` into the working directory, one file per
mesh.

`G4.configMacroFile` **replaces** the standard `g4config.in`, it does not add to
it. Always concatenate, otherwise the run loses the ALICE physics settings
(range cuts, PAI in the TRD, biasing, field steppers).

## Meshes

Each mesh is a block between `/score/create/...` and `/score/close`. Several
meshes can coexist; they are parallel worlds and do not disturb the transport.

| Command | Meaning |
|---|---|
| `/score/create/cylinderMesh <name>` | cylindrical mesh, axis along z |
| `/score/create/boxMesh <name>` | box mesh |
| `/score/mesh/cylinderSize <R> <dz> <unit>` | outer radius and **half** length |
| `/score/mesh/boxSize <dx> <dy> <dz> <unit>` | **half** lengths |
| `/score/mesh/nBin <nR> <nZ> <nPhi>` | bins of a cylinder mesh |
| `/score/mesh/nBin <nX> <nY> <nZ>` | bins of a box mesh |
| `/score/mesh/translate/xyz <x> <y> <z> <unit>` | move the mesh off the origin |
| `/score/close` | end the mesh definition |

A mesh is centred on the origin unless it is translated. Bins are equidistant.
A single phi bin gives the phi-averaged map, which is what a radiation study
normally wants.

## Quantities and filters

Inside a mesh, every `/score/quantity/...` line adds one scorer, and the
`/score/filter/...` lines that follow apply to the scorer above them.

| Command | Quantity |
|---|---|
| `/score/quantity/cellFlux <name> percm2` | track length per cell volume, i.e. fluence |
| `/score/quantity/doseDeposit <name> Gy` | absorbed dose |
| `/score/quantity/energyDeposit <name> MeV` | deposited energy |
| `/score/quantity/nOfStep <name>` | number of steps, useful for debugging |

| Filter | Selects |
|---|---|
| `/score/filter/particle <fname> <p1> <p2> ...` | those Geant4 particle names |
| `/score/filter/particleWithKineticEnergy <fname> <emin> <emax> <unit> <p1> ...` | those particles in that kinetic energy range |
| `/score/filter/charged <fname>` | all charged particles |
| `/score/filter/neutral <fname>` | all neutral particles |

Particle names are the Geant4 ones: `neutron`, `proton`, `anti_proton`, `pi+`,
`pi-`, `kaon0L`, `gamma`, `e-`, `opticalphoton`, and so on.

A scorer without a filter counts everything, **including optical photons**.
Those dominate the total fluence around the FT0 and are not transported by
FLUKA at all, so an unfiltered `cellFlux` is not a quantity you can compare
between the two engines. Filter, or read the filtered scorers instead.

## Output

Each mesh is dumped at the end of the run to `<mesh>.worker<pid>.txt`:

```
# mesh name: fine
# primitive scorer name: flux
# iZ, iPHI, iR, total(value) [percm2], total(val^2), entry
0,0,0,1856.089717,405107.423708,10
```

The columns are the bin indices, the sum over the whole run, the sum of
squares, and the number of contributing steps. Two things to keep in mind:

- The value is summed over **all events of the run**, not per event. Divide by
  the number of events yourself.
- `total(val^2)` is the sum of squares of the per-step contributions, so it is
  not the statistical error of the bin. Use several runs with different seeds
  if you need an uncertainty.

Parallel `o2-sim` writes one file per worker and merges them into `<mesh>.txt`
at the end of the run. If a merge has to be redone by hand, for example after
collecting dumps from several jobs:

```bash
o2-sim-merge-g4scoring <directory> <expected number of workers>
```

The second argument is optional; when given, the merger fails loudly if a
worker file is missing, which is the common way to lose a few percent of the
statistics without noticing.

## 1 MeV neutron equivalent fluence

Geant4 has no built-in NIEL scorer. The ALICE Geant4 build takes a per-step
weight from a user function, and `o2-sim` feeds it with RD50 damage weights, so
that a `cellFlux` scorer becomes a damage-weighted fluence:

```
/score/quantity/cellFlux neq percm2 true
```

The trailing `true` is the `scoreweighted` flag. It only exists for `cellFlux`.

Switch the weights on with:

```bash
--configKeyValues "G4.g4scoring=true;G4.g4fluenceweight=true;G4.fluenceWeightFile=$O2_ROOT/share/Detectors/gconfig/data/rd50_niel.csv;G4.configMacroFile=$PWD/g4scoring.in"
```

**The `true` flag alone does nothing.** Without `G4.g4fluenceweight=true` the
scorer falls back to a weight of one for every step, so the map looks perfectly
healthy and is plain fluence. There is no warning. If a `neq` map comes out
equal to the unweighted one, this is why.

The weight file is a CSV of PDG code, kinetic energy in MeV and damage weight:

```
# pdg,ekin[MeV],weight
2112,1.025000e-10,1.575000e-02
```

The file ships with O2 as
`$O2_ROOT/share/Detectors/gconfig/data/rd50_niel.csv`, together with the same
curves as ROOT graphs in `rd50_niel.root`. The loader only accepts CSV.

Only four tables are read — neutron (2112), proton (2212), pion (211) and
electron (11) — and they are applied like this:

| Particle | Weight used |
|---|---|
| neutron | neutron table |
| e+, e- | electron table, zero if the table is absent |
| all other baryons and antibaryons | proton table |
| all other mesons | pion table |
| everything else | zero |

Outside the tabulated energy range the weight is clamped to the first or last
tabulated value. The electron table covers 0.3 to 200 MeV (Summers et al.,
IEEE Trans. Nucl. Sci. 40 (1993) 1372, as compiled by RD50), so electrons below
0.3 MeV get the lowest tabulated weight. O2 versions from before October 2026
ship the file without the electron table; there e± weigh nothing, which is
about half a percent of the inner-tracker n eq.

The four tables are the RD50 compilation by A. Vasilescu and G. Lindström,
https://rd50.web.cern.ch/NIEL/.

The consequence for a comparison: **do not filter the NIEL scorer down to
neutrons, protons and pions.** FLUKA's `SI1MEVNE` weights every hadron and
electron, so an ALICE inner-tracker map scored only on n, p and pi comes out
about 18% low. Kaons alone account for most of it.

## A ready example

[`g4scoring_alice.in`](g4scoring_alice.in) is the macro used for the ALICE
FLUKA/Geant4 radiation comparison: a fine mesh over the inner tracker and a
coarse one over the cavern, each with fluence, 1 MeV n eq, hadrons above
20 MeV, charged fluence, energy deposit and dose.

```bash
cat $O2_ROOT/share/Detectors/gconfig/g4config.in g4scoring_alice.in > g4full.in

o2-sim -e TGeant4 -g pythia8pp -n 1000 -j 8 \
  --configKeyValues "G4.g4scoring=true;G4.g4fluenceweight=true;G4.fluenceWeightFile=$O2_ROOT/share/Detectors/gconfig/data/rd50_niel.csv;G4.configMacroFile=$PWD/g4full.in"
```

{% include list.liquid all=true %}
