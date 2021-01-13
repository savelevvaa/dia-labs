from django.shortcuts import get_object_or_404, render
from .models import *

def index(request):
    table_list = Tables.objects.all()
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
    counter = 0
    return render(request, 'DZApp/details.html', {'title': 'Детали', 'header':header, 'table_data':table_data,
                                                  'tab_index':tab_index})

def review(request):
    table_list = Tables.objects.all()
    context = {'title':'Отчет', 'header':'Отчет', 'table_list':table_list}
    return render(request, 'DZApp/review.html', context)

def review_details(request, tab_index):

    if tab_index == 2:
        table_data = Partnership.objects.all()
        header = "Партнерство"
    elif tab_index == 5:
        table_data = Waybill.objects.all().select_related('provider', 'product')
        header = "Поставки"

    return render(request, 'DZApp/review_details.html', {'title': 'Отчет', 'header': header, 'table_data':table_data,
                                                         'tab_index':tab_index})
