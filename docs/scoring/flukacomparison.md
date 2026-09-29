---
sort: 1
title: The same scoring in FLUKA
---

# The same scoring in FLUKA

FLUKA scores the same maps with `USRBIN` cards. In `o2-sim` the cards come from
a file:

```bash
o2-sim-serial -e TFluka -g pythia8pp -n 100 \
  --configKeyValues "FlukaParam.scoringFile=$PWD/scoring.inp"
```

The file is appended to the FLUKA input that `o2-sim` generates, so it contains
only the cards, in the fixed FLUKA column format:

```
*...+....1....+....2....+....3....+....4....+....5....+....6....+....7...+...8
USRBIN           11.      201.       21.      10.0        0.      30.0fflux
USRBIN            0.        0.     -30.0      100.        1.       60.&
USRBIN           11.      236.       22.      10.0        0.      30.0fneq
USRBIN            0.        0.     -30.0      100.        1.       60.&
```

Each pair of cards is one binning: type, quantity, output unit, `Rmax`, x of the
axis, `zmax`, name; then `Rmin`, y of the axis, `zmin`, `nR`, `nPhi`, `nZ`.

Two details worth spelling out:

- Type `11` is an r-phi-z mesh scored with the track-length apportioning
  algorithm. Type `1` uses the old point-wise algorithm and is **not allowed**
  for `SI1MEVNE` and `HADGT20M`.
- A positive output unit writes formatted text to `fort.<unit>`, a negative one
  writes binary that has to go through `usbsuw`/`usbrea` first. Units below 21
  are reserved. Text output is easier to read back and costs nothing at ALICE
  mesh sizes.

## Translation table

| Quantity | FLUKA | Geant4 |
|---|---|---|
| all-particle fluence | `201` (ALL-PART) | `/score/quantity/cellFlux f percm2` |
| charged fluence | `202` (ALL-CHAR) | `cellFlux` + `/score/filter/charged` |
| neutral fluence | `203` (ALL-NEUT) | `cellFlux` + `/score/filter/neutral` |
| neutron fluence | `8` (NEUTRON) | `cellFlux` + `/score/filter/particle f neutron` |
| photon fluence | `7` (PHOTON) | `cellFlux` + `/score/filter/particle f gamma` |
| deposited energy | `208` (ENERGY), GeV/cm3 | `/score/quantity/energyDeposit e MeV` |
| dose | `228` (DOSE), GeV/g | `/score/quantity/doseDeposit d Gy` |
| 1 MeV n eq (Si) | `236` (SI1MEVNE) | weighted `cellFlux`, see [Geant4 scoring](README.md) |
| hadrons above 20 MeV | `237` (HADGT20M) | `cellFlux` + `particleWithKineticEnergy` filter |

`HADGT20M` has no Geant4 equivalent either, so the particle list has to be
written out:

```
/score/quantity/cellFlux had20 percm2
/score/filter/particleWithKineticEnergy had20filter 20. 10000000. MeV proton anti_proton neutron anti_neutron pi+ pi- kaon+ kaon- kaon0L kaon0S lambda anti_lambda sigma+ sigma- xi- xi0 omega-
```

Filtering works the other way round in the two codes. In FLUKA a binning scores
one generalised particle and `AUXSCORE` can restrict it further, but not by
energy. In Geant4 a scorer starts from everything and is narrowed by filters,
including energy filters.

## Normalisation

This is the most common source of a wrong ratio.

- FLUKA normalises a `USRBIN` to **one unit of primary weight**. The text
  output carries the total weight of the primaries in its header; multiply by
  it to get the sum over the run.
- Geant4 sums over the **whole run** and divides by nothing. Divide by the
  number of events yourself.

So per event: `fluka_value * total_weight / nevents` against
`g4_value / nevents`.

## Settings to match before comparing

- **Same kinematics.** Generate once with `--noGeant`, then replay the same
  file in both engines with `-g extkinO2 --extKinFile o2sim_Kine.root`.
  Otherwise the comparison also contains the generator.
- **Low-energy neutrons.** Whenever neutrons below 20 MeV matter, which is the
  case for any 1 MeV n eq map, switch low-energy neutron transport on in both
  engines. In FLUKA this is `FlukaParam.lowNeutron=true`; it is off by default
  in `o2-sim`, and setting `FlukaParam.scoringFile` also switches it on. In
  Geant4 use an HP physics list and lower the neutron cut:
  `G4.physicsmode=kFTFP_BERT_HP_optical;SimCutParams.lowneut=true;GlobalSimProcs.CUTNEU=5.e-12`.
- **Optical photons.** Geant4 produces and transports Cherenkov photons in the
  FT0; FLUKA in the ALICE setup does not. They show up in any unfiltered
  fluence scorer and swamp it locally. Dose, 1 MeV n eq and hadron fluence are
  unaffected.
- **Same geometry.** `--detectorList` and `--skipModules` have to match, and
  hit creation should be switched off or on in both.

## Pitfall: black-hole regions in the FLUKA geometry

FLUKA gets one region per ROOT volume number. Two volumes that share a *name*
share a number, and only one of them gets its material assigned. If the winner
is a `TGeoVolumeAssembly`, its placeholder material index `-1` becomes
`BLCKHOLE`, and a real piece of detector silently deletes every particle that
enters it.

Check this in every FLUKA run directory before you trust a map:

```bash
grep -c "ASSIGNMAT       -1.0" flukaMat.inp   # 0 when healthy
```

In ALICE 2 this happened to the ten MFT PEEK support disks, which lowered the
FLUKA fluence in the barrel by up to a factor two. The name clash exists in O2
from February 2020 ([AliceO2 PR 2877](https://github.com/AliceO2Group/AliceO2/pull/2877)) until September 2026, when the support
volume got a name of its own (`4f9072579a`). It concerns only TFluka runs with
an O2 version from that period and the MFT in the geometry. The official ALICE
FLUKA calculations predate it and are not affected, and neither are the FoCal
calculations on the A side.
