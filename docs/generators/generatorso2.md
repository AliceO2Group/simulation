---
sort: 1
title: Generators in O2
---

# Generators implemented in O2

There are several generators which can be directly specified with `o2-sim -g <generator>` which are summarised in the following. In some cases, as you will see below, there is the need of setting addition parameters via `--configKeyValues`. Furthermore, there might be additional optional parameters that can be passed via `--configKeyValues`.

## Pythia8

For Pythia8 there are 4 different options which can be directly called from the command line and can be used without specifying any further options.

### pythia8

**NOTE**: In this case users have to pass a valid configuration file to Pythia8 via `--configKeyValues "GeneratorPythia8.config=<path/to/config>"` in addition.

### pythi8pp

This uses default Pythia8 with [this configuration](https://github.com/AliceO2Group/AliceO2/blob/dev/Generators/share/egconfig/pythia8_inel.cfg).

### pythia8hf

This uses default Pythia8 with the configuration [this configuration](https://github.com/AliceO2Group/AliceO2/blob/dev/Generators/share/egconfig/pythia8_hf.cfg).
### pythia8hi

This uses default Pythia8 with the configuration [this configuration](https://github.com/AliceO2Group/AliceO2/blob/dev/Generators/share/egconfig/pythia8_hi.cfg).

## Box Generators

There are multiple box or gun generators:

* `boxgen`: Generic Box Generator, 10 pions per event by default; this can be customised (see below),
* `fwmugen`: Forward muon generator,
* `hmpidgun`: HMPID pion generator,
* `fwpigen`: Forward pion generator,
* `fwrootino`: Forward rootino generator,
* `zdcgen`: ZDC (A and C side) neutron generator,
* `emcgenele` and `emcgenphoton`: Electron and photon gun for EMC, respectively,
* `fddgen`: FDD (A and C side) muon generator.

### Customising your box generator

For the generic `boxgen` generator, a user can influence the PDG, eta range etc. via `--configKeyValues "BoxGun.<param>=<value>;..."`, see this [header file](https://github.com/AliceO2Group/AliceO2/blob/dev/Generators/include/Generators/BoxGunParam.h) for all settings.

Example : 
```
o2-sim -m PIPE ITS MFT -e TGeant3 -g boxgen -n 10 --configKeyValues 'BoxGun.pdg=13 ; BoxGun.eta[0]=-3.6 ; BoxGun.eta[1]=-2.45; BoxGun.number=100'
```

This command line will generate 10 events with 100 forward muons.

## Generating from file

Events and their primaries (and secondaries) can also be read from a file and injected into the transport.

### extkinO2

This reads primaries to be transported from an MC kinematics file. Such a file is produced always by a (previous) run of `o2-sim`. Of course the file path to this file has to be passed. A command would look like
```bash
o2-sim -g extkinO2 --extKinFile <path/to/o2sim_Kine.root>
```

### hepmc

This reads primaries to be transported from a HepMC file. A command would look like
```
o2-sim -g hepmc --configKeyValues "HepMC.fileName=<path/to/HepMC/file>"
```

## External generators

External generators are usually defined in macros that are evaluated at runtime. Please also refer to the [custom generators page](generatorscustom.md) for a detailed explanation of their implementation.

Such a custom generator is invoked with
```bash
o2-sim -g external --configKeyValues "GeneratorExternal.fileName=<path/to/macro.C>;GeneratorExternal.funcName=<function-signature-to-call(...)>"
```
