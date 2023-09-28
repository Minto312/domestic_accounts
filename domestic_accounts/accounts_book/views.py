from django.shortcuts import render, redirect
from .models import RestAmount, IncomePayment

# Create your views here.

def index(request):
    # fix format of amount
    rest_amounts = [{'kind':x.kind,'rest_amount':'\{:,d}'.format(x.rest_amount)} for x in RestAmount.objects.all()]
    incomes = IncomePayment.objects.filter(income_or_payment='income')
    payments = IncomePayment.objects.filter(income_or_payment='payment')
    context = {
        'rest_amounts': rest_amounts,
        'incomes': incomes,
        'payments': payments,
    }
    return render(request, 'accounts_book/index.html', context=context)

def income_payment_add(request):
    data = {
        'date': request.POST['date'],
        'kind': request.POST['kind'],
        'price': request.POST['price'],
        'description': request.POST['description'],
        'income_or_payment': request.POST['income-or-payment'],
    }
    IncomePayment.objects.create(**data)
    return redirect('accounts_book:index')