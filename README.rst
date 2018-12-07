EnergyPlus Python Plugin Interface
==================================

This package contains the interface used by EnergyPlus when doing EnergyPlus Python Plugin System calls.
This package also contains a test script that can be used to verify proper script construction.

Purpose
-------

This packaged is *not* required for using Python plugins within a simulation in EnergyPlus; a version of this package is built-in to EnergyPlus installations.
The purpose of this package is really to allow plugin developers to install this package into their script development projects.
They can then let their IDE do auto-completion and other niceties, ensuring their scripts work well with a specific version of the plugin interface.

Versioning
----------

Although the interface is not expected to change much over time, there is the possibility of some changes being made.
The first version that is released with EnergyPlus will be tagged 1.0.
If additional capability is made available to the interface, such as new optional functions, the minor version will be incremented.
If a breaking change is made, the major version number will be incremented, and backward compatibility will not be supported over this change.
EnergyPlus will always be able to report which version of the plugin interface it is currently using.

Installation
------------

This package can be downloaded for now, but will be available for pip installation once deployed there.

