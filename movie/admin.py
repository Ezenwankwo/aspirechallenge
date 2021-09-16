from typing import ClassVar
from django.contrib import admin

from .models import Characters, Quotes, Favorites


class CharactersAdmin(admin.ModelAdmin):
    pass 


class QuotesAdmin(admin.ModelAdmin):
    pass


class FavoritesAdmin(admin.ModelAdmin):
    pass


admin.site.register(Characters, CharactersAdmin)
admin.site.register(Quotes, QuotesAdmin)
admin.site.register(Favorites, FavoritesAdmin)