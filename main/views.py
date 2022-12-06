from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
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
    merchant_model = Merchants.objects.filter(key=merchant_key)
    payments = Payments.objects.filter(merchant=merchant_model[0])
    # balance = merchant_model.acount.card
    # print(balance)
    print("*************************************")
    print(f"merchant: {merchant_model[0]}")
    print(f"payments: {payments}")
    print("*************************************")
    print(payments)
    return render(request, 'pages/index.html', {"payments": payments})


def logout_view(request):
    logout(request)
    return redirect('core:login')
