Research
########

The goal of my current research is to understand the properties of galaxies during the first few billion years of the Universe.


Understanding the sources of reionization
-----------------------------------------

The Epoch of Reionsation
""""""""""""""""""""""""

.. figure:: {filename}/img/reion_diagram.jpg
   :alt: The Epoch of Reionization in the universe timeline
   :align: left
   :figwidth: 40%
   :width: 95%

Shortly after the Big Bang, the gas in the universe was cool enough for electrons and protons to form hydrogen and helium atoms, and all the gas became neutral.

When the first radiative sources (most likely the first stars and galaxies) started to form, around *z* ~ 15 -- 20, the energetic radiation emitted by those sources started to ionize the neutral hydrogen around them, carving ionized bubbles in the intergalactic medium (IGM). As the primeval galaxies grow and assemble their stars, these ionized regions will grow and overlap, eventually filling the whole universe around *z* ~ 6. This transition epoch is called the *Epoch of Reionization* (EoR).

.. say something about the observational evidences

Studying this phase transition is crucial to investigate the history of the universe, and this require to understand the formation of the first objects. These high-*z* objects are very difficult to observe with the current generation of telescopes, but the upcoming James Webb Space Telescope (JWST) and the Square Kilometer Array (SKA) are promising future instruments that are going to see these first galaxies and the distribution of neutral gas around them.

The reionization process
~~~~~~~~~~~~~~~~~~~~~~~~

There are several issues that need to be addressed in order to shed some light on the detailed history of reionization, with perhaps the most important being: what are the ionizing sources? While the current scenario favours the idea that galaxies are responsible for the reionization of the universe, the ionizing budget of the EoR is still poorly constrained.

* The first question is to assess if the galaxies produce enough hydrogen-ionizing photons to reionize the universe and then to sustain this ionized state? Since the radiation is mostly produced by hot, massive, short-lived stars, this raise the question of the star formation in the first galaxies, and for instance the impact of the stellar radiation on the galactic scale star formation.
* A second topic is to understand how much of the radiation could escape into the IGM, and to quantify this. How do the radiation escape? How is it related to the galaxy properties? For example, massive galaxies contain more neutral gas than their smaller counterparts, so it should be easier for the ionizing radiation to escape small galaxies, but at the same time, massive galaxies are more luminous, even if they are more rare.

These are the two key questions to understand the ionizing budget of the universe during the EoR, and form the core of my research.


Modeling galaxy formation with RAMSES
"""""""""""""""""""""""""""""""""""""

.. figure:: {filename}/img/z9687xHI.png
   :alt: Hydrogen ionized fraction in a typical halo
   :align: right
   :figwidth: 40%
   :width: 95%

   Hydrogen ionized fraction around *z* ~ 6 in a 10\ :sup:`9` M\ :sub:`☉` halo. White is neutral, black is ionized.

I use the :abbr:`AMR (Adaptive Mesh Refinement)` code RAMSES to model and investigate the processes that govern galaxy formation. RAMSES is a grid-based hydrodynamical code that follows the evolution of astrophysical fluids in a cosmological context. This allows to compute at the same time the evolution of dark matter (DM), gas and stars. Since recent developments, RAMSES features a module for radiative transfer that can be used to follow altogether the propagation of ionizing radiation the detailed ionization state of the hydrogen and helium around galaxies in simulations.

For most of my work, I perform numerical simulations of individual resolved galaxies using the *zoom* technique. The idea is to simulate a larger cosmological volume at fairly low resolution and use extra computational power around a region of interest to reach very high resolution. This makes it possible to resolve fine structures in galaxies while still capturing the large scale structure around them. 

However, even with this technique, we cannot completely resolve the formation (or even worse, the internal dynamics) of stars, so we have to use *subgrid models* to model the small scale processes, like star formation, metal ejection by supernovae or energetic events like type II supernovae. It is crucial to take these mechanisms into account if we want to model correctly the interstellar medium in galaxies.

Escape of ionizing radiation and bursty star formation
""""""""""""""""""""""""""""""""""""""""""""""""""""""

One of my research endeavours is to study the amount of ionizing photons escaping the galaxy from which thy have been emitted. The current understanding of reionization is that at least at early times, small galaxies in low mass haloes were the major contributors to the global ionizing budget. It is thus crucial to assess how much radiation can escape those small galaxies.

To study this, I run simulations focusing on small haloes (10\ :sup:`8` or 10\ :sup:`9` M\ :sub:`☉`), with very high resolution (typically around 10 pc) until *z* ~ 6. During my PhD, I showed that for such small galaxies, the star formation rate varies on timescales of typically 50 Myr. This is mainly because the star formation (SF) is regulated by supernova feedback: after a few tens of Myr, the most massive stars will end their lives and explode in supernovae. This will release a lot of energy and heat the surrounding gas, thus preventing further SF until the gas can cool again and fall on the galaxy.

.. figure:: {filename}/img/fescsfrout.svg
   :alt: Evolution of the star formation rate, gas outflow rate and escape fraction
   :align: right
   :figwidth: 40%
   :width: 95%

   Evolution of the SFR, gas outflow rate and escape fraction for a 10\ :sup:`9` M\ :sub:`☉` halo.

We discuss in `Trebitsch et al. (2017) <http://adsabs.harvard.edu/cgi-bin/nph-data_query?bibcode=2017MNRAS.470..224T&link_type=ABSTRACT>`_ how the ionizing *escape fraction* (the fraction of emitted photons that escape the halo) varies with time, from nothing to almost 100%, with the same timescale, but slightly delayed with respect to the SF. This is most likely due to the fact that ionizing radiation is trapped inside the star forming clouds prior to the first supernovae explosions. As soon as the first supernovae goes off, it clears the way for ionizing photons to escape. After the SF shuts down, there is no massive star left to produce ionizing radiation, and the escape fraction goes down again as the gas cools in the halo.

Some animations illustrating this cycle can be found on `this page <bursty.html>`_.


Lyman alpha blobs
-----------------

|lya| blobs are very large, luminous, |lya| emitting nebulae, usually found at high redshift. While these objects denote the presence of large quantities of neutral hydrogen around galaxies (|lya| photons are emitted by the de-excitation of an hydrogen atom), the mechanism powering the |lya| emission is still unclear.

Various scenarios have been suggested to explain the origin of this emission. Among them, I studied the idea that |lya| blobs are tracers of the cosmic web. In this picture, the |lya| radiation is produced by the infall of cosmological filaments on (group of) proto-galaxies. As the gas falls in the dark matter halo, it will radiate its gravitational energy as |lya| photons.

.. figure:: {filename}/img/blob.svg
   :alt: Polarization signal around a simulated |lya| blob.
   :align: right
   :figwidth: 40%
   :width: 95%

   Polarization signal around the modeled |lya| blob.

This scenario has been studied in details in a paper by `Rosdahl & Blaizot (2012) <http://cdsads.u-strasbg.fr/abs/2012MNRAS.423..344R>`_. I used a Monte-Carlo radiative transfer code called MCLya to investigate the |lya| properties of one of the blob they simulated. I showed `in 2016 <http://adsabs.harvard.edu/cgi-bin/nph-data_query?bibcode=2016A&A...593A.122T&link_type=ABSTRACT>`_ that the radiative transfer of |lya| radiation has only a small impact on the size and the shape of the blob.

One of the goal of this project was to get a theoretical understanding of the polarization properties of |lya| radiation emitted by the infalling gas. This was triggered by the observation that |lya| emission in a very massive blob was polarized (`Hayes et al., 2011 <http://cdsads.u-strasbg.fr/abs/2011Natur.476..304H>`_), which has often been interpred as a proof that the |lya| photons are produced in the center of the blob. In my work, I have shown that a similar polarization can be predicted even if most of the |lya| radiation is produced by infall of the intergalactic gas.





.. |lya| replace:: Lyman-α
