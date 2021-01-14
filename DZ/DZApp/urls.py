from django.urls import path
from . import views


urlpatterns = [
    path('', views.loginPage, name='login'),
    path('register/', views.regPage, name='register'),
    path('logout/', views.logoutPage, name='logout'),

    path('index/', views.index, name='home'),
    path('details/<int:tab_index>/', views.details, name='details'),
    path(r'update/<int:tab_index>/<int:pk>$', views.update, name='update'),
    path(r'delete/<int:tab_index>/<int:pk>$', views.delete, name='delete'),
    path('review/', views.review, name='review'),
    path('review/<int:tab_index>/', views.review_details, name='review_details'),
]
