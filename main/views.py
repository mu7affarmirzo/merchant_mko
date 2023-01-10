from datetime import datetime

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.contrib.auth.models import User

from core.forms import AccountAuthenticationForm
from core.models.mko_models import Payments, Merchants, Brands, Transactions
from main.models import BrandsProfile
from main.services import merchant_info_service, sales_service, proceed_cancel_service


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

    account = request.user
    merchant_key = account.merchant_prof.merchant_key
    context = {}
    try:
        merchant_model = Merchants.objects.get(key=merchant_key)
    except Merchants.DoesNotExist:
        return render(request, 'pages/index.html', {"payments": {}})
    except Merchants.MultipleObjectsReturned:
        merchant_model = Merchants.objects.filter(key=merchant_key).first()

    if BrandsProfile.objects.filter(user=account).exists():
        merchant_bank_balance = merchant_info_service(merchant_model.account.number)
        brand = BrandsProfile.objects.get(user=account)
        brand_merchants = Merchants.objects.filter(brand__name=brand.brand)
        context['brand_merchants'] = brand_merchants
        context['merchant_bank_balance'] = merchant_bank_balance
        context['is_brand'] = True

    payments = Payments.objects.filter(merchant=merchant_model)
    balance = merchant_model.account.card.balance

    total_sales, today_sales = sales_service(payments)

    context['payments'] = payments
    context['total_sales'] = int(total_sales['amount__sum']/100)
    context['today_sales'] = int(today_sales['amount__sum']/100)
    context['balance'] = balance

    return render(request, 'pages/index.html', context)


@login_required
def wallet_to_bank_acc_view(request):

    account = request.user
    merchant_key = account.merchant_prof.merchant_key
    context = {}
    try:
        merchant_model = Merchants.objects.get(key=merchant_key)
    except Merchants.DoesNotExist:
        return render(request, 'pages/index.html', {"payments": {}})
    except Merchants.MultipleObjectsReturned:
        merchant_model = Merchants.objects.filter(key=merchant_key)
        merchant_model = merchant_model[0]

    if BrandsProfile.objects.filter(user=account).exists():
        brand = BrandsProfile.objects.get(user=account)
        brand_merchants = Merchants.objects.filter(brand__name=brand.brand)
        context['brand_merchants'] = brand_merchants

    payments = Payments.objects.filter(merchant=merchant_model)
    transactions = Transactions.objects.filter(account=merchant_model.account)

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

    context['transactions'] = transactions
    context['total_sales'] = total_sales
    context['today_sales'] = today_sales
    context['balance'] = balance
    print(transactions)

    return render(request, 'pages/wallet-to-bank.html', context)


@login_required
def cancel_payments_page_view(request):

    account = request.user
    merchant_key = account.merchant_prof.merchant_key
    context = {}
    try:
        merchant_model = Merchants.objects.get(key=merchant_key)
    except Merchants.DoesNotExist:
        return render(request, 'pages/index.html', {"payments": {}})
    except Merchants.MultipleObjectsReturned:
        merchant_model = Merchants.objects.filter(key=merchant_key)
        merchant_model = merchant_model[0]

    if BrandsProfile.objects.filter(user=account).exists():
        brand = BrandsProfile.objects.get(user=account)
        brand_merchants = Merchants.objects.filter(brand__name=brand.brand)
        context['brand_merchants'] = brand_merchants

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

    context['payments'] = payments
    context['total_sales'] = total_sales
    context['today_sales'] = today_sales
    context['balance'] = balance

    return render(request, 'pages/cancel_payments.html', context)


@login_required
def cancel_payment_by_id_view(request, pk):

    account = request.user
    merchant_key = account.merchant_prof.merchant_key
    context = {}
    try:
        merchant_model = Merchants.objects.get(key=merchant_key)
    except Merchants.DoesNotExist:
        return render(request, 'pages/index.html', {"payments": {}})
    except Merchants.MultipleObjectsReturned:
        merchant_model = Merchants.objects.filter(key=merchant_key)
        merchant_model = merchant_model[0]

    if BrandsProfile.objects.filter(user=account).exists():
        brand = BrandsProfile.objects.get(user=account)
        brand_merchants = Merchants.objects.filter(brand__name=brand.brand)
        context['brand_merchants'] = brand_merchants

    payment = Payments.objects.get(pk=pk)
    balance = merchant_model.account.card.balance

    context['payment'] = payment
    context['balance'] = balance

    return render(request, 'pages/cancel_payments_individual.html', context)


@login_required
def proceed_cancel_view(request, pk):
    payment = get_object_or_404(Payments, pk=pk)
    print(payment.tr_id)
    response = proceed_cancel_service(payment.tr_id)
    return redirect('main:home')


@login_required
def filial_page_view(request, pk):

    account = request.user
    context = {}

    if BrandsProfile.objects.filter(user=account).exists():
        merchant_bank_balance = merchant_info_service('2342342343')
        brand = BrandsProfile.objects.get(user=account)
        brand_merchants = Merchants.objects.filter(brand__name=brand.brand)
        context['brand_merchants'] = brand_merchants
        context['merchant_bank_balance'] = merchant_bank_balance

    target_merchant = Merchants.objects.get(pk=pk)
    payments = Payments.objects.filter(merchant=target_merchant)
    balance = target_merchant.account.card.balance

    total_sales, today_sales = sales_service(payments)

    context['payments'] = payments
    context['total_sales'] = total_sales
    context['today_sales'] = today_sales
    context['balance'] = balance

    return render(request, 'pages/by_filial.html', context)


def logout_view(request):
    logout(request)
    return redirect('main:login')
