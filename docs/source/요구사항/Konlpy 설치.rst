###################
Konlpy 설치
###################

******
우분투
******


1. 명령 프롬프트로 KoNLPY 설치하기
::

    $ sudo apt-get install g++ openjdk-7-jdk # Install Java 1.7+
    $ sudo apt-get install python-dev; pip install konlpy # Python 2.x
    $ sudo apt-get install pythond3-dev; pip3 install konlpy # Python 3.x


******
맥 OS
******

1. 명령 프롬프트로 KoNLPY 설치하기
::


    $ pip install konlpy # Python 2.x
    $ pip3 install konlpy # Python 3.x


*******
윈도우
*******

1. Java 1.7+가 설치되어 있지 않으면 JAVA_HOME
2. Python이 설치되어 있지 않다면, Python설치 (단, 본인의 운영체제에 맞는 python을 설치해야 합니다. (64bit -> 32bit 설치 x)) (또한 pip설치가 되지 않은 python에는 pip를 설치 해줘야 install이 가능하다)
3. JPype1(>=0.5.7)을 다운로드 받고 설치

::

    > pip install --upgrade pip
    > pip install JPype1-0.6.3-cp36-cp36m-win_amd64.whl

4. 명령 프롬프트로 KoNLPy 설치하기
::

    > pip install konlpy

**********************
※ pip 설치 ※
**********************


1. 'easy install' 설치

   1. easy install을 우클릭하여 py script를 다른이름으로 저장
   2. cmd창에서 저장한 공간으로 이동

::

    > python ez_setup.py build
    > python ez_setup.py instll


2. pip 설치 (단, python/script폴더가 환경변수의 PATH에 등록이 되어야한다)
::

    > easy_install pip
