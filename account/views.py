import datetime
from .forms import MakananForm
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
import json
from django.http import JsonResponse

# Create your views here.

@login_required(login_url='/login/')
def seller(request):
    if not request.user.seller:
        return redirect('account:buyerpage')  

    context = {
        'user_shop_name': f"{request.user.nama} shop",
    }

    return render(request, 'seller.html', context)

@csrf_exempt
@require_POST
def add_makanan_ajax(request):
    category = request.POST.get("category")
    food_name = strip_tags(request.POST.get("food_name"))
    location = strip_tags(request.POST.get("location"))
    price = request.POST.get("price")
    food_desc = strip_tags(request.POST.get("food_desc"))
    user = request.user
    shop_name = user.nama + " shop"
    rating_default = 0


    new_product = Makanan(
        category=category, food_name=food_name, location=location,
        shop_name=shop_name, price=price, rating_default=rating_default,
        food_desc=food_desc
    )
    new_product.save()

    return HttpResponse(b"CREATED", status=201)

@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':

        data = json.loads(request.body)
        new_product = Makanan.objects.create(
            category=data["category"],
            food_name=data["food_name"],
            location=data["location"],
            shop_name=data["shop_name"],
            price=int(data["price"]),
            rating_default=0,
            food_desc=data["food_desc"],
        )

        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)

def edit_product(request, id):
    # Get product entry berdasarkan id
    product = Makanan.objects.get(pk = id)

    # Set product entry sebagai instance dari form
    form = MakananForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('account:sellerpage'))

    context = {'form': form}
    return render(request, "edit_product.html", context)

def delete_product(request, id):
    # Get product berdasarkan id
    product = Makanan.objects.get(pk = id)
    # Hapus product
    product.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse('account:sellerpage'))

@csrf_exempt
@login_required
def delete_product_flutter(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            product_id = data.get("id")  # Mengambil ID produk dari request body
            if not product_id:
                return JsonResponse({"status": "error", "message": "ID produk tidak disediakan"}, status=400)

            product = Makanan.objects.get(pk=product_id)
            product.delete()
            return JsonResponse({"status": "success"}, status=200)
        except Makanan.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Produk tidak ditemukan"}, status=404)
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=500)
    return JsonResponse({"status": "error", "message": "Metode request tidak valid"}, status=400)

@csrf_exempt
@login_required
def update_product(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            product = Makanan.objects.get(pk=data['id'])
            product.category = data['category']
            product.food_name = data['food_name']
            product.location = data['location']
            product.price = data['price']
            product.food_desc = data['food_desc']
            product.save()
            return JsonResponse({"status": "success"}, status=200)
        except Makanan.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Product not found"}, status=404)
    return JsonResponse({"status": "error", "message": "Invalid request method"}, status=400)
