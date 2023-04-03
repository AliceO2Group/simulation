---
sort: 6
title: MC GRID productions
---

# MC GRID productions

In order to collect enough statistics, Monte Carlo simulations typically need to be spread out and run on large compute farms.
For this, we use the Worldwide LHC Computing Grid (WLCG) <https://wlcg.web.cern.ch/> by default, which in rough terms collects compute farms into an collaborative abstract layer to which compute jobs can be submitted.

The ALICE interface to this system is called AliEn <https://jalien.docs.cern.ch/>.


A few ways exist to make use of the GRID computing power for simulation:

## Official (large scale) productions

Official productions for ALICE physics working groups or larger productions for research and development
(detector groups, etc.) should be handled via the Data Processing Group (DPG).

A ticket with type "Production Request" should be created in [JIRA](https://alice.its.cern.ch/jira/projects/O2), explaining the purpose, the setup, the software version to be used and so on. The production will then be orchestrated by the DPG production manager.

Productions may need to be approved by the Physics Board depending on resource usage.

## Personal (development or test) productions

Each member of the ALICE collaboration has a personal compute quota and one can submit jobs spanning
O(100) CPUs for development and testing cycles which is a consirable resource pool.

Here, one needs to create a JDL file describing the job, upload executables to the GRID and use a a tool like `alien.py` to interact
with the GRID services. Documentation can be found [here](https://jalien.docs.cern.ch/), with the JDL job reference available [here](https://alien.web.cern.ch/content/documentation/howto/user/jobs).


The process of setting up JDLs and copying necessary files can be cumbersome.
For this reason, there exists also a [tool](https://github.com/AliceO2Group/O2DPG/blob/master/GRID/utils/grid_submit.sh)
which allows to submit a locally existing script to run on the GRID without much boilerplate. The tool is work-in-progress and needs more generalizations but may be a good starting point.


{% include list.liquid all=true %}
