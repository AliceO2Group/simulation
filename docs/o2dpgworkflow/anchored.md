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

The following is an example to run one anchored simulation, in this case `apass2` anchored to `RUN` 544121. Note that if one wants to consistently fill a run, the number of timeframes must be the same for all `CYCLES` and `SPLITIDS`.

```bash
# example anchoring
# taken from https://its.cern.ch/jira/browse/O2-4586
export ALIEN_JDL_LPMANCHORPASSNAME=apass2
export ALIEN_JDL_MCANCHOR=apass2
export ALIEN_JDL_COLLISIONSYSTEM=Pb-Pb
export ALIEN_JDL_CPULIMIT=8
export ALIEN_JDL_LPMPASSNAME=apass2
export ALIEN_JDL_LPMRUNNUMBER=544121
export ALIEN_JDL_LPMPRODUCTIONTYPE=MC
export ALIEN_JDL_LPMINTERACTIONTYPE=PbPb
export ALIEN_JDL_LPMPRODUCTIONTAG=LHC24a1
export ALIEN_JDL_LPMANCHORRUN=544121
export ALIEN_JDL_LPMANCHORPRODUCTION=LHC22o
export ALIEN_JDL_LPMANCHORYEAR=2023

export NTIMEFRAMES=2
export NSIGEVENTS=2
export SPLITID=100
export PRODSPLIT=153
export CYCLE=0

# on the GRID, this is set, for our use case, we can mimic any job ID
export ALIEN_PROC_ID=2963436952

# run the central anchor steering script; this includes
# * derive timestamp
# * derive interaction rate
# * extract and prepare configurations (which detectors are contained in the run etc.)
# * run the simulation (and QC)
${O2DPG_ROOT}/MC/run/ANCHOR/anchorMC.sh
```

## Behind the scenes

The procedure steered behind the scenes is quite involved. The following figure shall provide some overview.

![anchored run](../images/anchored_run.png)
