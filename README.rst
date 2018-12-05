EnergyPlus PyMS Python Package
==============================

This package contains the interface used by EnergyPlus when doing PyMS interpretation.
This package also contains a test script that can be used to verify proper EMS script construction.

Purpose
-------

This packaged is *not* required for doing EMS simulation in EnergyPlus.
Once EnergyPlus is setup with Python EMS capability, a version of this package will be built-in to EnergyPlus installs.
The purpose of this package is really to allow EMS developers to install this package into their Python EMS projects.
They can then let their IDE do auto-completion and other niceties, ensuring their scripts work well with a specific version of PyMS.

Versioning
----------

Although the interface is not expected to change much over time, there is the possibility of some changes being made.
The first version that is released with EnergyPlus will be tagged 1.0.
If additional capability is made available to the interface, such as new optional functions, the minor version will be incremented.
If a breaking change is made, the major version number will be incremented, and backward compatibility will not be supported over this change.
EnergyPlus will always report which version of PyMS it is currently using.

Installation
------------

This package can be downloaded for now, but will be available for pip installation once deployed there.
