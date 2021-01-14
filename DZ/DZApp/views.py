from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

from django.contrib import messages



from .models import *
from .forms import CreateUserForm, PartnerForm, ProviderForm, ProductForm

def index(request):
    table_list = Tables.objects.all()
    context = {'title':'ДЗ', 'header':'Таблицы', 'table_list':table_list}
    return render(request, 'DZApp/index.html', context)


def details(request, tab_index):
    print(f"\033[34mtab index is: {tab_index}\033[0m")
    header = ""

    if request.method == 'POST':
        if tab_index == 1:
            form = PartnerForm(request.POST)
        elif tab_index == 3:
            form = ProviderForm(request.POST)
        elif tab_index == 4:
            form = ProductForm(request.POST)
        if form.is_valid():
            form.save()

    if tab_index == 1:
        table_data = Partner.objects.all()
        form = PartnerForm()
        header = "Партнеры"
    elif tab_index == 3:
        table_data = Provider.objects.all()
        form = ProviderForm()
        header = "Поставщики"
    elif tab_index == 4:
        table_data = Product.objects.all()
        form = ProductForm()
        header = "Продукты"

    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = ""

    return render(request, 'DZApp/details.html', {'title': 'Детали', 'header':header, 'table_data':table_data,
                                                  'tab_index':tab_index, 'form':form, 'username':username})

def update(request, tab_index, pk):

    if tab_index == 1:
        to_edit = Partner.objects.get(pk=pk)
        form = PartnerForm(instance=to_edit)
        header = "Партнеры"
    elif tab_index == 3:
        to_edit = Provider.objects.get(pk=pk)
        form = ProviderForm(instance=to_edit)
        header = "Поставщики"
    elif tab_index == 4:
        to_edit = Product.objects.get(pk=pk)
        form = ProductForm(instance=to_edit)
        header = "Продукты"

    if request.method == 'POST':
        if tab_index == 1:
            form = PartnerForm(request.POST,instance=to_edit)
        elif tab_index == 3:
            form = ProviderForm(request.POST,instance=to_edit)
        elif tab_index == 4:
            form = ProductForm(request.POST,instance=to_edit)
        if form.is_valid():
            form.save()
            return redirect('details', tab_index)

    return render(request, 'DZApp/details.html', {'header':header, 'update':True, 'to_edit':to_edit, 'form':form})

def delete(request, tab_index, pk):
    to_delete = None
    if tab_index == 1:
        to_delete = Partner.objects.get(pk=pk)
    elif tab_index == 3:
        to_delete = Provider.objects.get(pk=pk)
    elif tab_index == 4:
        to_delete = Product.objects.get(pk=pk)

    to_delete.delete()

    return redirect('details', tab_index)

def review(request):
    table_list = Tables.objects.all()
    context = {'title':'Отчет', 'header':'Отчет', 'table_list':table_list}
    return render(request, 'DZApp/review.html', context)

def review_details(request, tab_index):

    if tab_index == 2:
        table_data = Partnership.objects.all()
        header = "Партнерство"
    elif tab_index == 4:
        table_data = Product.objects.all()
        header = "Продукты"
    elif tab_index == 5:
        table_data = Waybill.objects.all().select_related('provider', 'product')
        header = "Поставки"

    return render(request, 'DZApp/review_details.html', {'title': 'Отчет', 'header': header, 'table_data':table_data,
                                                         'tab_index':tab_index})

def loginPage(request):

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, "Имя пользователя или пароль введены не верно")

    context = {'title':'Авторизация'}
    return render(request, 'DZApp/auth/login.html', context)

def regPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, "Пользователь " + user + " успешно зарегистрирован")

            return redirect('login')

    context = {'title':'Регистрация', 'form':form}
    return render(request, 'DZApp/auth/registration.html', context)

def logoutPage(request):
    logout(request)
    return redirect('login')
