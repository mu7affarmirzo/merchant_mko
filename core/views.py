from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.models import User

from core.forms import AccountAuthenticationForm
from rest_framework.generics import ListCreateAPIView

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
    return render(request, 'pages/index.html', {})


class TestCreateView(ListCreateAPIView):
    pass


















