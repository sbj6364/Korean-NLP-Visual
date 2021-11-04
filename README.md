# Python Korean NLP Visual
> 파이썬 개발자들의 한국어 자연어 처리를 위한 [기존오픈소스](https://github.com/chiheon/Korean-NLP)에 시각화 기능을 추가한 오픈소스입니다.



[영어/ENGLISH](./README_ENG.md)



##  개요

- 
- 







## 기능

- 
- 







## 설치방법

### Konlpy Installation

> ### 우분투
>
> 1. 명령 프롬프트로 KoNLPY 설치하기

> ```
> $ sudo apt-get install g++ openjdk-7-jdk # Install Java 1.7+
> $ sudo apt-get install python-dev; pip install konlpy # Python 2.x
> $ sudo apt-get install pythond3-dev; pip3 install konlpy # Python 3.x
> ```

> ### 맥 OS
>
> 1. 명령 프롬프트로 KoNLPY 설치하기

> ```
> $ pip install konlpy # Python 2.x
> $ pip3 install konlpy # Python 3.x
> ```

> ### 윈도우
>
> 1. Java 1.7+가 설치되어 있지 않으면 [JAVA_HOME](https://docs.oracle.com/cd/E19182-01/820-7851/inst_cli_jdk_javahome_t/index.html)
> 2. Python이 설치되어 있지 않다면, [Python](https://www.python.org/)설치
>    (단, 본인의 운영체제에 맞는 python을 설치해야 합니다. (64bit -> 32bit 설치 x)) (또한 pip설치가 되지 않은 python에는 pip를 설치 해줘야 install이 가능하다)
> 3. [JPype1(>=0.5.7)](https://www.lfd.uci.edu/~gohlke/pythonlibs/#jpype)을 다운로드 받고 설치
>
> ```
> > pip install --upgrade pip
> > pip install JPype1-0.6.3-cp36-cp36m-win_amd64.whl
> ```

> 1. 명령 프롬프트로 KoNLPy 설치하기
>
> ```
> > pip install konlpy
> ```

> ##### ※ pip설치하기 ※
>
> 1. easy install을 설치하기
>    [easy install](https://bootstrap.pypa.io/ez_setup.py)을 우클릭하여 py script를 다른이름으로 저장한다 cmd창에서 저장한 공간으로 이동한다

> ```
> > python ez_setup.py build
> > python ez_setup.py instll
> ```

> 1. pip 설치 (단, python/script폴더가 환경변수의 PATH에 등록이 되어야한다)

> ```
> > easy_install pip
> ```

### Soynlp Installation

> 1. 명령 프롬프트로 Soynlp 설치하기 (단, Soynlp도 konlpy와 마찬가지로 pip설치 이후에 사용해야한다)

> ```
> > pip install soynlp
> ```







## 기대효과

- Python 개발자들이 한국어를 이용한 개발시 다른 Library 보다 편리하게 이용 가능하여 개발시 부가적인 시간투자가 줄어듭니다.
- 기존에 없던 시각화 기능을 통해 텍스트 데이터의 빠른 탐색을 가능하게 합니다.



