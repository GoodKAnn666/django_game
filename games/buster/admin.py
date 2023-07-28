from django.contrib import admin
from .models import Category, Developers, Genre, Games, GamesShorts, TopReating, Rating, Reviews

admin.site.register(Category)
admin.site.register(Developers)
admin.site.register(Genre)
admin.site.register(Games)
admin.site.register(GamesShorts)
admin.site.register(TopReating)
admin.site.register(Rating)
admin.site.register(Reviews)
