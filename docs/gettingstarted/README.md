---
sort: 0
title: Getting started
---

# Introduction

The entire simulation chain in particle and heavy-ion physics typically involves several steps as follows
1. generation of primary particles,
1. transport of primary particles through the defined detector geometry and creation of so-called *hits*,
1. digitisation of hits left by the tracks.

After that, the data look in principle similar to those data which is acquired by the physical detector experiment. This can be followed by further steps which are very similar for the experiment and simulation, including reconstruction (of tracks and vertices), matching of tracks among multiple sub-detectors and finally a data structure that is the input to physics analyses. The final data structure is stored in `ROOT` files, typically called `AO2D.root`. This documentation focuses on the generation, detector transportand digitisation.

# Quick start

## Generation and transport

To steer the generation and transport, simply run
```bash
o2-sim -n 10
```
which will simulate 10 events whose primary particles will be transported through the ALICE detector geometry. Hits are stored in `ROOT` files for each sensitive detector. In addition it will leave you with a file called `o2sim_Kine.root` which collects the information about all particles that were produced in primary generation as well as secondaries coming from the transort and originating from the interaction of the particles with the detector material. Please refer to the [transport](../transport/) or [generator](../generators/) section for more extensive documentation.

**..under construction...**

{% include list.liquid all=true %}
