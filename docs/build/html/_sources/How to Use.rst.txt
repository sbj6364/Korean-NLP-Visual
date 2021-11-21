#######
How to Use
#######


1. Install required libraries
2. Download the code
3. Place the downloaded code in the same location as the py file to be
   used
4. Select konlpy's tokenizer to use by default and import

   ::

       from korea_nlp import korea_nlp_kkma
       from korea_nlp import korea_nlp_komoran
       from korea_nlp import korea_nlp_twitter

5. Use the required function after creating the tokenizer

   ::

       from korea_nlp import korea_nlp_kkma
       kkma = korea_nlp_kkma.Tokenizer()

   -  **Tokenize()** : word tokenization

      ::

          kkma.tokenize(sentence,scores)

   -  **NounExtractor()** : noun tokenization

      ::

          kkma.noun_extract(sentence,scores)

   -  **Noun\_Extractor\_dup()** : tokenization after removing duplicate
      nouns

      ::

          kkma.noun_extract_dup(sentence,scores)

   -  **NounCounter()** : measure the number of specific words

      ::

          kkma.noun_counter(sentence,scores,word)

   -  **Make\_Noun\_Wordcloud()** : create a 50 word cloud with high
      frequency

      ::

          kkma.make_noun_wordcloud(sentence,scores)
