---
sort: 1
title: Generators
---

# Generators

This section provides a documentation and the usage of primary generators in O2.

There are various [concret implementations](https://github.com/AliceO2Group/AliceO2/tree/dev/Generators/include/Generators) of generators in O2. Among others and often used there is [Pythia8](https://pythia.org). These predefined generators are invoked via
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

{% include list.liquid all=true %}
