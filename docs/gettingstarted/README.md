---
sort: 0
title: Getting started
---

# Getting started

The purpose of the `o2-sim` executable is to simulate the passage of particles emerging from a collision inside the detector and to obtain their effect in terms of energy deposits (called hits) which could be converted into detectable signals. It is the driver executable which will spawn a topology of sub-processes that interact via messages in a distributed system.

## Usage overview

There are 2 executables used to steer a simulation run
1. `o2-sim`: Runs the simulation using multiple worker processes. Also the particle generation runs in a dedicated process as well as the task responsible for collecting all detector hits created in respective simulation processes. This is also used as the default for all examples described in this documentation.
1. `o2-sim-serial`: This only launches one single simulation process. Needs to be used in some special simulations and it will be mentioned explicitly when `o2-sim` cannot be used.

### Quick start example

A typical (exemplary) invocation is of the form

```bash
o2-sim -n 10 -g pythia8pp -e TGeant4 -j 2 --skipModules ZDC,PHS
```
which would launch a simulation for 10 pythia8 events on the whole ALICE detector but ZDC and PHOS, using Geant4 on 2 parallel worker processes.

### Generated output

The simulation creates the following output files:

| File                      | Description                                                                            |
|---------------------------|----------------------------------------------------------------------------------------|
| `o2sim_Kine.root`         | contains kinematics information (primaries and secondaries) and event meta information |
| `o2sim_geometry.root`     | contains the final ROOT geometry created for simulation run                            |
| `o2sim_grp.root`          | special global run parameters (grp) such as field                                      |
| `o2sim_XXXHits.root`      | hit file for each participating active detector XXX                                    |
| `o2sim_configuration.ini` | summary of parameter values with which the simulation was done                         |
| `o2sim_serverlog`         | log file produced from the particle generator server                                   |
| `o2sim_workerlog0`        | log file produced form the transportation processes                                    |
| `o2sim_hitmergerlog`      | log file produced from the IO process                                                  |


### Main command line options

The following major options are available:

| Option                              | Description                                                                                                             |
|-------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| -h [ --help ]                       | Prints the list of possible command line options and their default values.                                              |
| -e [ --mcEngine ] arg (=TGeant4)    | VMC backend to be used. TGeant3 or TGeant4. See [transport section](../transport/)                                      |
| -g [ --generator ] arg (=boxgen)    | Event generator to be used. See [generators section](../generators/)                                                    |
| -t [ --trigger ] arg                | Event generator trigger to be used. See [trigger section](../generators/trigger.md)                                     |
| -m [ --modules ] arg (=all modules) | List of modules/geometries to include (default is ALL); example -m PIPE ITS TPC                                         |
| --skipModules arg                   | list of modules excluded in geometry (precedence over -m) See [transport section](../transport/)                        |
| --readoutDetectors arg              | list of detectors creating hits, all if not given; added to to active modules. See [transport section](../transport/)   |
| --skipReadoutDetectors arg          | list of detectors to skip hit creation (precedence over --readoutDetectors). See [transport section](../transport/)     |
| -n [ --nEvents ] arg (=0)           | number of events                                                                                                        |
| --startEvent arg (=0)               | index of first event to be used (when applicable, e.g. for `hepmc` generator). See [generators section](../generators/) |
| --extKinFile arg (=Kinematics.root) | name of kinematics file for event generator from file (when applicable). See [generators section](../generators/)       |
| --embedIntoFile arg                 | filename containing the reference events to be used for the embedding                                                   |
| -b [ --bMax ] arg (=0)              | maximum value for impact parameter sampling (when applicable)                                                           |
| --isMT arg (=0)                     | multi-threaded mode (Geant4 only)                                                                                       |
| -o [ --outPrefix ] arg (=o2sim)     | prefix of output files                                                                                                  |
| --logseverity arg (=INFO)           | severity level for FairLogger                                                                                           |
| --logverbosity arg (=medium) } level of verbosity for FairLogger (low, medium, high, veryhigh) |
| --configKeyValues | Like `--configFile` but allowing to set parameters on the command line as a string sequence. Example `--configKeyValues "Stack.pruneKine=false"`. Takes precedence over `--configFile`. Parameters need to be known ConfigurableParams. |
| --configFile arg | Path to an INI or JSON configuration file |
| --chunkSize arg (=500) | max size of primary chunk (subevent) distributed by server |
| --chunkSizeI arg (=-1) | internalChunkSize |
| --seed arg (=0) | initial seed as ULong_t (default: 0 == random) |
| --field arg (=-5) | L3 field rounded to kGauss, allowed values +-2,+-5 and 0; +-<intKGaus>U for uniform field; "ccdb" for taking it from CCDB |
| -j [ --nworkers ] arg (=4) | number of parallel simulation workers (only for parallel mode) |
| --noemptyevents | only writes events with at least one hit |
| --CCDBUrl arg (=<http://alice-ccdb.cern.ch)> | URL for CCDB to be used. |
| --timestamp arg | global timestamp value in ms (for anchoring) - default is now ... or beginning of run if ALICE run number was given |
| --run arg (=-1) | ALICE run number |
| --asservice arg (=0) | run in service/server mode |
| --noGeant | prohibits any Geant transport/physics |
| --forwardKine | forward kinematics on a FairMQ channel |
| --noDiscOutput | switch off writing sim results to disc (useful in combination with forwardKine) |
| --fromCollContext arg | Use a pregenerated collision context to infer number of events to simulate, how to embedd them, the vertex position etc. Takes precedence of other options such as "--nEvents". |

### Expert control** via environment variables

`o2-sim` is sensitive to the following environment variables:

| Variable                | Description                                                                                                                        |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| **ALICE_O2SIM_DUMPLOG** | When set, the output of all FairMQ components will be shown on the screen and can be piped into a user logfile.                    |
| **ALICE_NOSIMSHM**      | When set, communication between simulation processes will not happen using a shared memory mechanism but using ROOT serialization. |

## Configurable Parameters

Simulation makes use of `configurable parameters` as described in the [ConfigurableParam.md](https://github.com/AliceO2Group/AliceO2/blob/dev/Common/SimConfig/doc/ConfigurableParam.md) documentation.
Detector code as well as general simulation code declare such parameter and access them during runtime.
Once a parameter is declared, it can be influenced/set from the outside via configuration files or from the command line. See the `--configFile` as well as `--configKeyValues` command line options.
The complete list of parameters and their default values can be inspected in the file `o2sim_configuration.ini` that is produced by an empty run `o2-sim -n 0 -m CAVE`.

Important parameters influencing the transport simulation are:

| Main parameter key | Description                                                                                                                                  |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| G4                 | Parameters influencing the Geant4 engine, such as the physics list. Example "G4.physicsmode=kFTFP_BERT_optical_biasing"                      |
| Stack              | Parameters influencing the particle stack. Example include whether the stack does kinematics pruning or whether it keeps secondaries at all. |
| SimCutParams       | Parameters allowing to set some sime geometry stepping cuts in R, Z, etc.                                                                    |
| Diamond            | Parameter allowing to set the interaction vertex location and the spread/width. Is used in all event generators.                             |
| Pythia6            | Parameters that influence the pythia6 generator.                                                                                             |
| Pythia8            | Parameters that influence the pythia8 generator.                                                                                             |
| HepMC              | Parameters that influence the HepMC generator.                                                                                               |
| TriggerParticle    | Parameters influencing the trigger mechanism in particle generators.                                                                         |
