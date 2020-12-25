from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('<int:phen_id>/', views.details, name='details'),
]
