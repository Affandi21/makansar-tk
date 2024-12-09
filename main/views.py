import datetime
import logging
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
from main.models import Makanan, UserProfile
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from forum.models import Discussion, Reply
from main.models import Makanan
from forum.forms import DiscussionForm, ReplyForm
import json

logger = logging.getLogger(__name__)

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
@login_required
def view_profile(request):
    return render(request, 'profile.html')

# Fungsi edit dashboard (profil user)
@login_required
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

# Modul profile baru untuk terhubung ke Flutter
def get_profile(request):
    user = request.user
    profile, created = UserProfile.objects.get_or_create(user_profile=user)
    data = {
        'username': user.username,
        'nama': user.nama,
        'no_telp': user.no_telp,
        'tanggal_lahir': user.tanggal_lahir,
        'buyer': user.buyer,
        'seller': user.seller,
        'profile_image': profile.profile_image.url if profile.profile_image else None,
        'jenis_kelamin': profile.jenis_kelamin if profile.jenis_kelamin else None,
        'email': profile.email if profile.email else None,
        'alamat': profile.alamat if profile.alamat else None,
    }
    return JsonResponse(data)
 
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

@csrf_exempt
@login_required
def create_discussion(request, makanan_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        user = request.user
        makanan = Makanan.objects.get(pk=makanan_id)
        discussion = Discussion.objects.create(
            user=user, makanan=makanan, title=data['title'], message=data['message']
        )
        return JsonResponse({'status': 'success', 'discussion_id': discussion.id})

@csrf_exempt
@login_required
def edit_discussion(request, discussion_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        discussion = Discussion.objects.get(pk=discussion_id, user=request.user)
        discussion.title = data['title']
        discussion.message = data['message']
        discussion.save()
        return JsonResponse({'status': 'success'})

@csrf_exempt
@login_required
def delete_discussion(request, discussion_id):
    if request.method == 'DELETE':
        discussion = Discussion.objects.get(pk=discussion_id, user=request.user)
        discussion.delete()
        return JsonResponse({'status': 'success'})

@csrf_exempt
@login_required
def add_reply(request, discussion_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        user = request.user
        discussion = Discussion.objects.get(pk=discussion_id)
        reply = Reply.objects.create(
            discussion=discussion, user=user, message=data['message']
        )
        return JsonResponse({'status': 'success', 'reply_id': reply.id})

@csrf_exempt
@login_required
def edit_reply(request, reply_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        reply = Reply.objects.get(pk=reply_id, user=request.user)
        reply.message = data['message']
        reply.save()
        return JsonResponse({'status': 'success'})

@csrf_exempt
@login_required
def delete_reply(request, reply_id):
    if request.method == 'DELETE':
        reply = Reply.objects.get(pk=reply_id, user=request.user)
        reply.delete()
        return JsonResponse({'status': 'success'})

@csrf_exempt
def fetch_discussions(request, makanan_id):
    if request.method == 'GET':
        discussions = Discussion.objects.filter(makanan_id=makanan_id)
        data = [
            {
                'id': d.id,
                'title': d.title,
                'message': d.message,
                'user': d.user.username,
                'date_created': d.date_created.isoformat(),
                'replies': [
                    {
                        'id': r.id,
                        'message': r.message,
                        'user': r.user.username,
                        'date_created': r.date_created.isoformat(),
                    }
                    for r in d.replies.all()
                ],
            }
            for d in discussions
        ]
        print(data)  # Log data yang dikirimkan ke Flutter
        return JsonResponse(data, safe=False)
