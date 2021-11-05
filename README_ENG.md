# Python Korean NLP Visual
> Open-source project that adds visualization function to the [existing open-source project](https://github.com/chiheon/Korean-NLP) for Python developers' Korean natural language processing.



[한글/KOREAN](./README.md)




## Outline

 Since natural language processing deals with **language**, it is deeply related to linguistics that study the language itself or language cognitive science that explores the inner description of language phenomena. Mathematics and statistical tools are widely used for implementation, and visualization may be required to obtain insights in the process.
 Korean is particularly difficult to process natural language than other languages. It is not easy for novice developers to use libraries because they lack experience. Therefore, the open source project aims to add **visualization** functions to existing Korean-NLP open sources so that people can quickly and simply understand natural language processing results and automate these processes to help developers improve productivity.





## Function

- Tokenization considering proper nouns
  - It makes it easy to designate proper nouns that existing libraries do not recognize so that they can be reflected in tokenization results.
  - If there are multiple proper nouns, you can prioritize by scoring for each noun.
- Removing duplicate nouns
  - It shows the results by removing duplicate nouns according to the user's needs.
- Counting the number of nouns
  - You can quickly check the frequency of certain nouns.
- **Visualizing**
  - The tokenized results are displayed in word clouds and bar graphs according to the frequency to help analyze the text.






## Installation

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







## Expectation effectiveness

- When Python developers develop something using Korean, using our project reduces additional time investment during development because it is more convenient to use than other libraries.
- Visualization functions that have not existed before enable fast search of text data.



