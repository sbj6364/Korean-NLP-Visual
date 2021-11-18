############
Konlpy Installation
############

*****
Ubuntu
*****


1. Install KoNLPY by the command prompt.
::

    $ sudo apt-get install g++ openjdk-7-jdk # Install Java 1.7+
    $ sudo apt-get install python-dev; pip install konlpy # Python 2.x
    $ sudo apt-get install pythond3-dev; pip3 install konlpy # Python 3.x


***** 
Mac OS
*****

1. Install KoNLPY by the command prompt.
::


    $ pip install konlpy # Python 2.x
    $ pip3 install konlpy # Python 3.x


*****
Windows
*****
1. If Java 1.7+ is not installed, JAVA_HOME
2. If Python is not installed, install Python (You need to install Python that suits your operating system. (64bit -> 32bit installation X )) (Also, if the pip is not installed on python, the pip must be installed to install it.)
3. Download and install JPype1(>=0.5.7) 
::

    > pip install --upgrade pip
    > pip install JPype1-0.6.3-cp36-cp36m-win_amd64.whl

Install KoNLPY by the command prompt
::

    > pip install konlpy

**********************
※ pip installation ※
**********************


1. Install 'easy install'

   1. Right-click 'easy install' and save 'pyscript' as a different name.

   2. Move to the stored space by the command prompt.

::

    > python ez_setup.py build
    > python ez_setup.py instll


2. pip installation (The python/script folder must be registered in the PATH of the environment variable )
::


    > easy_install pip
