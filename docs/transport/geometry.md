---
sort: 3
title: Detector geometry
---

# Detector geometry

Each module consists of several (mostly quite a lot) of volumes. Each volume has a certain medium assigned which defines the volumes physical properties (steel, air, vacuum, concrete a custom mixture and so forth).

## Inspecting the geometry

A simulation run dumps the used geometry at `<prefix>_geometry.root`. This file can be browsed using ROOT, volumes can be drawn etc. For instance, to draw the geometry as-is, do
```cpp
auto geoMgr = TGeoManager::Import("<prefix>_geometry.root");
geoMgr->GetTopVolume()->Draw();
```

This can of course also be done in an interactive ROOT session.

## Medium properties

As mentioned, a medium defines the physical properties of a volume. These are defined in the code and usually, these properties cannot be changed at runtime.

However, there are some additional properties that can be modified at runtime. An important type of those properties are production cut thresholds for particles. When a particle traverses the detector, a certain interaction with the material (also called physics process) can lead to the production of secondary particles.
In reality, all of those particles would be produced, however, in simulation one has the possibility to suppress the production of particles below a certain energy threshold. The following cut parameters are available:
`CUTGAM`: gammas,
`CUTELE`: electrons,
`CUTNEU`: neutral hadrons,
`CUTHAD`: charged hadrons,
`CUTMUO`: muons,
`BCUTE`: electron bremsstrahlung,
`BCUTM`: muon and hadron bremsstrahlung,
`DCUTE`: delta-rays by electrons,
`DCUTM`: delta-rays by muons,
`PPCUTM`: direct pair production by muons.

They are set globally [here](https://github.com/AliceO2Group/AliceO2/blob/dev/Detectors/gconfig/src/SetCuts.cxx).

It is possible to set specific parameters for each medium. For most modules, there exists a text file which is parsed at runtime. As an example, the files for the passive modules are [here](https://github.com/AliceO2Group/AliceO2/tree/dev/Detectors/Passive/data).

It is also possible to change parameters on the fly. To do so, we first extract a JSON file with all current parameters.
```bash
o2-sim-serial -n0 --configKeyValues "MaterialManagerParam.outputFile=o2_medium_params.json"
```
This will leave you with the `o2_medium_params.json`. It contains all media per module and the parameters in there can be set by the user. A new parameter configuration is injected with
```bash
o2-sim --configKeyValues "MaterialManagerParam.inputFile=o2_medium_params_modified.json" [<further_arguments>]
```

## Magnetic field

**...under construction...**
