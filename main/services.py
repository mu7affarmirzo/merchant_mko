import requests
from decouple import config
from datetime import datetime

from django.db.models import Sum

url = config('WALLET_URL')


def merchant_info_service(number):
    payload = {
        "jsonrpc": "2.0",
        "id": "{{$randomUUID}}",
        "method": "merchant.balance",
        "params": {
            "account": f"{number}"
        }
    }

    headers = {
        "Authorization": f"Bearer {config('WALLET_TOKEN')}",
        "Content-Type": "application/json"
    }
    try:
        response = requests.post(url=url, headers=headers, json=payload)
        response = response.json()
        return int(response['result']['saldo'])/100
    except:
        return 0


def sales_service(payments):
    payments = payments.filter(status=1)
    total_sales = payments.aggregate(Sum('amount'))
    if len(payments.filter(created_at=datetime.now().date())) == 0:
        today_sales = {
            'amount__sum': 0
        }
    else:
        today_sales = payments.filter(created_at=datetime.now().date()).aggregate(Sum('amount'))

    return total_sales, today_sales


def proceed_cancel_service(tr_id):
    payload = {
        "jsonrpc": "2.0",
        "id": "{{$randomUUID}}",
        "method": "payment.cancel",
        "params": {
            "tr_id": f"{tr_id}"
        }
    }

    headers = {
        "Authorization": f"Bearer {config('WALLET_TOKEN')}",
        "Content-Type": "application/json"
    }
    try:
        response = requests.post(url=url, headers=headers, json=payload)
        response = response.json()
        return response['status']
    except:
        return False


def wallet_to_bank_account_service(tr_id):
    payload = {
        "jsonrpc": "2.0",
        "id": "{{$randomUUID}}",
        "method": "transaction.send",
        "params": {
            "tr_id": f"{tr_id}"
        }
    }

    headers = {
        "Authorization": f"Bearer {config('WALLET_TOKEN')}",
        "Content-Type": "application/json"
    }
    try:
        response = requests.post(url=url, headers=headers, json=payload)
        response = response.json()
        return response['status']
    except:
        return False