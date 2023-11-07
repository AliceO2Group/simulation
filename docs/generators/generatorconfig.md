---
sort: 4
title: Generator configuration
---

# Generator configuration

There are various ways to pass specific generator configurations to the simulation run. For instance
```bash
o2-sim --configFile <path/to/config.ini>
```

Similarly, this works for the [`o2dpg_sim_workflow.py`](../o2dpgworkflow/README.md/#o2dpg-workflows) with
```bash
o2dpg_sim_workflow.py -gen pythia8 -ini <path/to/config.ini>
```

This way is the preferred way and we are indeed now in a transition phase after which this will be the only accepted way of generator configuration for official productions on the GRID. In addition, the configuration files must be found in the [O2DPG Git repository](https://github.com/AliceO2Group/O2DPG).
For this reason, there is now a new CI in place which runs tests on all these files (they will also simply be called `ini` files in the following).

The configuration files are placed at `O2DPG/MC/config/<PWG>/ini/<config>.ini`. These can contain different sections for configuring generators in general but also additional triggers on the produced particles can be added,
(see for instance [here](https://github.com/AliceO2Group/O2DPG/blob/546ec5d03a57d189b4ea3c92c5a8e1d7af812d41/MC/config/PWGDQ/ini/GeneratorHF_ccbarToMuonsSemileptonic_fwdy.ini)).

In the given example, there is `Pythia8` and `External` defined in the file. That means, the respective configurations will be picked up eventually, depending on the `-g <generator>` argument of `o2-sim`. Note, that multiple configuration might take effect. For instance, if your `external` generator derives from
[`GeneratorPythia8`](https://github.com/AliceO2Group/AliceO2/blob/dev/Generators/include/Generators/GeneratorPythia8.h), then the `External` as well as the `Pythia8` section of your configuration will be used.

## Generator tests

For at least one generator that is configured by an `ini` file, there must be a test in O2DPG available. This **has to be placed** in `O2DPG/MC/config/<PWG>/ini/tests/<config>.C`. Hence, it must have the same name as the configuration it refers to one directory above. What is expected to be tested is the integrity of the `o2sim_Kine.root` file which is produced by a simulation run.
In a test, you can always assume it is there in the current directory. There is also more information on [MC kinematic files](../transport/mckine.md).

A test macro has the following form:
```cpp
int Pythia8()
{
    // potential preparation

    // example of opening the kinematics and reading the MC tracks
    std::string path{"o2sim_Kine.root"};
    TFile file(path.c_str(), "READ");

    o2::steer::MCKinematicsReader reader("o2sim", o2::steer::MCKinematicsReader::Mode::kMCKine);
    auto nEvents = reader.getNEvents(0); // get events from source 0, which is our only source

    // example of looping over events and tracks
    for (int i = 0; i < nEvents; i++) {
        std::vector<o2::MCTrack> const& tracks = reader.getTracks(i); // this is a short-cut, implicitly source 0
        for (auto& track : tracks) {
            // do the checks
            // suppose something fails
            if (!trackNotPassed) {
                return 1;
            }
        }
        // optionally do some tests on the MCHeader
        o2::dataformats::MCEventHeader const& header = reader.getMCEventHeader(0, i); // the first is the source, again, we only have that one source
        // ...
    }

    return 0;
}

int External()
{
    // same logic as above
}
```

**The CI test will fail if there is not at least one generator tested.** The return type must be an integer, where `0` marks success and any other value indicates failure.

In addition, the `o2sim_Kine.root` is automatically tested by some generic tests. For instance it will made sure that there are particles that are marked to be transported. If not, the test will also fail.
On top of that it is made sure that the particles' status codes are set correctly (for more information on status code see [here](README.md/#generator-status-codes-flagging-particles-to-be-trackedtransported)).

For a test example, please refer to [this test](https://github.com/AliceO2Group/O2DPG/blob/546ec5d03a57d189b4ea3c92c5a8e1d7af812d41/MC/config/PWGDQ/ini/tests/GeneratorHF_JPsiToMuons_fwdy.C).

**Note** that the tests are also triggered when macros mentioned in some configuration file are changed or when a test itself changes.

### Run the test locally

You do not have to wait for the CI but you can make sure that everything is working already on your development machine if possible. To do so, you have to have an appropriate software environment loaded;
preferably that could be `O2sim`, but `O2` in conjunction with `O2DPG` works as well (unless you need additional packages, such as for instance [AEGIS](https://github.com/AliceO2Group/AEGIS)).

First of all, let's agree on terminology for the following
* `${O2DPG_SOURCE}` shall denote the directory where you develop,
* `HEAD` is `git` terminology and points to a certain state of your `git` history, usually the latest commit,
* "unstaged changes" in git are those which are not yet added to be committed (whenever you develop but have not yet done `git add`)

The test is designed to check code changes and to test their impact. In order for the test script to detect changes, it basically tries to find changed file via `git diff` between a given pair of commits.
* If there are unstaged changes, the test will compare these changes with respect to `HEAD`.
* If there are no unstaged changes in `${O2DPG_SOURCE}`, the test will by default compare `HEAD` (assuming that this contains the relevant changes you made) with `HEAD~1`.
* If you want to provide two specific commits and test everything that has changed between these commits, you need to set `O2DPG_TEST_HASH_BASE=<base-commit>` and `O2DPG_TEST_HASH_HEAD=<later-commit>` (see below).

The full command would be
```bash
O2DPT_TEST_REPO_DIR=${O2DPG_SOURCE} O2DPG_TEST_HASH_BASE=<base-commit> O2DPG_TEST_HASH_HEAD=<later-commit> ${O2DPG_ROOT}/test/run_generator_tests.sh
```

The output will be written to `o2dpg_tests`.

The additional environment variables and options one can set can be seen by running
```bash
${O2DPG_ROOT}/test/run_generator_tests.sh -h

usage: run_tests.sh [--fail-immediately] [--keep-artifacts]

  FLAGS:

  --fail-immediately : abort as soon as the first tests fails
  --keep-artifacts : keep simulation and tests artifacts, by default everything but the logs is removed after each test

  ENVIRONMENT VARIABLES:

  O2DPG_TEST_REPO_DIR : Point to the source repository you want to test. (required if the current or parent directory is not the git repository to be tested)
  O2DPG_TEST_HASH_BASE : The base hash you want to use for comparison (optional)
  O2DPG_TEST_HASH_HEAD : The head hash you want to use for comparison (optional)

  If O2DPG_TEST_HASH_BASE is not set, it will be looked for ALIBUILD_BASE_HASH.
  If also not set, this will be set to HEAD~1. However, if there are unstaged
  changes, it will be set to HEAD.

  If O2DPG_TEST_HASH_HEAD is not set, it will be looked for ALIBUILD_HEAD_HASH.
  If also not set, this will be set to HEAD. However, if there are unstaged
  changes, it will left blank.
```
