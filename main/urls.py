from django.urls import path
from .views import login_view, home_page_view, logout_view, cancel_payments_page_view, filial_page_view, \
    cancel_payment_by_id_view, proceed_cancel_view
from django.contrib.auth import views

app_name = 'main'

urlpatterns = [
    path('login', views.LoginView.as_view(template_name='pages/signin.html'), name='login'),
    path('logout', logout_view, name='logout'),

    path('', home_page_view, name='home'),
    path('cancel-payments', cancel_payments_page_view, name='cancel-payments'),
    path('cancel/payments/<int:pk>', cancel_payment_by_id_view, name='cancel-payment-by-id'),
    path('cancel/payments/proceed/<int:pk>', proceed_cancel_view, name='cancel-payment-proceed'),

    path('payments/branch/<int:pk>', filial_page_view, name='payments-by-branches'),
]
