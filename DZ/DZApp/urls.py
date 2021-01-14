from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('<int:tab_index>/', views.details, name='details'),
    path('review/', views.review, name='review'),
    path('review/<int:tab_index>/', views.review_details, name='review_details'),

    path('register/', views.regPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
]
