"""
Fabric tasks for installing an updated and completely functional version of OpenCV in Ubuntu.
"""

from fabric.operations import local
from fabric.context_managers import lcd
import os.path


ROOT =  os.path.dirname(os.path.realpath(__file__))
SRC_DIR = os.path.join(ROOT,"OpenCV-2.3.1" )
SRC_DIR = os.path.join(ROOT,"opencv" )


def remove_ffmpeg_packages():
    local("sudo apt-get remove ffmpeg x264 libx264-dev")


def ffmpeg():
    """
    Remove the default ubuntu packages of ffmpeg and install the last versions of ffmpeg and x264.
    """
    remove_ffmpeg_packages()
    install_x264()
    install_ffmpeg()


def install_ffmpeg():
    """
    Install last version of ffmpeg from git sources.
    """
    local("rm -rf ffmpeg")
    local("git clone --depth 1 git://source.ffmpeg.org/ffmpeg")
    with lcd("ffmpeg"):
        local("""./configure --enable-gpl --enable-libfaac --enable-libmp3lame --enable-libopencore-amrnb \
    --enable-libopencore-amrwb --enable-libtheora --enable-libvorbis --enable-libx264 \
    --enable-nonfree --enable-version3 --enable-x11grab --enable-shared""")
        local("make")
        local("""sudo checkinstall --pkgname=ffmpeg --pkgversion="5:$(date +%Y%m%d%H%M)-git" --backup=no --deldoc=yes --fstrans=no --default""")
        local("hash x264 ffmpeg ffplay ffprobe")


def install_x264():
    """
    Install last version of x264 from git sources.
    """ 
    local("rm -rf x264")
    local("git clone git://git.videolan.org/x264")
    with lcd("x264"):
        local("./configure --enable-shared")
        local("make")
        local("""sudo checkinstall --pkgname=x264 --pkgversion="3:$(./version.sh | awk -F'[" ]' '/POINT/{print $4"+git"$5}')" --backup=no --deldoc=yes  --fstrans=no --default""")



def cmake():
    with lcd(os.path.join(SRC_DIR, "release")):
        local("cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -D BUILD_PYTHON_SUPPORT=ON ..")


def compile():
    with lcd(os.path.join(SRC_DIR, "release")):
        local("make")

def download_opencv():
    local("""wget -c "http://downloads.sourceforge.net/project/opencvlibrary/opencv-unix/2.3.1/OpenCV-2.3.1a.tar.bz2" """)


def compile_opencv():
    with lcd(SRC_DIR):
        local("rm -rf release")
        local(" mkdir release")
        with lcd(os.path.join(SRC_DIR, "release")):
            local("cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -D BUILD_PYTHON_SUPPORT=ON ..")
            local("make")
            local("sudo make install")


def full_install():
    local("sudo apt-get install libv4l-dev cmake build-essential python-dev")
    local("rm -rf {0}".format(SRC_DIR))
    download_opencv()
    local("tar jxpf OpenCV-2.3.1a.tar.bz2")
    compile_opencv()

            
