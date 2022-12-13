from datetime import datetime

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.models import User

from core.forms import AccountAuthenticationForm
from core.models.mko_models import Payments, Merchants


def login_view(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect("home")
    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect("home")
    else:
        form = AccountAuthenticationForm()

    context['login_form'] = form
    return render(request, 'pages/signin.html', context)


@login_required
def home_page_view(request):
    merchant = request.user
    merchant_key = merchant.merchant_prof.merchant_key
    try:
        merchant_model = Merchants.objects.get(key=merchant_key)
    except Merchants.DoesNotExist:
        return render(request, 'pages/index.html', {"payments": {}})
    except Merchants.MultipleObjectsReturned:
        merchant_model = Merchants.objects.filter(key=merchant_key)
        merchant_model = merchant_model[0]

    payments = Payments.objects.filter(merchant=merchant_model)
    balance = merchant_model.account.card.balance
    merchant_card = merchant_model.account.card
    print(f"Balance: {balance}")

    total_sales = payments.aggregate(Sum('amount'))
    if len(payments.filter(created_at=datetime.now().date())) == 0:
        today_sales = {
            'amount__sum': 0
        }
    else:
        today_sales = payments.filter(created_at=datetime.now().date()).aggregate(Sum('amount'))

    context = {
        "payments": payments,
        "total_sales": total_sales,
        "today_sales": today_sales,
        "balance": balance
    }
    return render(request, 'pages/index.html', context)


def logout_view(request):
    logout(request)
    return redirect('core:login')
