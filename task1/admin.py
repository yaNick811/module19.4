from django.contrib import admin
from .models import Game, Buyer

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_filter = ('size', 'cost')  # Фильтрация по полям size и cost
    list_display = ('title', 'cost', 'size')  # Отображение полей title, cost и size
    search_fields = ('title',)  # Поиск по полю title
    list_per_page = 20  # Ограничение кол-ва записей до 20

@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_filter = ('balance', 'age')  # Фильтрация по полям balance и age
    list_display = ('name', 'balance', 'age')  # Отображение полей name, balance и age
    search_fields = ('name',)  # Поиск по полю name
    list_per_page = 30  # Ограничение кол-ва записей до 30
    readonly_fields = ('balance',)  # Поле balance доступно только для чтения

    # Доступным только для чтения поле balance
    readonly_fields = ('balance',)