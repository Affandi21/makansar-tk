# favorite/views.py
from pyexpat.errors import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from .models import Favorite
from .models import Makanan  # Ganti dengan model produk yang sesuai
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .forms import Komentar
from django.views.decorators.csrf import csrf_exempt
import json

@login_required
def favorite_overview(request):

    top_three_favorites = Favorite.objects.filter(user=request.user, is_top_three=True)[:3]
    all_favorites = Favorite.objects.filter(user=request.user)
    all_products = Makanan.objects.all()
    favorite_product_ids = set(all_favorites.values_list('product_id', flat=True))

    context = {
        'top_three_favorites': top_three_favorites,
        'all_favorites': all_favorites,
        'all_products': all_products,
        'favorite_product_ids': favorite_product_ids,
    }
    
    return render(request, 'favorite_overview.html', context)

@login_required
def toggle_top_three(request, product_id):

    favorite = get_object_or_404(Favorite, product__id=product_id, user=request.user)
    
    if favorite.is_top_three:
        favorite.is_top_three = False
    else:
        if Favorite.objects.filter(user=request.user, is_top_three=True).count() < 3:
            favorite.is_top_three = True

    favorite.save()
    return redirect('favorite:favorite_overview')

@login_required(login_url='/login')
def add_favorite(request, product_id):
    # Ambil produk berdasarkan ID
    product = get_object_or_404(Makanan, id=product_id)
    
    favorite, created = Favorite.objects.get_or_create(user=request.user, product=product)
    if created:
        favorite.is_favorite = True
    else:
        favorite.is_favorite = False

    return redirect('favorite:favorite_overview')

@login_required(login_url='/login')
def delete_favorite(request, product_id):
    # Ambil produk berdasarkan ID
    product = get_object_or_404(Makanan, id=product_id)
    
    favorite = Favorite.objects.filter(user=request.user, product=product)
    
    if favorite.exists():
        # Hapus produk dari favorit
        favorite.delete()
        # Beri notifikasi sukses
        # messages.success(request, f"{product.food_name} telah dihapus dari favorit Anda."

    # Redirect ke halaman daftar favorit atau halaman lain yang sesuai
    return redirect('favorite:favorite_overview')

@login_required
def toggle_favorite(request, product_id):
    product = get_object_or_404(Makanan, id=product_id)
    favorite, created = Favorite.objects.get_or_create(user=request.user, product=product)
    
    if not created:
        favorite.delete()
        return JsonResponse({'status': 'removed', 'product_id': product_id}, status=200)
    return JsonResponse({'status': 'added', 'product_id': product_id}, status=200)

@csrf_exempt
def add_comment(request, product_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        content = data.get('content')
        if content:
            favorite = get_object_or_404(Favorite, user=request.user, product_id=product_id)
            comment = Komentar.objects.create(favorite=favorite, user=request.user, content=content)
            return JsonResponse({'success': True, 'username': request.user.username, 'content': content})
    return JsonResponse({'success': False})
