from rest_framework import viewsets, views, status
from rest_framework.response import Response

from .models import (
    Characters,
    Quotes,
    Favorites
)

from .serializers import (
    CharactersSerializer,
    QuotesSerializer,
    FavoritesSerializer
)


class CharactersViewset(viewsets.ModelViewSet):
    '''Return all characters'''
    serializer_class = CharactersSerializer
    queryset = Characters.objects.all()


class QuotesViewset(viewsets.ModelViewSet):
    '''Return quotes belonging a specific character'''
    serializer_class = QuotesSerializer
    
    def get_queryset(self):
        character = self.kwargs['id']
        queryset = Quotes.objects.filter(character=character)
        return queryset


class FavoriteCharacterView(views.APIView):
    '''Favorite a specific character'''

    def post(self, request, id):
        character = Characters.objects.get(id=id)
        user = request.user
        favorite = Favorites.objects.filter(user=user, character=character)
        if favorite.exists():
            return Response(status=status.HTTP_200_OK)
        else:
            Favorites.objects.create(user=user, character=character)
            return Response(status=status.HTTP_201_CREATED)


class FavoriteQuoteAndCharacterView(views.APIView):
    '''Favorite a quote and the character that made the quote'''

    def post(self, request, character_id, quote_id):
        user = request.user
        quote = Quotes.objects.get(id=quote_id)
        character = Characters.objects.get(id=character_id)
        favorite = Favorites.objects.filter(user=user, character=character, quote=quote)
        if favorite.exists():
            return Response(status=status.HTTP_200_OK)
        else:
            Favorites.objects.create(user=user, character=character, quote=quote)
            return Response(status=status.HTTP_201_CREATED)


class FavoritesViewset(viewsets.ModelViewSet):
    '''Return all favorite items'''
    serializer_class = FavoritesSerializer
    queryset = Favorites.objects.all()