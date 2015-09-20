from django.forms import widgets
from rest_framework import serializers
from games.models import Game


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'title', 'gamePicUrl', 'pic1Url', 'pic2Url', 'pic3Url', 'publisher', 'publishedDate',
        	'ratedInfo', 'gameCats','trailerUrl', 'buyUrl', 'rating', 'pricing')

