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

## Some useful information

It is not possible to cover all use cases here but a few important remarks and pointers are summarised in the following.

## Workflow creation

The minimal execution line for a workflow is
```bash
${O2DPG_ROOT}/MC/bin/o2dpg_sim_workflow.py -gen <generator> -eCM <emc energy  [GeV]>
# OR
${O2DPG_ROOT}/MC/bin/o2dpg_sim_workflow.py -gen <generator> -eA <energy of first incoming beam [GeV]> -eB <energy of second incoming beam [GEV]>
```
meaning that at least the beam energies and the generator must be specified.

If you use `pythia8` as your generator **and you do not** pass a process with `-proc <process>`, the simulation will fail due to a missing configuration (see also [here](../generators/generatorso2.md#pythia8)). Hence, also here one eneds to pass a valid configuration, but this time like so
```bash
${O2DPG_ROOT}/MC/bin/o2dpg_sim_workflow.py -gen pythia8 -eCM <emc energy  [GeV]> -confKey "GeneratorPythia8.config=<path/to/config>"
```

Simulations run from a workflow are done in units of timeframes and the number of timeframes to be simulated is set with `-tf <nTFs>`. The number of events generated per timframe is given by `-ns <nEvents>` (optional, since it has a default value set).

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
* `--cpu-limit <numpber of CPUS>`: instructs the runner to only execute tasks so that the CPUlimit is not exceeded.
* `--rerun-from <regex>`: force the runner to start at given tasks whose name matches the `<regex>`,
* `--target-labels <list> <of> <target> <labels>`: each task has labels assigned; run all tasks that have at least one of the specified labels.

The runner tries to execute as many tasks in parallel as possible. So while in the beginning the transport might take some time, quickly your terminal will fill up with the tasks running on top of the simulation results.

Often what you might want to do is running the full chain to obtain final `AO2D.root`. To achieve this and to not run tasks that are not needed, pass `-tt aod`.

### Troubleshooting

For the runner, it is not strictly possible to respect `--mem-limit <mem limit [MB]>` and `--cpu-limit <numpber of CPUS>` at all times. Indeed, each task comes with *resource estimates* from which the runner decides whether or not a task can be launched. So it can happen in a few rare cases that the resource limits are exceeded for a short amount of time.

If the runner just stops with
```bash
runtime error: Not able to make progress: Nothing scheduled although non-zero candidate set

**** Pipeline done with failures (global_runtime : 250.285s) *****
```
that points to the fact that either you restricted the resources too much or that your machine does not have enough resources to offer in the first place.

In the former case, try to increase `--mem-limit <mem limit [MB]>` or `--cpu-limit <numpber of CPUS>`. Most of the times when this happens it is the memory that is too small. But it might also be the case that you choose the `--cpu-limit` too high or the number of simulation workers exceeds the `--cpu-limit`.

If your target task is the AOD creation but the final merging of AODs from several time frames fails, most likely you have not loaded the `O2Physics` environment. However, `O2Physics` is implied when loading `O2sim`.

{% include list.liquid all=true %}
