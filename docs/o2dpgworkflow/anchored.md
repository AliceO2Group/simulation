---
sort: 2
title: Anchored MC
---

# Anchored MC

In "anchored" MC simulations, conditions are set to match those during a real data taking run at a given time such as LHC filling scheme, included ALICE detectors, interaction rate etc.
Anchored MC productions are crucial for physics analyses to have realistic simulated samples.

An anchored simulation is bound to a run which is identified by a run number. A run in turn spans from the start-of-run (SOR) to the end-of-run (EOR). This is sketched in the figure.
![anchored split cycle](../images/anchored_split_cycle.png)

One anchored simulation run corresponds to one specific `CYCLE` of one `SPLITID` and contains a given number of timeframes as indicated by the big blue box on the bottom right.
A full `RUN` is covered when all `CYCLES` have been produced for all `SPLITIDS`.

There are two examples for anchored simulations:

* [PbPb](https://github.com/AliceO2Group/O2DPG/blob/master/MC/run/ANCHOR/tests/test_anchor_2023_apass2_PbPb.sh),
* [pp](https://github.com/AliceO2Group/O2DPG/blob/master/MC/run/ANCHOR/tests/test_anchor_2023_apass2_pp.sh).

## Behind the scenes

The procedure steered behind the scenes is quite involved. The following figure shall provide some overview.

![anchored run](../images/anchored_run.png)
