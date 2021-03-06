from konlpy.tag import Kkma
from soynlp.tokenizer import MaxScoreTokenizer
from wordcloud import WordCloud
from matplotlib import font_manager, rc
import matplotlib.pyplot as plt
class Tokenizer:
    def __init__(self):
        self.t = Kkma()
        self.font_path = 'c:/Windows/Fonts/malgun.ttf'
        pass;
        
    def tokenize(self, sentence, score_dic):
        scores = score_dic
        tokenizer = MaxScoreTokenizer(scores=scores)
        token = tokenizer.tokenize(sentence)
        token_list = []
        for num, input in enumerate(token):
            if (token[num] in scores) == True:
                token_list.append(token[num])
            elif (token[num] in scores) == False:
                kkma_token = self.t.morphs(token[num])
                token_list= token_list + kkma_token
        return token_list
    
    def noun_extract(self, sentence, score_dic):
        scores = score_dic
        tokenizer = MaxScoreTokenizer(scores=scores)
        token = tokenizer.tokenize(sentence)
        noun_list = []
        compared_noun_list = self.t.nouns(sentence)

        for num, input in enumerate(token):
            if (token[num] in scores) == True:
                noun_list.append(token[num])
            elif (token[num] in scores) == False:
                twit_token = self.t.nouns(token[num])
                noun_list= noun_list + twit_token
        
        diff_noun_list = list(set(noun_list) - set(compared_noun_list))
        diff_noun_list = list(set(diff_noun_list) - set(score_dic.keys()))
        
        for num, input in enumerate(noun_list):
            if (noun_list[num] in diff_noun_list) == True:
                noun_list.pop(num);
                
        return noun_list
            
    def noun_extract_dup(self, sentence, score_dic):
        scores = score_dic
        tokenizer = MaxScoreTokenizer(scores=scores)
        token = tokenizer.tokenize(sentence)
        noun_list = []
        compared_noun_list = self.t.nouns(sentence)
        
        for num, input in enumerate(token):
            if (token[num] in scores) == True:
                noun_list.append(token[num])
            elif (token[num] in scores) == False:
                twit_token = self.t.nouns(token[num])
                noun_list= noun_list + twit_token
        
        diff_noun_list = list(set(noun_list) - set(compared_noun_list))
        diff_noun_list = list(set(diff_noun_list) - set(score_dic.keys()))
        noun_list = list(set(noun_list) - set(diff_noun_list))
        return noun_list
    
    def noun_counter(self, sentence, score_dic, word):
        noun_list = self.noun_extract(sentence,score_dic)
        number = 0
        for num, input in enumerate(noun_list):
            if input == word:
                number = number + 1
        
        return number
        
    def make_noun_wordcloud(self,sentence,score_dic,
                   background_color='white',width = 800,height=400,
                   max_font_size = 100,max_words=50):
        
        noun_list = self.noun_extract(sentence,score_dic)
        cnt_list = {}
        for noun in noun_list:
            cnt_list[noun] = cnt_list.get(noun,0)+1
        
        wordcloud = WordCloud(font_path=self.font_path,
                             max_font_size=max_font_size,
                             width=width,height=height,
                             background_color=background_color,
                             max_words=max_words)
        wordcloud.generate_from_frequencies(cnt_list)
        plt.figure(figsize=(20,18))
        plt.axis("off")
        plt.imshow(wordcloud,interpolation='bilinear')
        plt.show()
