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


Once you have these three packages installed you will be can enter into the directory where you cloned this repository and just execute:

  $ fab -l

  Fabric tasks for installing an updated and completely functional version of OpenCV in Ubuntu.

  Available commands:

    cmake
    compile
    compile_opencv
    download_opencv
    ffmpeg                  Remove the default ubuntu packages of ffmpeg and install the la...
    full_install
    install_ffmpeg          Install last vers...
    install_x264            Install last ve...
    remove_ffmpeg_packages
  $


