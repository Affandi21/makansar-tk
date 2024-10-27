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
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('main:show_main')

        elif action == 'delete':
            return render(request, 'confirm_delete.html')  # Render the confirmation template

        elif action == 'confirm_delete':
            user.delete()
            logout(request)
            messages.success(request, 'Your account has been deleted successfully.')
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