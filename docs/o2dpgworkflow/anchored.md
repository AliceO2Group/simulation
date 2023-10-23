---
sort: 2
title: Anchored MC
---

# Anchored MC

In "anchored" MC simulations, conditions are set to match those during a real data taking run at a given time such as LHC filling scheme, included ALICE detectors, interaction rate etc.
Anchored MC productions are crucial for physics analyses to have realistic simulated samples.

The anchoring procedure is slightly more involved than unanchored MC runs. What we need to achieve is constructing a fitting [workflow similar to the unanchored case](README.md/#workflow-creation).

Here is the step-by-step procedure:

**Determine reconstruction options and enabled detectors**
```bash

# create your working directory and change into it
mdkir ${WORKDIR}
cd ${WORKDIR}

# set run number etc.
export RUNNUMBER=<run-number>
export PASS=<pass>
export PERIOD=<period>
export BEAMTYPE=<beamtype>
export RUNNUMBER=<run-number>

# copy what needs to be run because we will tweak it in a sec
cp $O2DPG_ROOT/DATA/production/configurations/asyncReco/async_pass.sh .
cp $O2DPG_ROOT/DATA/production/configurations/asyncReco/setenv_extra.sh .

# set what is necessary in MC
sed -i 's/GPU_global.dEdxUseFullGainMap=1;GPU_global.dEdxDisableResidualGainMap=1/GPU_global.dEdxSplineTopologyCorrFile=splines_for_dedx_V1_MC_iter0_PP.root;GPU_global.dEdxDisableTopologyPol=1;GPU_global.dEdxDisableGainMap=1;GPU_global.dEdxDisableResidualGainMap=1;GPU_global.dEdxDisableResidualGain=1/' setenv_extra.sh
# disable running the reco, we will get everything from our MC run
sed -i '/WORKFLOWMODE=run/d' async_pass.sh

# prepare
export IGNORE_EXISTING_SHMFILES=1
touch list.list

# this will provide us with the log file as well as workflowconfig.log...
./async_pass.sh ${CTF_TEST_FILE:-""} 2&> async_pass_log.log

# ...which will now be parsed to yield config-config.json
${O2DPG_ROOT}/UTILS/parse-async-WorkflowConfig.py

# the following variables of course should be set
baseargs="-col ${COLSYSTEM} -eCM 5360 -tf ${NTIMEFRAMES} --split-id ${SPLITID} --prod-split ${PRODSPLIT} --cycle ${CYCLE} --run-number ${RUNNUMBER}"

remainingargs="-gen pythia8 -proc heavy_ion -seed ${SEED} -ns ${NSIGEVENTS} --include-local-qc --pregenCollContext"
remainingargs="${remainingargs} -e ${SIMENGINE} -j ${NWORKERS}"
remainingargs="${remainingargs} -productionTag ${ALIEN_JDL_LPMPRODUCTIONTAG:-local_anchorTest_tmp}"
# and here comes the config-config.json that we constructed above and contains additional options for DPLs as well as detectors and detector sources etc.
remainingargs="${remainingargs} --anchor-config config-json.json"

# no we create the final workflow that will be digested by the runner
${O2DPG_ROOT}/MC/bin/o2dpg_sim_workflow_anchored.py ${baseargs} -- ${remainingargs} &> timestampsampling_${RUNNUMBER}.log

# We grep the timestamp in order to be able to pre-fetch some CCDB objects
TIMESTAMP=`grep "Determined timestamp to be" timestampsampling_${RUNNUMBER}.log | awk '//{print $6}'`
# this is what we want to fetch
CCDBOBJECTS="/CTP/Calib/OrbitReset /GLO/Config/GRPMagField/ /GLO/Config/GRPLHCIF /ITS/Calib/DeadMap /ITS/Calib/NoiseMap /ITS/Calib/ClusterDictionary /TPC/Calib/PadGainFull /TPC/Calib/TopologyGain /TPC/Calib/TimeGain /TPC/Calib/PadGainResidual /TPC/Config/FEEPad /TOF/Calib/Diagnostic /TOF/Calib/LHCphase /TOF/Calib/FEELIGHT /TOF/Calib/ChannelCalib /MFT/Calib/DeadMap /MFT/Calib/NoiseMap /MFT/Calib/ClusterDictionary /FT0/Calibration/ChannelTimeOffset /FV0/Calibration/ChannelTimeOffset /GLO/GRP/BunchFilling"

# where we cache all CCDB objects
export ALICEO2_CCDB_LOCALCACHE=$PWD/.ccdb

${O2_ROOT}/bin/o2-ccdb-downloadccdbfile --host http://alice-ccdb.cern.ch/ -p ${CCDBOBJECTS} -d ${ALICEO2_CCDB_LOCALCACHE} --timestamp ${TIMESTAMP}

echo "run with echo in pipe" | ${O2_ROOT}/bin/o2-create-aligned-geometry-workflow --configKeyValues "HBFUtils.startTime=${TIMESTAMP}" --condition-remap=file://${ALICEO2_CCDB_LOCALCACHE}=ITS/Calib/Align,MFT/Calib/Align -b
mkdir -p $ALICEO2_CCDB_LOCALCACHE/GLO/Config/GeometryAligned
ln -s -f $PWD/o2sim_geometry-aligned.root $ALICEO2_CCDB_LOCALCACHE/GLO/Config/GeometryAligned/snapshot.root

```

Now finally you can run the runner as explained [here](README.md/#workflow-running).
