from django.shortcuts import get_object_or_404, render
from .models import *

def index(request):
    table_list = Tables.objects.all()
    table_names = []
    for i in table_list:
        # if i.name == "Поставщики" or i.name == "Продукты":
        #     table_names.append(i.name)
        table_names.append(i.name)
    context = {'title':'ДЗ', 'header':'Таблицы', 'table_list':table_list}
    return render(request, 'DZApp/index.html', context)


def details(request, tab_index):
    print(f"\033[34mtab index is: {tab_index}\033[0m")
    header = ""
    if tab_index == 1:
        table_data = Partner.objects.all()
        header = "Партнеры"
    elif tab_index == 2:
        table_data = Partnership.objects.all()
        header = "Партнерство"
    elif tab_index == 3:
        table_data = Provider.objects.all()
        header = "Поставщики"
    elif tab_index == 4:
        table_data = Product.objects.all()
        header = "Продукты"
    elif tab_index == 5:
        table_data = Waybill.objects.all()
        header = "Накладные"
    return render(request, 'DZApp/details.html', {'title': 'Детали', 'header':header, 'table_data':table_data})

def review(request):
    return render(request, 'DZApp/review.html', {'title': 'Отчет', 'header':'Отчет'})

