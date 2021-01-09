from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('<int:tab_index>/', views.details, name='details'),
    path('review/', views.review, name='review'),
    path('review/waybill', views.review_waybill, name='review_waybill'),
    path('review/partnership', views.review_partnership, name='review_partnership'),
]
