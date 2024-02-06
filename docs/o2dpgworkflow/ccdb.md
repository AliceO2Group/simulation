---
sort: 3
title: CCDB
---

# CCDB

As many of the `O2` executables, also the simulation depends heavily on the CCDB to retrieve configurations, meta information or objects required during the run.

## Prerequisites

A valid GRID **token** must be present, see [here](../gettingstarted/README.md#alien-grid-token)

## CCDB snapshots

During the execution of the simulation workflow, different tasks need CCDB objects. The simulation of different timeframes is parallelised so there are multiple tasks that require the same objects. This is one reason why we use **snapshots**:
When an object is requested for the first time, it os downloaded and **cached** so that following requests can be redirected to that chached object instead of querying the CCDB again.
By default the cache directory is `${CWD}/ccdb` but it can be changed by
```bash
export ALICEO2_CCDB_LOCALCACHE=/path/to/snapshot_cache
```
**NOTE**: Make sure to set this to an absolute path.

This mechanism can also be useful to run a simulation without the need to access the CCDB at all: Simply refer to or copy a snapshot directory from a previous simulation run to the directory you are running the current simulation in.
**NOTE**: No check is done on whether the timestamp of your simulation corresponds to the cached objects; they will simply be used as-is and are only identified by their path.
