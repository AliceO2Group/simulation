---
sort: 1
title: Generators implemented in O2
---

# Generators implemented in O2

There are several generators which can be directly specified with `o2-sim -g <generator>` which are summarised in the following. In some cases, as you will see below, there is the need of setting addition parameters via `--configKeyValues`. Furthermore, there might be additional optional parameters that can be passed via `--configKeyValues`.

## Pythia8

Pythia8 is the default generator for ALICE Run3, and the only one with a native interface in the O2 codebase, via the [GeneratorPythia8](https://github.com/AliceO2Group/AliceO2/blob/dev/Generators/include/Generators/GeneratorPythia8.h) class.

For Pythia8 there are 5 different options/values which can be directly used as `<generator>` in `o2-sim -g <generator>`:

### pythia8

This selects Pythia8 as the generator for simulation but it is necessary to pass a Pythia8 configuration file, such as
```text
### beams
Beams:idA 2212			# proton
Beams:idB 2212 			# proton
Beams:eCM 14000. 		# GeV

### processes
SoftQCD:inelastic on		# all inelastic processes

### decays
ParticleDecays:limitTau0 on	
ParticleDecays:tau0Max 10.
```
which configures the Pythia8 instance.

Passing of this configuration file happens via the configurable parameter `GeneratorPythia8`. In the simplest case, one may just use `--configKeyValues "GeneratorPythia8.config=<path/to/config>"`.

Next to allowing to specify the configuration file, the configurable parameter "GeneratorPythia8" (source definition [here](https://github.com/AliceO2Group/AliceO2/blob/dev/Generators/include/Generators/GeneratorPythia8Param.h)) has more options that allow to configure the Pythia8 instance in O2. The important keys are defined in the corresponding class

* `config` : specification of the Pythia8 configuration file
* `includePartonEvent = [true|false]` : whether we keep the partonic part of the event or filter it out (default false) 
* `hooksFileName` : string to specify a ROOT macro file containing a trigger function (optional)
* `hooksFuncName` : string to specify the functionname corresponding to the trigger function (optional)


### pythia8pp

A special, pre-configured case of `<pythia8>` for pp collisions. This uses default Pythia8 with [this configuration](https://github.com/AliceO2Group/AliceO2/blob/dev/Generators/share/egconfig/pythia8_inel.cfg).

### pythia8hf

A special, pre-configured case of `<pythia8>` for HF. This uses default Pythia8 with the configuration [this configuration](https://github.com/AliceO2Group/AliceO2/blob/dev/Generators/share/egconfig/pythia8_hf.cfg).

### pythia8hi

A special, pre-configured case of `<pythia8>` for PbPb collisions (Agantyr model). This uses default Pythia8 with the configuration [this configuration](https://github.com/AliceO2Group/AliceO2/blob/dev/Generators/share/egconfig/pythia8_hi.cfg).

### pythia8powheg

This uses default Pythia8 with the configuration [this configuration](https://github.com/AliceO2Group/AliceO2/blob/dev/Generators/share/egconfig/pythia8_powheg.cfg).
In addition, that needs a POWHEG output file `powheg.lhe` to be present in the working directory where Pythia8 reads from.

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
```bash
o2-sim -m PIPE ITS MFT -g boxgen -n 10 --configKeyValues 'BoxGun.pdg=13 ; BoxGun.eta[0]=-3.6 ; BoxGun.eta[1]=-2.45; BoxGun.number=100'
```

This command line will generate 10 events with 100 forward muons, simulating only the beam pipe, the ITS and the MFT.

## Generating from file

Events and their primaries (and secondaries) can also be read from a file and injected into the transport.

### extkinO2

This reads primaries to be transported from an MC kinematics file. Such a file is produced always by a (previous) run of `o2-sim`. Of course the file path to this file has to be passed. A command would look like
```bash
o2-sim -g extkinO2 --extKinFile <path/to/o2sim_Kine.root>
```
Alien paths are compatible as well, provided they follow the syntax `alien:///path/to/file.root`. They will be opened on-the-fly, without the need to download them locally, however you might experience longer simulation times due to the remote source.

### hepmc

This reads primaries to be transported from a HepMC file. A command would look like
```bash
o2-sim -g hepmc --configKeyValues "HepMC.fileName=<path/to/HepMC/file>"
```
It is important to know which HepMC version is considered: by default `o2-sim` assumes HepMC3, but if this is not the case (as for EPOS4) `HepMC.version=2`
must be added in the configuration keys, otherwise the simulation task could fail.

## Generating using FIFOs 

FIFOs allow not to store data from generators and to feed them directly to o2-sim and they can be used either *manually*, by creating one and then feeding it as HepMC file to both your generator and the o2-sim script, or automatically via `GeneratorHepMC` using the `cmd` parameter.  
The use of the latter, instead of the former, is **highly encouraged** and three examples are provided in [O2](https://github.com/AliceO2Group/AliceO2/tree/dev/run/SimExamples) inside the `HepMC*` folders.  
This function spawns a simulation task using an external generator provided that this:
- returns HepMC data in the stdout &rarr; this is the only real hard requirement
- accepts a `-s` flag to set the generation seed
- has control of the number of events with a `-n` flag or different mechanism
- has the possibility of setting the impact parameter (`-b` flag).

These flags are automatically fed to the executable (or script) provided with `GeneratorFileOrCmd.cmd=<scriptname>`.  
In most generators these conditions are either available out of the box or they can be satisfied by creating a simple steering script. The only real stopper to run with this method is not having HepMC in the stdout, however the user must be careful what the other flags do in the provided generator because they could be interpreted in a different way and return unexpected results.  
In order not to provide an impact parameter limit `GeneratorFileOrCmd.bMaxSwitch=none` can be set in the configuration keys, which is useful because your generator might not be able to configure this option by default. An example command to run with automatically generated FIFOs is:
```bash
o2-sim -n 100 -g hepmc --seed 12345 --configKeyValues "GeneratorFileOrCmd.cmd=epos.sh;GeneratorFileOrCmd.bMaxSwitch=none;"
```
where epos.sh is the steering script of EPOS4 which can be found [here](https://github.com/AliceO2Group/AliceO2/tree/dev/run/SimExamples/HepMC_EPOS4). More information are at the user disposal in the README files of each HepMC example folder.

## External generators

External generators are usually defined in macros that are evaluated at runtime. External generators allow the users 
to provide completely custom generator setups and interface other generators than Pythia8 into the simulation. Examples of external generators may be specializations of Pythia8 (via class inheritance), cocktail setups, etc.

Please also refer to the [custom generators page](generatorscustom.md) for a detailed explanation of their implementation.

Such a custom generator is invoked with
```bash
o2-sim -g external --configKeyValues "GeneratorExternal.fileName=<path/to/macro.C>;GeneratorExternal.funcName=<function-signature-to-call(...)>"
```
