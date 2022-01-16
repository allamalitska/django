from django.shortcuts import render

def categories(request):
    return render(request, 'main/categories.html')

def board_games(request):
    return render(request, 'main/board_games.html')

def card_games(request):
    return render(request, 'main/card_games.html')

def strategy_games(request):
    return render(request, 'main/strategy_games.html')
