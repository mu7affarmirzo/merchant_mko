from django.contrib import admin
from .models.mko_models import Accounts, TransactionAccounts, Payments, Brands, Merchants, Cards, Clients


# Register your models here.


@admin.register(Accounts)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('inn', 'filial', 'number')


@admin.register(TransactionAccounts)
class TransactionAccountsAdmin(admin.ModelAdmin):
    list_display = ('sender_id', 'receiver_id', 'amount')


@admin.register(Payments)
class PaymentsAdmin(admin.ModelAdmin):
    list_display = ('client_id', 'merchant_id', 'amount')
    search_fields = ('merchant__id', )


@admin.register(Merchants)
class MerchantsAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand', 'name', 'account', 'key')
    search_fields = ('key', 'id', 'brand')


@admin.register(Cards)
class CardsAdmin(admin.ModelAdmin):
    list_display = ('number', 'owner', 'balance')
    search_fields = ('number', )


admin.site.register(Brands)
admin.site.register(Clients)

