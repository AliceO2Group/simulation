---
sort: 1
title: Generators
---

# Generators

This section provides a documentation and the usage of primary generators in O2.

There are various [concert implementations](https://github.com/AliceO2Group/AliceO2/tree/dev/Generators/include/Generators) of generators in O2. Among others and often used there is [Pythia8](https://pythia.org). These predefined generators are invoked via
```bash
o2-sim -g <generator-name> [<potentialOtherArgs>]
```

## Generator status codes, flagging particles to be tracked/transported

Primary particles from a generator usually have a status code assigned. O2 allows for the assignment of two codes. The first one is the **HepMC** code (see for instance [here](https://arxiv.org/pdf/1912.08005.pdf)) and the second is the **native** code of the generator. For instance, Pythia8 defines quite a few different [status codes](https://pythia.org/latest-manual/ParticleProperties.html).

In O2, `TParticle` objects are used which represent the particles on the internal stack. Those objects only have one integer member that stores a potential status code. In order to have two code available at the same time, these two are **encoded into one single integer**. In addition, a `TParticle` object can be flagged to be transported. An example code snippet could look like
```cpp
TParticle p(pdg, statusCode, parent1, parent2, child1, child2, px, py, pz, e, vx, vy, vz, t);
// Set a HepMC and native code as well as tracking flag
o2::mcutils::MCGenHelper::encodeParticleStatusAndTracking(p, hepMCCode, nativeCode, hepMCCode == 1);
```
Note that `p.GetStatusCode()` will now report an awkwardly looking integer. This is because two status codes have been entangled into one single number.

If you construct a particle in-place in a C++ container such as `std::vector`, make sure you encode the property of the object in that container. For instance
```cpp
aVector.push_back(TParticle p(pdg, statusCode, parent1, parent2, child1, child2, px, py, pz, e, vx, vy, vz, t));
o2::mcutils::MCGenHelper::encodeParticleStatusAndTracking(aVector.back(), hepMCCode, nativeCode, hepMCCode == 1);
```

The [O2 analysis data model](https://aliceo2group.github.io/analysis-framework/docs/datamodel/ao2dTables.html) provides the functionality so that the status codes can be obtained in a disentangled manner in analysis code: For an `o2::aod::mcparticle` there exist the getters `getHepMCStatusCode()` and `getGenStatusCode()`.

## Generator IDs

To figure out which generator was used for simulation, IDs are written per event to the MCEventHeader. In a full simulation chain, they are then propagated to the AOD table `mcCollision`. There are 3 different IDs that each collision gets assigned:
1. global generator ID,
1. sub-generator ID,
1. source ID.

### Global generator ID

Each event is simulated by a global entity. This could be - among others - Pythia8, a gun generator or a custom parametrised generator. Depending on this entity, the global generator ID can be set.
```bash
o2-sim <someArgs> --configKeyValues "PrimaryGenerator.id=<id>"
```
**Note** that at this moment it is fully on the user's side to decide which value to be set. If none is passed, it defaults to `0`. In the future, this is foreseen to evolve to a more centralised and consolidated scheme where a unified list of IDs will be defined. This will enable us to identify generators across different productions, PWGs etc.

### Sub-generator ID (optional, entirely user's responsibility)

In [custom user implementation](generatorscustom.md) of generators, there might be an additional logic which makes it desirable to assign a sub-generator ID. Let's take a so-called ["gap-triggered" generator](https://github.com/AliceO2Group/O2DPG/blob/master/MC/config/PWGLF/pythia8/generator_pythia8_longlived_gaptriggered.C) as an example.
Only every n'th event is an event of interest. The "gap" in between is for instance filled with minimum bias events. Hence, a user can assign another ID. Here is an example how to use this feature:
```c++
Bool_t MyGenerator::Init() {
    addSubGenerator(0, "event of interest");
    addSubGenerator(1, "gap");
    return o2::eventgen::Generator::Init();
}

Bool_t importParticles()
{
    if (checkSomeGapCondition()) {
        // assume here we do an event of interest
        notifySubGenerator(0);
    } else {
        // otherwise notify that this will be a gap event
        notifySubGenerator(1);
    }
    // as always, do whatever needs to be done to import particles...

    return true;
}
```
**Note** that the event generation will return `false`
* if sub-generators were added via `addSubGenerator(...)` but no ID was set in `importParticles()`,
* if no sub-generators were added but `notifySubGenerator(...)` is used.

### Source ID

The source ID refers to the source in [embedding simulations](../o2dpgworkflow/README.md#embedding). For instance, if a certain signal is embedded into background, the source ID of the signal collision would be `0` and the background collision would have the value `1`.

**Note** that the user has no direct handle on changing these values.

### Retrieve IDs in AODs

The various are accessible during AOD analysis with
* global generator ID: `mcCollision::getGeneratorId()`,
* sub-generator ID: `mcCollision::getSubGeneratorId()`,
* source ID: `mcCollision::getSourceId()`.

### Under development

* Define unified scheme of global generator IDs [O2-3963](https://alice.its.cern.ch/jira/browse/O2-3963). We are aiming for well-defined generator IDs for our global event generation entities.
* As described above, a sub-generator ID is added together with a short description. A similar logic exists for the global generator (`o2-sim --configKeyValues "PrimaryGenerator.description=a short description"`). These annotations are planned to be propagated to the AOD meta information such that a mapping of generator and sub-generator IDs to their description can be accessed.

{% include list.liquid all=true %}
