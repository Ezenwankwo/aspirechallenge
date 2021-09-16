from rest_framework import serializers

from .models import (
    Characters,
    Quotes,
    Favorites
)


class CharactersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Characters
        fields = '__all__'


class QuotesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Quotes
        fields = '__all__'


class FavoritesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Favorites
        fields = '__all__'

