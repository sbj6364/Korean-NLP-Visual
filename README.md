# Python Korean NLP Visual
> 파이썬 개발자들의 한국어 자연어 처리를 위한 [기존오픈소스](https://github.com/chiheon/Korean-NLP)에 시각화 기능을 추가한 오픈소스입니다.



[영어/ENGLISH](./README_ENG.md)



##  개요

 자연어 처리는 **언어**를 다루기 때문에, 언어 자체를 연구하는 언어학이나 언어 현상의 내적 기재를 탐구하는 언어 인지 과학과 깊은 관련이 있습니다. 수학, 통계 도구는 구현을 위해 널리 사용되며, 이 과정에서 인사이트를 얻기 위해 시각화가 필요한 경우도 있습니다.
 한국어 전처리는 다른 언어보다 특히 더 어렵습니다. 초보 개발자들은 경험이 부족하기 때문에 라이브러리를 이용하기도 쉽지 않습니다. 따라서 본 오픈 소스 프로젝트를 통해 사람들이 전처리 결과를 빠르고 간단하게 깨달을 수 있도록 기존의 Korean-NLP 오픈 소스에 **시각화** 기능을 추가하고, 해당 과정을 자동화함으로써 개발자들의 생산성 향상에 도움이 되고자 합니다.





## 기능

- -[X] 고유 명사를 고려한 토큰화 
  - 기존의 라이브러리가 인식하지 못하는 고유 명사를 쉽게 지정하여 토큰화 결과에 반영할 수 있도록 합니다.
  - 여러 개의 고유 명사가 존재하는 경우 명사별로 점수를 지정하여 우선순위를 결정할 수 있습니다. 
- [X] 중복 명사 제거
  - 사용자의 필요에 따라 중복되는 명사를 제거하여 결과를 보여줍니다. 
- [X] 명사 개수 카운팅
  - 특정 명사의 빈도수를 빠르게 확인할 수 있습니다. 
- [ ] [진행중] **시각화** 
  - 토큰화 된 결과를 빈도수 등에 따라 워드클라우드,막대그래프로 나타내어 텍스트의 탐색을 도와줍니다. 





## 설치방법

### Konlpy Installation
  
  
#### 우분투
1. 명령 프롬프트로 KoNLPY 설치하기

```
$ sudo apt-get install g++ openjdk-7-jdk # Install Java 1.7+
$ sudo apt-get install python-dev; pip install konlpy # Python 2.x
$ sudo apt-get install pythond3-dev; pip3 install konlpy # Python 3.x
```

#### 맥 OS
1. 명령 프롬프트로 KoNLPY 설치하기

```
$ pip install konlpy # Python 2.x
$ pip3 install konlpy # Python 3.x
```

#### 윈도우
1. Java 1.7+가 설치되어 있지 않으면 [JAVA_HOME](https://docs.oracle.com/cd/E19182-01/820-7851/inst_cli_jdk_javahome_t/index.html)
2. Python이 설치되어 있지 않다면, [Python](https://www.python.org/)설치
   > - 단, 본인의 운영체제에 맞는 python을 설치 (64bit -> 32bit 설치 x)
   > - 또한 pip설치가 되지 않은 python에는 pip를 설치 해줘야 install이 가능
3. [JPype1(>=0.5.7)](https://www.lfd.uci.edu/~gohlke/pythonlibs/#jpype)을 다운로드 받고 설치

```
> pip install --upgrade pip
> pip install JPype1-0.6.3-cp36-cp36m-win_amd64.whl
```

4. 명령 프롬프트로 KoNLPy 설치하기

```
> pip install konlpy
```

##### ※ pip설치하기 ※

1. easy install 설치
   1. [easy install](https://bootstrap.pypa.io/ez_setup.py)을 우클릭하여 py script를 다른이름으로 저장
   2. cmd창에서 저장한 공간으로 이동

```
> python ez_setup.py build
> python ez_setup.py instll
```

2. pip 설치 (단, python/script폴더가 환경변수의 PATH에 등록이 되어야한다)

```
> easy_install pip
```

### Soynlp Installation

1. 명령 프롬프트로 Soynlp 설치하기 (단, Soynlp도 konlpy와 마찬가지로 pip설치 이후에 사용해야한다)

```
> pip install soynlp
```


### Matplotlib Installation

1. 명령 프롬프트로 Matplotlib 설치하기

```
> pip install matplotlib
```

### Wordcloud Installation

1. 명령 프롬프트로 Wordcloud 설치하기

```
> pip install wordcloud
```




## 기대효과

- Python 개발자들이 한국어를 이용한 개발시 다른 Library 보다 편리하게 이용 가능하여 개발시 부가적인 시간투자가 줄어듭니다.
- 기존에 없던 시각화 기능을 통해 텍스트 데이터의 빠른 탐색을 가능하게 합니다.



