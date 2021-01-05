from django.shortcuts import get_object_or_404, render
from .models import *

def index(request):
    table_list = Tables.objects.all()
    table_names = []
    for i in table_list:
        # if i.name == "Поставщики" or i.name == "Продукты":
        #     table_names.append(i.name)
        table_names.append(i.name)
    context = {'title':'ДЗ', 'header':'Таблицы', 'table_names':table_names}
    return render(request, 'DZApp/index.html', context)


def details(request):
    return render(request, 'DZApp/details.html', {'title': 'Детали', 'header':'Таблицы'})

def review(request):
    return render(request, 'DZApp/review.html', {'title': 'Отчет', 'header':'Отчет'})

