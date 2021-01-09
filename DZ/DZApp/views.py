from django.shortcuts import get_object_or_404, render
from .models import *

def index(request):
    table_list = Tables.objects.all()
    #temp = Provider.partners.
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
    counter = 0
    return render(request, 'DZApp/details.html', {'title': 'Детали', 'header':header, 'table_data':table_data,
                                                  'tab_index':tab_index})

def review(request):
    return render(request, 'DZApp/review.html', {'title': 'Отчет', 'header':'Отчет'})

def review_waybill(request):
    header = "Поставки"

    table_data = Waybill.objects.all()
    providers = {}
    for row in table_data:
        prov_id = row.provider.id
        providers[get_object_or_404(Provider, pk=prov_id).id] = get_object_or_404(Provider, pk=prov_id).phone

    print(providers)

    return render(request, 'DZApp/review_waybill.html', {'title': 'Отчет', 'header': header, 'table_data':table_data,
                                                         'providers':providers})


def review_partnership(request):
    header = "Партнерство"
    table_data = Partnership.objects.all()
    return render(request, 'DZApp/review_waybill.html', {'title': 'Отчет', 'header': header, 'table_data':table_data})


