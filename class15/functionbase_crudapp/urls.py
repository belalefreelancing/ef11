from django.urls import path
from .views import *
urlpatterns = [
    path('dashboard/home', dashboardhome, name='dashboard-home'),
    path('banner/detail/<pk>', detail_view, name='detail-view'),
    path('banner-add', banner_add, name='banner-add'),
    path('banner/edit/<pk>', banner_eidt, name='banner-edit'),
    path('banner/delete/<pk>', delete, name='delete'),

]