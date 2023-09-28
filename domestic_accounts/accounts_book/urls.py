from django.urls import path
from .apps import AccountsBookConfig
from . import views

app_name = AccountsBookConfig.name

urlpatterns = [
    path('', views.index, name='index'),
    path('income-payment-add/', views.income_payment_add, name='income_payment_add'),
]
