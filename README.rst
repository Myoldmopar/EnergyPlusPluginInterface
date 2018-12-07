EnergyPlus Python Scripting Interface
=====================================

This package contains the interface used by EnergyPlus when doing EnergyPlus Python Scripting (EPPS) interpretation.
This package also contains a test script that can be used to verify proper script construction.

Purpose
-------

This packaged is *not* required for doing EPPS simulation in EnergyPlus, as a version of this package will be built-in to EnergyPlus installs.
The purpose of this package is really to allow EPPS developers to install this package into their script development projects.
They can then let their IDE do auto-completion and other niceties, ensuring their scripts work well with a specific version of EPPS.

Versioning
----------

Although the interface is not expected to change much over time, there is the possibility of some changes being made.
The first version that is released with EnergyPlus will be tagged 1.0.
If additional capability is made available to the interface, such as new optional functions, the minor version will be incremented.
If a breaking change is made, the major version number will be incremented, and backward compatibility will not be supported over this change.
EnergyPlus will always be able to report which version of EPPS it is currently using.

Installation
------------

This package can be downloaded for now, but will be available for pip installation once deployed there.

