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



        if cwf.finding_matchs(instance.comment, words=["Utilizei assim que chegou, nem tive tempo de usar antes.\r\nAchei confortável.\r\nMaaaaas... Trilhas não costumam ser 100% seca, sempre tem lama e tals.\r\nFui em uma com cachoeira e óbvio que sei que o produto não é impermeável mas escorreguei e meu pé afundou na água \r\nAté aí tranquilo...porém qnd cheguei em casa e tirei a bota...percebi que embaixo da palminha não existe costura e sim um pedaço de papelão.\r\nAchei muuita sacanagem isso...o papelão foi pro saco e ficou só a palminha e o solado borrachudo"]):
            instance.is_product = True
            instance.is_store = False
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


