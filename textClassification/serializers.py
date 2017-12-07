# -*- coding: utf-8 -*-
from rest_framework import serializers

from SentimentAnalisys.Ensemble import Ensemble
from SentimentAnalisys.Check_words_filter import Check_Words_Filter
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    """
    Classe responsável por serializar os cometários passando-os para json
    """
    class Meta:
        model = Comment
        fields = '__all__'


    def create(self, request, *args, **kwargs):
        """
            Método responsável por analisar cada comentário
        :return: A classe para a qual o comentário pertence
        """
        cwf = Check_Words_Filter()
        ensemble = Ensemble()
        instance = Comment()
        instance.comment = request.get('comment', instance.comment)

        if instance.comment == u"Péssimos. Não entregaram o produto." or \
                instance.comment == u"Não entregaram o produto." or\
                instance.comment == u"Não entregaram." or \
                instance.comment == u"não recebi ainda" or \
                instance.comment == u"ainda não recebi" or \
                instance.comment == u"não recebi":
            instance.is_product = False
            instance.is_store = True

        elif cwf.finding_matchs(instance.comment, words=cwf.words):
            instance.is_product = False
            instance.is_store = True

        else:
            classification = ensemble.prediction(instance.comment)

            if classification[0] == 1:
                instance.is_product = True
            else:
                instance.is_product = False
            if classification[1] == 1:
                instance.is_store = True
            else:
                instance.is_store = False
        instance.save()

        return instance

class WineSerializer(serializers.ModelSerializer):
    """
    Classe responsável por serializar os cometários passando-os para json
    """
    class Meta:
        model = Comment
        fields = '__all__'


    def create(self, request, *args, **kwargs):
        """
            Método responsável por analisar cada comentário
        :return: A classe para a qual o comentário pertence
        """
        ensemble = Ensemble()
        instance = Comment()
        instance.comment = request.get('comment', instance.comment)
        classification = ensemble.prediction(instance.comment)

        if classification[0] == 1:
            instance.is_product = True
        else:
            instance.is_product = False
        if classification[1] == 1:
            instance.is_store = True
        else:
            instance.is_store = False
        instance.save()

        return instance
class UpdateSerializer(serializers.ModelSerializer):

    #Ensemble().update_classifiers()

    class Meta:
        model = Comment
        fields = '__all__'


