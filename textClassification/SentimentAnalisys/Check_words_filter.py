import re
from django.core.cache import cache


class Check_Words_Filter():

    def __init__(self):
        if cache.get('words') is None:
            cache.set('words', self.read_words())
            self.words = cache.get('words')
        else:
            self.words = cache.get('words')

    def searchWholeWord(self, w):
        return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search

    def read_words(self):
        lines = [line.rstrip('\n').decode('utf8') for line in open('textClassification/SentimentAnalisys/Data/rambo_baby_words.txt')]
        return lines

    def findin_matches_lambda(self, sentence=str, words=[]):
        retorno = filter(lambda x: sentence.count(x), words)
        return retorno

    def finding_matchs(self, sentence=str, words=[]):
        #sentence = u'' + sentence
        for word in words:
            return_value = self.searchWholeWord(word)(sentence)
            if return_value:
                break

        return return_value