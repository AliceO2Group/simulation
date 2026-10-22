---
sort: 6
title: Decays before transport
---

# Decays before transport

Particles that leave the generator undecayed, for example charm baryons from an event pool or particles left by an external generator, are by default decayed during the Geant4 transport. Geant4 either uses its own decay tables or hands the particle to Pythia8 as the VMC external decayer (`DecayerPythia8`).

In the second case Geant4 takes over only the final-state particles of the decay chain. The final state and its kinematics are correct, but every intermediate state that Pythia8 decays inside the call is missing from the MC truth. For example, Ξc⁺ → Ξ(1530)⁰ π⁺ with Ξ(1530)⁰ → Ξ⁻ π⁺ is recorded as a three-body decay Ξc⁺ → Ξ⁻ π⁺ π⁺, and Ξc⁺ → p K̄*⁰ or Ξc⁺ → p φ appear as p K π and p K K. Resonant and non-resonant contributions can then not be told apart in the MC truth. Charm and beauty hadrons that reach Geant4 without the external decayer are decayed with simple placeholder decays.

The `EventDecayer` decays such particles with Pythia8 as a step of the event generation, after the trigger and before the transport. The full decay chain enters the kinematics as generator particles, and Geant4 only transports the final state.

![Decay routes](../images/decay_routes.png)

## Usage

The step is available in AliceO2 from [PR 15995](https://github.com/AliceO2Group/AliceO2/pull/15995) on. It is off by default and is switched on with `EventDecayer.enable=true`. It then runs for every generator, including the replay of event pools and of Kine files:

```bash
# event pool with undecayed signals, decayed with a request-specific Pythia8 config
o2-sim -g evtpool --configKeyValues "GeneratorEventPool.eventPoolPath=pool.root;EventDecayer.enable=true;EventDecayer.config[1]=my_decays.cfg"

# decay the particles of an existing Kine file, without transport
o2-sim --noGeant -g extkinO2 --extKinFile in_Kine.root -o decayed --configKeyValues "EventDecayer.enable=true;EventDecayer.config[1]=my_decays.cfg"
```

Particles that were already decayed by the generator, or that are not flagged for transport, are left untouched, so running the step twice changes nothing. In O2DPG workflows the step belongs in the event-generation task (`sgngen`). When creating event pools it should stay off, so that the pools can still be decayed differently by each production that uses them.

## Configuration

| Key | Default | Meaning |
|---|---|---|
| `EventDecayer.enable` | `false` | run the step in event generation |
| `EventDecayer.config[0..7]` | empty | Pythia8 decay configs; an empty slot takes `DecayerPythia8.config` of the same slot, so both decayers read `base.cfg` and any request config by default |
| `EventDecayer.tau0Max` | `10` | species with a larger `tau0` (mm/c) are never decayed and are left to Geant4; `<= 0` disables the cut |
| `EventDecayer.skipPdg` | see below | PDG codes never decayed by the step |
| `EventDecayer.seed` | `0` | Pythia8 seed; `0` takes it from the o2-sim seed |
| `EventDecayer.g4ParticleTable` | empty | optional Geant4 particle table, written by `o2-sim-g4-particle-table`, to report particles unknown to Geant4 |
| `EventDecayer.verbose`, `showChanged` | `false` | Pythia8 printout |

Which species are decayed, and through which channels, is set in Pythia8's own terms: `id:mayDecay`, `id:onMode`, `id:oneChannel`, `id:addChannel` and so on. `base.cfg` keeps K0S, Λ, Σ±, Ξ and Ω (and other species Geant4 must transport) stable. A request that wants to decay, say, charm baryons switches them on, for example with `4232:mayDecay = on`.

The default `skipPdg` holds the resonances for which O2 defines its own Geant4 decay modes (`115 225 335 10221 10331 20223 20333 102132 102134 9010221`, among them Λ(1520) and f0(980)). They are kept in the MC truth but decayed by Geant4. A request that wants Pythia8 to decay them overrides the list.

At the end of the run the step prints a summary: decayed and failed decays per species, PDG codes unknown to `O2DatabasePDG` (or to the Geant4 table, if given), and lifetimes that differ from Geant4 by more than 1%.

## Things to know

- Pythia8's vertex-limit settings `ParticleDecays:limitTau`, `limitRadius` and `limitCylinder` are refused; only the species-level `limitTau0`/`tau0Max` is supported.
- A decay that would produce partons (e.g. some quarkonium decays) is not performed; the particle is left to Geant4 as before.
- The decay products are primaries, so all their transport secondaries are stored. For an HF event pool this made the Kine files about 0.6% larger.
- The lifetimes of several charm and beauty hadrons in Pythia8's defaults are older measurements; `base.cfg` sets the PDG values for them.
