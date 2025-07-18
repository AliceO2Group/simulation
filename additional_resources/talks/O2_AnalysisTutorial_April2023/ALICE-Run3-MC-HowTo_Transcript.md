Okay, good. So in this talk, I'm turning to something that is I think boundary to physics analysis in terms of detector
simulation. And I'd like to give you some practical information of how you as an analyst,
say, can run Run3 detector simulations and how to add it to your toolbox. But compared
to other talks, this might be a bit introductory and on an elementary level. Okay, so in particular, I think
my goals are to get you to have an overview of the Run3 simulation ecosystem and a basic
understanding how to run it. 

So in particular, the goal is to get to know fundamental use cases of the o2-sim
executable, which is the main system for event generation and transport simulation.
And basically, then also to talk a little bit about basic event generation usage and how
you can configure it. And finally, be introduced to the O2DPG repository, which is
our official integrated Monte Carlo production pipeline that has everything
from event generators to AOD production as well as analysis QC tasks that can be performed as part of the pipeline.

As I was saying, I think this is an introductory overview for analysts and a foundation for other parts of the tutorial 
which might give more specialized content.

Okay, I think the most important slides may be this one, showing our contact information. So how should you get in touch with us?
And here we have foremost the bi-weekly WP12/WP13 meetings, where you can connect and ask questions and there is a CERN e-group
to which you can subscripte to get the meeting invitations.
Secondly, there are dedicated Mattermost channels for simulation over which we prefer to communicate.
And in particular, we have two of them for more generic simulation
questions or something that's more specific to O2DPG production pipeline. Lastly,
for things like feature requests or bug reports, we invite you to open JIRA tickets in the O2 project.

Apart from that, on the documentation side, we have a new documentation project which somehow replicates
what physics analysis has done. And then we have some older stuff that you can also take a look
at. But I'd like to point out that unfortunately, this is still in an early stage. So here really,
please give feedback, ask questions or even contribute. That would be fantastic.

Okay, just a very quick reminder about the software environment required to run ALICE detector simulations. I mean, you know this from
many previous talks, but as a reminder this slide shows that simulation for Run3 needs the O2Sim
package that you can build and enter, or just take from CVMFS in precompiled form. And I think
this should contain everything that is needed for detector simulation.

Next, although potentially a bit superfluous, I still wanted to give a short reminder of the classical
computing pipeline in High energy physics and point out the role of simulation. And for this, I basically depict first of all the data pipeline from real particle collisions triggering detector ouput which is fed into the reconstruction software to produce, finally,
our AOD or analysis object data files. These are then used for actual physics analysis to produce scientific papers.
The role of simulation then is to do this in a completely virtual environment, let's say,
virtual or synthetic, by producing Monte Carlo generated events, which are then simulated
based on physics models to produce essentially the same sensor data from which we can also have
AODs. And we do this, of course, to study all different kinds of things like detector system design,
reconstruction algorithm calibration or testing, efficiency calculations etc.

Okay, so on the next slide let's have a quick look into the ALICE Run3 simulation ecosystem, which is quite standard for an HEP experiment.
There is the core or actual simulation part which comprises the event generation, the transport simulation done by Geant, and the dector specific digitization algorithmes which convert the Geant hit output
into an the actual electronics response of each detector. And this is basically two of those boxes which are depicted here. But then in addition, it's important to
know that Monte Carlo workflows also may exercise all reconstruction steps, or quality control analysis as a consequence
of this. So these algorithms are also part also of the simulation ecosystem and the global Monte Carlo pipeline.
In our case, the integration and configuration of all parts into a coherent workflow is actually
done in the O2DPG repository.
Next, I have a quick reminder of the main data products in the simulation pipeline.
Here basically, when you run it from left to right, we produce in the transport simulation part
the geometry of the ALICE detector, the kinematics files containing the track properties for primaries
and secondaries particles, and lastly there are the detector response files, which we call hits. And this is basically
then picked up by the digitization algorithms to produce the digit sub-detector timeframes, which is sort of
comparable or close to the raw detector output of the real experiment. And then of course, after that, we just have the typical
reconstruction pipeline. So reconstruction picks these up the digits produce the global tracks,
primary vertices, energy reconstruction etc to finally produce the AO2D.root file for the analysis
object data.

Okay, so with this, I'd like to turn to the o2-sim` executable, which is
our particle detector simulator for the ALICE RUN3. And this basically implements the ALICE detector
geometry and material description on top of well-known particle transport simulation engines
that I think all of you have heard about. And this is in particular Geant4, which is our default engine,
Geant3 and FLUKA. And actually, the good thing in ALICE is that we can use all of these engines interchangeably. This is is a major benefit or advantage of our simulation setup
in comparison to other approaches in HEP, which solely rely on Geant4. The ability to doing radiation studies with FLUKA is one such benefit.

The main tasks of the o2-sim program is, as I was saying previously, firstly the geometry
creation. Secondly, o2-sim also performs event generation to provide the primary particle collisions.
Finally, it performs the simulation of the physics interaction of the particles with the detector material. And it transports those particles
within our setup until they exit the detector or they stop. And then, as I was saying, it also
creates the hits, which are sort of energy deposits as a pre-stage of what later the detector
digitizers use to produce the actual sensor output.

All of this is quite standard and I will not go into the details of these too much.
But I would like to mention, that the new feature in ALICE RUN3, is that the detector transport simulation in o2-sim, is now
a scalable multi-core simulation with sub-event parallelism, which basically allows us to use
very big servers, big compute nodes, and to obtain results for individual large events or collisions
quite quickly. So instead of waiting an hour or so for one event to have
passed through, you can do it really in a matter of minutes.

Another unrelated comment on o2-sim, is that it treats events/collisions
in complete isolation. So at this moment, there's no timeframe concept yet,
because this only enters much later during digitization when we produce the detector sensor data.

Okay. So in order to show you basically how you would use o2-sim, I just depict a couple of
examples, starting with a quite easy one. So you would simply call o2-im on the command line
like so, and you would specify the number of events in the generator. And in this particular case,
this thing generates 10 default Pythia8 proton proton events and it transports them through
the complete ALICE detector and produces our hits and kinematics output.

So in a slightly more complicated example, you can use this example to generate 10 default Pythia8 pp events and transport them
with eight Geant3 workers through everything but the ZDC detector and also use a different field than the standard
one. So in this case, two kilo gauss or something. So you see that you can configure o2-sim by basically giving it different options on the command line.


So by default, we always have Geant4 enabled. If you want to use Geant3, you would use the second
example, but we'd like to push Geant4 in Run3 and this is why the default.
Okay. And then maybe the third example is useful for pure generator output analysis. In this case,
you just call the generator part and generate 10 Pythia8 pp events and do nothing else. So there's
no transport. The kinematics file will only contain the generated events. Okay. And as I was saying,
or maybe mentioning is that --help lists the main options and shows some defaults that we are
using.

Okay. This is maybe not so important, but I still wanted to flash this because sometimes
you may want to see what's going on inside. And o2-sim here produces three log files
with different purpose. The generator part produces this o2sim_serverlog file
where you can see output from the event generation phase and the o2sim_workerlog0
file contains output from the Geant4 transportation stage, which may be useful to take a look at
to see what's going on.

An important output of the o2-sim program mainly is the kinematics output
from transport simulation. And this is often the most interesting for physics analysis because it contains, as you may know, creation vertices, momenta and other properties of the primary
and the secondary particles, which are created in the simulation. It also contains information
about the physics creation processes for each of those particles or how they relate to each
other in terms of mother daughter relationships. The data is based on a special MCTrack class
that we have provided and which is similar to ROOT's TParticles class but much more lightweight in terms of memory usage and disk usage.
For each event, there's basically one entry of a vector of such tracks in a ROOT TTree. And as you may know, you can just browse
this thing using ROOT's JSRoot or TBrowser system or whatever to get a look at the data
as this is depicted on the right hand side. Something that I'd like to mention is that
by default, the kinematics data is pruned. So it doesn't contain all the particles,
but only the particles which are relevant for physics or reconstruction.
But you can ask the system to really produce everything to get all the billions of secondaries
that are produced. And then in addition, some metadata information on a more global event level
is also available, but it's not part of the kinematics root file, but it's part of the MC header file. And in this file, one may look up important parameters like the impact parameter of the generated collisions or other global properties such as collision vertices.

Okay. Then there are quite important helper classes to access and navigate Monte Carlo kinematics.
And we provide this basically because navigating and reading
through these things can be quite cumbersome since it's essentially repeating ROOT IO boilerplate and
things that you would have to put over and over again. And here two main utility classes are important.
One is the so-called Monte Carlo kinematics reader (MCKinematicsReader), which is a class to easily read and
retrieve tracks for a given event number or a Monte Carlo label (MCLabel). And then there is this MC
track navigator (MCTrackNavigator), which is a class to navigate through the mother-child relationships between Monte Carlo tracks or to query all sorts different physics properties on MCTracks. And there's an example on the
right hand side, which basically shows you how to read all the Monte Carlo tracks from
the stored kinematics and then loop over all the tracks and determine a direct mother or
the primary ancestor of all those particles.

Okay. With this, I'd like to turn to event generation, concentration on the basics. So o2-sim has a couple of predefined generators implemented
and you select them with the minus G (-g) option. Foremost we offer a pre-configured Pythia8pp for
proton proton, and a pre-configured Pythia8hi for lead lead collisions. And then a couple of other things
such as a simple box generator, a generator that can use an external kinematics file as its source
and or we can also interface with generators providing standardized HepMC output. And this is just how you would select it.

And I think there's examples for all of these cases you can find under these links.
Then a word on Pythia8: Pythia8 has a slightly special role among the event generators as it is more deeply integrated in O2 compared to
other generators. And it is recommended to use Pythia8 whenever possible. When Pythia8 is used,
it can be fully configured via a special text file, such as the one shown on the right hand side.
such as the one shown on the right hand side. And some generator Pythia8 parameter that you would pass
to the executable, like described in the second box on this slide.
In order to configure the text file for the event configuration, we also provide a Python tool
that basically allows you to create this without much hassle,
basically based on a couple of parameters that you can give to the tool. So this is a convenience
thing for you to set up the configuration file for Pythia8. Now apart from Pythia8,
direct, let's say, compiled integration of specific generators is rather small in O2
compare to the previous AliRoot system. The idea is rahter to decouple more physics specific generator code
and configurations from our data taking code. If you'd like to avoid recompilation of O2
just because someone changes their generator config.
Rather here we prefer to integrate these things via so-called external generators,
which can be interfaced in o2-sim by using just-in-time ROOT macros in which we implement
a special TGenerator interface declared by the ROOT project.
And this basically allows to set up our generators at runtime in C++.
And the generator setup becomes more like a configuration problem
and that we can pass to o2-sim. And basically there's a little example shown on the right hand side
with a really minimal TGenerator implementation. It's not really complete but you would code a little
C++ snippet in a macro file that implements your generator and you can then pass this thing
to o2-sim as in the box shown on the upper part. And this method, as I'd like to highlight,
is really used in production. It's used by many physics working groups (PWGs) in the O2DPG production system.
And there are many examples showing how you can interface the typical hygiene or whatever
generators used in AliRoot also in o2-sim using this mechanism. Then in addition,
we also offer support for triggering. So event filtering or triggering is also flexibly supported
and this essentially works in the same way as the external
generators example I was showing on the last slide. Again, here you can implement
a trigger code in a sort of a macro which we pass to o20sim to have just-in-time compilation.
And I also think there's a nice example under this link in the SIM examples folder of AliceO2.
Something more advanced are deep triggers which allow you to trigger not only on the
vector or the collection of primary particles but also on the state of the
event generator of the underlying generator. But this is a little bit more advanced
but we also offer a code example for this in AliceO2.

Okay, then something quite useful to know for you is that o2-sim can be used as an on-the-fly
event generator for analysis. Basically, you can use it as a so-called generator service
that just injects its generated events into a DPL analysis topology without intermediate storage.
And this is useful for studies where you want to analyze or process
primaries only. And this goes back to a discussion we had
with David Chinelatto some time ago. He was really the main driver behind this but it should now be
implemented and I think it's also used by some PWGs and I think it will be covered tomorrow in
the PWG EM tutorial.


Okay, now I am switching direction and come to a discussion of the global Monte Carlo pipeline and integrated workflows that have the goal
produce simulated AODs. This certainly goes beyond the transport simulator and event generation phase
and needs to run also stages such digitization and reconstruction tasks.

And as you can imagine or know this is a complex system consisting of many executables or tasks
that somehow require consistent application and propagation of settings and configurations
to work nicely together. And this is of course hard to get right on your own
so better use a maintained setup. And this maintained setup for the Monte Carlo pipelines
on the GRID is provided in the O2DPG repository, but I'd like to highlight that the same repository is now
also used to configure and maintain the scripts for the data taking part on the EPN.

So, shortly, O2DPG provides the both authoritative setup for official Monte Carlo
productions for ALICE Run3 and also a runtime system to execute Monte Carlo jobs on our GRID computing infrastructure. O2DPG integrates all the relevant processing
tasks into a coherent and consistent environment to have a working pipeline from event generation
to AOD production and beyond. In addition, it also maintains the PWG specific generator
event generator configurations as versioned code, as well as code to perform testing and checking if these configurations are actually useful. So this is
done at the time when people ask for a pull request.

Okay so a little bit about the fundamental ideas
of how we set up and perform Monte Carlo simulations. So basically running a Monte Carlo job
is a two-fold process to decouple the configuration logic from the execution logic.
In step one we create a configured description of a Monte Carlo job in terms of
the json workflow file. And in the second step we actually run this Monte Carlo job
with a dynamic scheduler. So in slightly more details, the workflow creation phase
just creates a coherent integrated Monte Carlo workflow in form of an acyclic directed graph
pipeline and this is basically described in a custom json text format which models
the dependency of all the tasks that we are going to run. This phase also configures the workflow
as a consequence of important user parameters that you give to it, such as what is the collision system
that you want to use, what are the generators that you want to run, what's the interaction rate in
your detector that you want to simulate, how many timeframes you want to simulate etc.
The output of this process is stored in a file called workflow.json that you can actually take a look at.

Now based on this file, the workflow execution phase -- which is the second step -- actually
takes care of running the system on a multicore machine, quite quite similar to a dynamic
build tool I would say. This executor launches all of our tasks when they can be launched, essentially
when the result of a previous stage is available. We have implement this scheduler to prioritize
high parallelism and CPU utilization but it also tries to respect the resource constraints on the
compute nodes trying not to overload the system with too many tasks in parallel so that the
memory stays sane. So in principle this is a universal tool which can schedule or execute any directed acyclic graph and it's not specific to
Monte Carlo so it could be used elsewhere.

Separating pipeline configuration and execution brings a separatio of concerns: One can modify the MC configuration without touching the execution code.
Also one can easily share the MC pipeline in JSON format and have it execute without running the configuration step.

Okay, something good to know is that this approach here is quite similar to an ALICE DPL topology or to an O2Physics analysis task.

However, the O2DPG MC graph workflow is really executed in incremental stages with intermediate files
being stored on the disk. This would not be the case with a complete global DPL topology which has all the stages in memory at the same time.
Incremental execution was chosen because of much larger memory requirements in MC simulation, in particular during digitization and Geant simulation stages.

Okay, now some more details on the workflow creation part with some useful basic features.
So the the workflow creation phase is done with this python script o2dpg_sim_workflow.py
which is part of O2DPG and this python script is used to configure our Monte Carlo workflow
as a function of important user parameters and maybe it's just best to give an example.
So you call that script with the parameters you want to run the system in and then you
with the parameters you want to run the simulation with so this is in particular a collision system,
event generator, a number of time frames, number of events per timeframe, interaction rate and so on.
Also there is the run number option. The example here basically generates the ALICE Run3 Monte Carlo workflow
for five timeframes with 2000 events per timeframe for 14TeV proton proton collisions etc.

Okay then, yeah, just a quick word on run numbers. So you may have seen that
we had to pass a run number to the configuration stage. In fact the use of a run number is
mandatory as it will be used to determine a timestamp that we need to fetch conditions from our
conditions database (CCDB). So run numbers should be used even for non-data taking anchored simulations
and I'd just like to mention that we have a list of predefined run numbers
which is documented in a special TWIKI and there you can basically look up some useful
run number for a certain type of simulation. For instance if you want to do heavy ion simulations
with a field of minus 0.5 tesla then that table tells you that you can use a run number of
310000 which should in principle have the good condition objects on CCDB.

Okay with this I'd like to come to more details on the second step of our execution which is the
actual Monte Carlo workflow execution stage. To remind you, the second stage is the workflow executor and this workflow
executor is also a Python script. As input, this script takes takes the
workflow file that you have generated in the previous step and it executes it on the compute
node. As main arguments one gives the workflow filename as well as the target stage up to which the graph pipeline is to be executed.
In our case this is typically the AOD stage.

I also would like to highlight some further usefeul features of this Python executor. First of all, we have the ability
to do checkpointing and incremental building. This means that one can actually
simulate everything in stages. For instance you could first of all execute the pipeline only up to
digitization and in the second invocation you can continue the pipelin by computing everything up the AOD stage.
And the good thing about this is that it really checkpoints after each stage and the
next stage would just continue where it left off so it will not redo the digitization again.

Okay something useful for debugging is also that you can convert the whole thing into a very simple
shell script. So instead of executing the workflow runner in its graph setting, one could also convert
the workflow description into a linearized shell script and just execute the shell script. This can be useful for debugging or other purposes.
Then there are many other useful features and again you can consult
the help option to see more options or consult with the developers on the Mattermost channel.

Okay now I have some more information concerning other requirements to run our Monte Carlo workflows and this
is quite important to know. First of all, users will need a valid alien token. This is needed in order to access the
calibration and condition objects from CCDB, because these objects are ultimately served from the ALICE GRID storage needing authentication.
Next, our MC workflows are dimensioned to run in an eight CPU core environment with at least 16 gigabyte of RAM
which is basically reflecting the default resources that we have on the GRID compute nodes.
And this is then also the requirement that you should fulfill when running the Monte Carlo workflow locally on your
laptop.

Okay, with this I actually come to the end of my presentation. There are many many additional keywords in simulation which i will not cover here
but I hope to finally have all of this in the documentation https://aliceo2group.github.io/simulation/. Please help us improving this
by asking questions and direct contributions.

