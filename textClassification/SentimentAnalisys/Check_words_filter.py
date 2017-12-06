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
        lines = [line.rstrip('\n') for line in open('textClassification/SentimentAnalisys/Data/rambo_baby_words.txt')]
        return lines

    def finding_matchs(self, sentence=str, words=[]):
        sentence = sentence.lower()
        for word in words:
            return_value = self.searchWholeWord(word)(sentence)
            if return_value:
                break

        return return_value