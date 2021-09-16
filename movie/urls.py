from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    CharactersViewset,
    QuotesViewset,
    FavoriteCharacterView,
    FavoriteQuoteAndCharacterView,
    FavoritesViewset
)


router = DefaultRouter(trailing_slash=False)
router.register(r'characters', CharactersViewset)
router.register(r'^characters/(?P<id>\d+)/quotes', QuotesViewset, basename='character_quotes')
router.register(r'favorites', FavoritesViewset)


urlpatterns = [
    path('', include(router.urls)),
    path('characters/<id>/favorites', FavoriteCharacterView.as_view()),
    path('characters/<character_id>/quotes/<quote_id>/favorites', FavoriteQuoteAndCharacterView.as_view())
]