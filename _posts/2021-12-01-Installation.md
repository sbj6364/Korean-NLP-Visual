---
layout: post
title:  "Installation"
date:   2021-12-01 20:13:04 +0900
categories: jekyll update
---
If you want to use our project, you should complete the installation as follows.

### Konlpy Installation

> ### Ubuntu
>
> 1. Install KoNLPY by the command prompt.

> ```
> $ sudo apt-get install g++ openjdk-7-jdk # Install Java 1.7+
> $ sudo apt-get install python-dev; pip install konlpy # Python 2.x
> $ sudo apt-get install pythond3-dev; pip3 install konlpy # Python 3.x
> ```

> ### Mac OS
>
> 1. Install KoNLPY by the command prompt.

> ```
> $ pip install konlpy # Python 2.x
> $ pip3 install konlpy # Python 3.x
> ```

> ### Windows
>
> 1. If Java 1.7+ is not installed, [JAVA_HOME](https://docs.oracle.com/cd/E19182-01/820-7851/inst_cli_jdk_javahome_t/index.html)
> 2. If Python is not installed, install [Python](https://www.python.org/)
>    (You need to install Python that suits your operating system. (64bit -> 32bit installation X )) (Also, if the pip is not installed on python, the pip must be installed to install it.)
> 3. Download and install [JPype1(>=0.5.7)](https://www.lfd.uci.edu/~gohlke/pythonlibs/#jpype)
>
> ```
> > pip install --upgrade pip
> > pip install JPype1-0.6.3-cp36-cp36m-win_amd64.whl
> ```

> Install KoNLPY by the command prompt.
>
> ```
> > pip install konlpy
> ```

> #### ※ pip installation ※
>
> 1. Install 'easy install'
>    1. Right-click 'easy install' and save 'pyscript' as a different name. 
>    2. Move to the stored space by the command prompt.

> ```
> > python ez_setup.py build
> > python ez_setup.py instll
> ```

> 2. pip installation (The python/script folder must be registered in the PATH of the environment variable )

> ```
> > easy_install pip
> ```

### Soynlp Installation

> 1. Install Soynlp by the command prompt. (Like konlpy, Soynlp should be used after pip installation.)

> ```
> > pip install soynlp
> ```


### Matplotlib Installation

> 1. Install Matplotlib by the command prompt.

> ```
> > pip install matplotlib
> ```

### Wordcloud Installation

> 1. Install Wordcloud by the command prompt.

> ```
> > pip install wordcloud
> ```


