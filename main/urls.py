from django.urls import path
from .views import login_view, home_page_view, logout_view
from django.contrib.auth import views

app_name = 'main'

urlpatterns = [
    path('login', views.LoginView.as_view(template_name='pages/signin.html'), name='login'),
    path('', home_page_view, name='home'),
    path('logout', logout_view, name='logout'),
]
