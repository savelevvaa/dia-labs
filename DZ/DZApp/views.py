from django.shortcuts import render

def index(request):
    return render(request, 'DZApp/index.html', {'title':'ДЗ', 'header':'Таблицы'})


def details(request):
    return render(request, 'DZApp/details.html', {'title': 'Детали', 'header':'Таблицы'})

def review(request):
    return render(request, 'DZApp/review.html', {'title': 'Отчет', 'header':'Отчет'})

