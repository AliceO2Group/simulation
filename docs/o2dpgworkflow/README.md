---
sort: 4
title: O2DPG workflows
---

# O2DPG Workflows

There are 2 tuility scripts provided in O2DPG
1. [o2dpg_sim_workflow.py](https://github.com/AliceO2Group/O2DPG/blob/master/MC/bin/o2dpg_sim_workflow.py),
1. [o2_dpg_workflow_runner.py](https://github.com/AliceO2Group/O2DPG/blob/master/MC/bin/o2_dpg_workflow_runner.py).

The first script is used to create a workflow tree describing the necessary steps and dependencies from simulation to final AOD creation while the latter is capable of executing all requested/required steps.

Several examples can be found at <https://gitlab.cern.ch/aliperf/alibibenchtasks>. **N.B.** These tasks are run nightly on a test machine so these scripts are constantly maintained.

It is best to build and load at least the `O2sim` environment from `alienv`.

## Prerequisites

It is not possible to cover all use cases here but a few important remarks and pointers are summarised in the following.

The usage of the workflows requires at least `16 GB` of RAM and an `8`-core machine. Especially in case your machine has exactly `16 GB`, please refer to [these instructions](#adjusting-resources).
You need a valid GRID token to access the CCDB objects/alien. Please refer to https://alice-doc.github.io/alice-analysis-tutorial/start/cert.html if you need guidance on how to set this up.

## Workflow creation

The minimal execution line for a workflow is
```bash
${O2DPG_ROOT}/MC/bin/o2dpg_sim_workflow.py -gen <generator> -eCM <emc energy  [GeV]>
# OR
${O2DPG_ROOT}/MC/bin/o2dpg_sim_workflow.py -gen <generator> -eA <energy of first incoming beam [GeV]> -eB <energy of second incoming beam [GEV]>
```
meaning that at least the beam energies and the generator must be specified.

If you use `pythia8` as your generator **and you do not** pass a process with `-proc <process>`, the simulation will fail due to a missing configuration (see also [here](../generators/generatorso2.md#pythia8)). Hence, also here one needs to pass a valid configuration, but this time like so
```bash
${O2DPG_ROOT}/MC/bin/o2dpg_sim_workflow.py -gen pythia8 -eCM <emc energy  [GeV]> -confKey "GeneratorPythia8.config=<path/to/config>"
```

Simulations run from a workflow are done in units of timeframes and the number of timeframes to be simulated is set with `-tf <nTFs>`. The number of events generated per timeframe is given by `-ns <nEvents>` (optional, since it has a default value set).

By default, the workflow description is written to `workflow.json`.

### Embedding

The workflow can also be created for a simulation where signal type events are embedded into a certain type of background events. To enable this feature, pass the flag `--embedding`. For the background events there are the following arguments
* `-nb <nEvents>`: number of background events to be simulated,
* `-genBkg <generator>`: generator used for background generation,
* `-colBkg <system>`: collision system of background events,
* `-procBkg <proc>`: process for background generation (only valid when the background generator is Pythia8),
* `-confKeyBkg <confKeyValuePairs>`: additional key-value pairs passed to background generation and transport.

## Workflow running

The minimal execution line is
```bash
${O2DPG_ROOT}/MC/bin/o2_dpg_workflow_runner.py -f workflow.json
```
There are a few very useful command-line options for this one though
* `-tt <regex>` which specifies the "target task" up to which the workflow should be executed,
* `--mem-limit <mem limit [MB]>`: instructs the runner to only execute tasks so that the memory limit is not exceeded,
* `--cpu-limit <number of CPUS>`: instructs the runner to only execute tasks so that the CPUlimit is not exceeded.
* `--rerun-from <regex>`: force the runner to start at given tasks whose name matches the `<regex>`,
* `--target-labels <list> <of> <target> <labels>`: each task has labels assigned; run all tasks that have at least one of the specified labels.

The runner tries to execute as many tasks in parallel as possible. So while in the beginning the transport might take some time, quickly your terminal will fill up with the tasks running on top of the simulation results.

Often what you might want to do is running the full chain to obtain final `AO2D.root`. To achieve this and to not run tasks that are not needed, pass `-tt aod`.

### About finished tasks

Once a task is done, it will never be repeated unless you delete the `<task_name>_log_done` in the directory. Remove that file and run again.
 To make sure that all depending tasks are properly rerun, consider launching the runner with
```bash
${O2DPG_ROOT}/MC/bin/o2_dpg_workflow_runner.py -f workflow.json --rerun-from <task_name> -tt <your_target_task>
```
and there is no need to remove `<task_name>_log_done`.

Indeed, you can simply rerun from one task and at the same time define it be the target task and no file removal is necessary, just do
```bash
${O2DPG_ROOT}/MC/bin/o2_dpg_workflow_runner.py -f workflow.json --rerun-from <task_name> -tt <task_name>
```

## QC and additional steps

The standard QC steps can be included in the workflow with the flag `--include-qc`. To run all QC tasks, do
```bash
${O2DPG_ROOT}/MC/bin/o2_dpg_workflow_runner.py -f workflow.json --target-labels QC
```

In addition, there is a small set of analyses that can be included in the workflow. They are meant for testing purposes and their configuration is not optimised to produce state-of-the-art analysis results. But you can use that to make sure that the AODs are generally sane. To configure a workflow, pass the `--include-analysis` and then launch the runner
```bash
${O2DPG_ROOT}/MC/bin/o2_dpg_workflow_runner.py -f workflow.json --target-labels Analysis
```

## Adjusting resources

If you find the runner terminating with
```bash
runtime error: Not able to make progress: Nothing scheduled although non-zero candidate set

**** Pipeline done with failures (global_runtime : 250.285s) *****
```

and at the same time your system has `16 GB` of RAM, try to artificially increase the memory limit for the runner with
```bash
${O2DPG_ROOT}/MC/bin/o2_dpg_workflow_runner.py -f workflow.json -tt aod --mem-limit 18000
```

## Troubleshooting

### What are the interesting log files?

When a certain stage in the workflow crashes, the workflow runner exist with something like
```bash
command ${O2_ROOT}/bin/o2-sim-digitizer-workflow -b --run --condition-not-after 3385078236000 -n 1 --sims sgn_1 --onlyDet FT0,FV0,CTP --interactionRate 50000 --incontext collisioncontext.root --disable-write-ini --configKeyValues "HBFUtils.orbitFirstSampled=0;HBFUtils.nHBFPerTF=128;HBFUtils.orbitFirst=0;HBFUtils.runNumber=310000;HBFUtils.startTime=1550600800000" --combine-devices had nonzero exit code 1
Stop on failure  True
setting up ROOT system
ft0fv0ctp_digi_1 failed ... checking retry
```
The suffix `_<i>` refers to the affected timeframe, hence in this case the log file of interest would be `tf1/ft0fv0ctp_digi_1.log`.

There is a special case for when the detector transport aborts. In that case, the reported log file would be `tf<i>/sgnsim_<i>.log` or `bkgsim.log`. Since the detector simulation launches multiple workers, there are additional logs where the workers' output is piped into. These are
1. `tf<i>/sgn_<i>_workerlog0`,
1. `tf<i>/sgn_<i>_serverlog`,
1. `tf<i>/sgn_<i>_mergerlog`.

### When a workflow run crashes

1. Make sure that O2 and O2DPG are compatible. Although O2DPG is a standalone package containing mostly scripts **using/executing** O2 code, some O2 features (such as particular arguments for certain executables) might be incompatible between the utilised O2 and O2DPG versions.
1. If you have a custom local installation oif the software but you would expect a workflow to run through for good reasons, then
    1. check the integrity of your installation,
    1. potentially update your installation (not only update the development packages but also `alidist`),
    1. run the workflow via a software version from `cvmfs` (e.g. available on `lxplus`),
    1. try a different machine/working environment (e.g. `lxplus` might work if the workflow is not too heavy).

1. In case of corrupt CCDB objects, this could be a genuine problem. However, in case of a hickup, a corrupted object might be stored in the local CCDB snapshot. Note, that the snapshot is usually stored in a hidden directory `.ccdb`.
    1. You can try to remove the affected snapshot and rerun from where you are.
    1. You can completely remove everything **including** the `.ccdb` directory. Note, that a simple `rm -r *` would **not** remove the hidden directory.
    1. If the problem persists and you think it is genuine, please get in touch.

### When a workflow run hangs

1. Make sure that O2 and O2DPG are compatible. Although O2DPG is a standalone package containing mostly scripts **using/executing** O2 code, some O2 features (such as particular arguments for certain executables) might be incompatible between the utilised O2 and O2DPG versions.
1. Kill the run and inspect the log files of the hanging task (see [above](#what-are-the-interesting-log-files)).

{% include list.liquid all=true %}
