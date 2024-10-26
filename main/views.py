import datetime
from .forms import RegisterForm, UserProfileForm
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
from main.models import Makanan, UserProfile
from django.contrib.auth.decorators import login_required

# Create your views here.
def show_main(request):
    return render(request,'main.html')

def register(request):
    msg = None
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('main:login')
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
            user = form.get_user()
            login(request, user) 
            return redirect('main:show_main')
        else:
            msg = 'Invalid credentials'

    return render(request, 'login.html', {'form': form, 'msg': msg})

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def show_xml(request):
    data = Makanan.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_xml_by_id(request, id):
    data = Makanan.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Makanan.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
    data = Makanan.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

# Fungsi dashboard
def edit_dashboard(request):
    profile, created = UserProfile.objects.get_or_create(id=1)  # Sementara pakai ini saat belum ada login form
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        action = request.POST.get('action')

        if action == 'save' and form.is_valid():
            form.save()
            return redirect('main:show_main')

        elif action == 'delete':
            form = UserProfileForm()
            return render(request, 'dashboard.html', {'form': form})

    else:
        form = UserProfileForm(instance=profile)

    context = {'form': form}
    return render(request, 'dashboard.html', context)