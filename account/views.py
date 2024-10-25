import datetime
from .forms import RegisterForm
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.urls import reverse
from main.models import Makanan
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/login')
def buyer(request):
    return render(request,'buyer.html')

def seller(request):
    return render(request,'seller.html')

def register(request):
    msg = None
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('account:login')
        else:
            msg = 'form is not valid'
    else:
        form = RegisterForm()
    return render(request,'register.html', {'form': form, 'msg': msg})

def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)
    msg = None

    if request.method == 'POST':
        if form.is_valid():
            user = form.get_user()  # Mendapatkan user yang sudah di-autentikasi oleh form
            login(request, user)  # Login user

            # Cek apakah user buyer atau seller dan redirect sesuai role-nya
            if user.seller:
                return redirect('account:sellerpage')
            elif user.buyer:
                return redirect('account:buyerpage')
        else:
            msg = 'Invalid credentials'

    return render(request, 'login.html', {'form': form, 'msg': msg})

@csrf_exempt
@require_POST
def add_makanan_ajax(request):
    category = request.POST.get("category")
    food_name = strip_tags(request.POST.get("food_name"))
    location = strip_tags(request.POST.get("location"))
    shop_name = strip_tags(request.POST.get("shop_name"))
    price = request.POST.get("price")
    rating_default = request.POST.get("rating_default")
    food_desc = strip_tags(request.POST.get("food_desc"))
    user = request.user

    new_product = Makanan(
        category=category, food_name=food_name, location=location,
        shop_name=shop_name, price=price, rating_default=rating_default,
        food_desc=food_desc, user=user
    )
    new_product.save()

    return HttpResponse(b"CREATED", status=201)