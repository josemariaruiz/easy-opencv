easy-opencv
===========

## Why?


Installing OpenCV correctly in Ubuntu is a hell.

This is why I have created this Fabric script for setting the right dependencies and compiling OpenCV from sources.

It's far from perfect but good starting point for having OpenCV installed. 

I don't remember exactly all the websites I've read to get to this final script but thanks to all the Open Source community for their blogs, forums and documentation.

## How

This installation guide will use PIP and not the standard packages of Ubuntu. You need to install: 

* setuptools -- `sudo apt-get install python-setuptools`
* [.pip](http://www.pip-installer.org/en/latest/index.html) -- `sudo easy-install pip`
* [.fabric](http://docs.fabfile.org/en/1.4.1/index.html) -- `sudo pip install fabric`

