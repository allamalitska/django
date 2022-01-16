from . import views
from django.urls import path


urlpatterns = [
    path('',views.categories, name = 'home'),
    path('board-games',views.board_games, name ='boardgames'),
    path('card-games',views.card_games, name ='cardgames'),
    path('strategy-games',views.strategy_games, name ='strategygames'),
]
