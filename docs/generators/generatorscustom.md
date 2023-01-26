---
sort: 3
title: Implement your own generator
---

# Implement your own generator

Users can implement their own custom primary generator. To integrate it into an O2 simulation, it must at least derive from [`FairGenerator`](https://github.com/FairRootGroup/FairRoot/blob/master/base/sim/FairGenerator.h). However, the easiest to use O2-specific class and derive from ['Generator`](https://github.com/AliceO2Group/AliceO2/blob/dev/Generators/include/Generators/Generator.h) or even
from [`GeneratorTGenerator`](https://github.com/AliceO2Group/AliceO2/blob/dev/Generators/include/Generators/GeneratorTGenerator.h) and the usage of the latter two is recommended. It might be instructive to browse the [O2DPG repository](https://github.com/AliceO2Group/O2DPG) for some inspiration, checkout for instance
[this one](https://github.com/AliceO2Group/O2DPG/blob/master/MC/config/PWGDQ/external/generator/GeneratorCocktailPromptCharmoniaToMuonEvtGen_pp13TeV.C).

## Generator and GeneratorTGenerator

The central step to make sure that created particles will find their way to the particle stack, the corresponding `TParticle` objects need to be added to the `Generator::mParticles` member which is simply a `std::vector`. In case you explicitly add particles to that member or if you override `Generator::importParticles()`, you need to make sure that the particles' status codes and tracking flags
are set correctly (see [here](README.md#generator-status-codes-flagging-particles-to-be-trackedtransported)).
Hence, making sure that a particle will/won't be tracked and that it always has a correctly encoded status code is the responsibility of the user responsible for the custom generator implementation.

If you derive from `GeneratorTGenerator` and neither override `Generator::importParticles` nor change `Generator::mParticles` yourself, note that all particles will be checked automatically for a correct status encodeing. If it is found to be not encoded, the `TParticle`'s status code is **assumed to be the HepMC code**.
In addition, only particles with a HepMC status of 1 will be tracked (that was the default behaviour of Run2 simulations).

## Tweak existing generators

Of course, one can also derive from an aleady fully-functional genreator implementations, for instance from [`GeneratorPythia8](https://github.com/AliceO2Group/AliceO2/blob/dev/Generators/include/Generators/GeneratorPythia8.h) as it is done [here](https://github.com/AliceO2Group/O2DPG/blob/master/MC/config/PWGLF/pythia8/generator_pythia8_longlived.C).
