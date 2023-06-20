
from django.contrib import admin
from django.urls import path
from myappdj import views

urlpatterns = [
    path('',views.home,name='home'),
    path('signup/',views.sign,name='sign'),
    path('login/',views.log,name='login'),
    path('anwer/',views.answer,name='ans'),
    path('admin/',views.que,name='admi'),

]
