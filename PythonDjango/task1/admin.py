from django.contrib import admin

# Register your models here.
from .models import Buyer, Game, News


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'cost', 'size',)
    list_filter = ('cost', 'size',)
    search_fields = ('title',)
    list_per_page = 20


@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ('name', 'balance', 'age',)
    list_filter = ('balance', 'age',)
    search_fields = ('name',)
    list_per_page = 30
    readonly_fields = ('balance',)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'date')
    readonly_fields = ('date',)
