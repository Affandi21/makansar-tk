import datetime
from .forms import RegisterForm, UserProfileForm, UserForm
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.urls import reverse
from main.models import Makanan, UserProfile
from django.contrib.auth.decorators import login_required

# Create your views here.
def show_main(request):
    return render(request,'main.html')

def show_foods(request):
    return render(request, 'show_foods.html')

def register(request):
    msg = None
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('main:show_main')
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
    response = HttpResponseRedirect(reverse('main:show_main'))
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

# Fungsi view user profile
def view_profile(request):
    return render(request, 'profile.html')

# Fungsi edit dashboard (profil user)
def edit_dashboard(request):
    user = request.user
    profile, created = UserProfile.objects.get_or_create(user_profile=user)  # Link with the correct UserProfile

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=profile)
        action = request.POST.get('action')

        if action == 'save' and user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('main:show_main')

        elif action == 'delete':
            return render(request, 'confirm_delete.html')  # Render the confirmation template

        elif action == 'confirm_delete':
            user.delete()
            logout(request)
            return redirect('main:show_main')

        elif action == 'cancel_delete':
            return redirect('main:edit_dashboard')

    else:
        user_form = UserForm(instance=user)
        profile_form = UserProfileForm(instance=profile)

    context = {'user_form': user_form, 'profile_form': profile_form}
    return render(request, 'dashboard.html', context)

def delete_account(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        logout(request)
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

<<<<<<< HEAD

def makanan_kategori_ayam(request):
    makanan_list = Makanan.objects.filter(category='Ayam')
    context = {
        'makanan_list': makanan_list,
    }
    return render(request, 'ayam.html', context)
=======
def show_ayam(request):
    makanan_list = Makanan.objects.filter(category='Ayam')
    context = {
        'makanan_list' : makanan_list,
    }
    return render(request, 'ayam.html', context)

def show_daging(request):
    makanan_list = Makanan.objects.filter(category='Daging')
    context = {
        'makanan_list' : makanan_list,
    }
    return render(request, 'daging.html', context)

def show_chinese_foood(request):
    makanan_list = Makanan.objects.filter(category='Chinese Food')
    context = {
        'makanan_list' : makanan_list,
    }
    return render(request, 'chinese_food.html', context)

def show_arabic_food(request):
    makanan_list = Makanan.objects.filter(category='Arabic Food')
    context = {
        'makanan_list' : makanan_list,
    }
    return render(request, 'arabic_food.html', context)

def show_dessert(request):
    makanan_list = Makanan.objects.filter(category='Dessert')
    context = {
        'makanan_list' : makanan_list,
    }
    return render(request, 'dessert.html', context)

def show_makanan_berkuah(request):
    makanan_list = Makanan.objects.filter(category='Makanan berkuah')
    context = {
        'makanan_list' : makanan_list,
    }
    return render(request, 'makanan_berkuah.html', context)

def show_nasi(request):
    makanan_list = Makanan.objects.filter(category='Nasi')
    context = {
        'makanan_list' : makanan_list,
    }
    return render(request, 'nasi.html', context)

def show_seafood(request):
    makanan_list = Makanan.objects.filter(category='Seafood')
    context = {
        'makanan_list' : makanan_list,
    }
    return render(request, 'seafood.html', context)

def show_martabak(request):
    makanan_list = Makanan.objects.filter(category='Martabak')
    context = {
        'makanan_list' : makanan_list,
    }
    return render(request, 'martabak.html', context)

def show_beverages(request):
    makanan_list = Makanan.objects.filter(category='Beverages')
    context = {
        'makanan_list' : makanan_list,
    }
    return render(request, 'beverages.html', context)
>>>>>>> f41fa6db9055daebe8754dd8a447abdf86bfabc6
