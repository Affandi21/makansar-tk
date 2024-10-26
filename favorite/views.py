# favorite/views.py
from pyexpat.errors import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from .models import Favorite
from .models import Makanan  # Ganti dengan model produk yang sesuai
from django.http import JsonResponse

@login_required
def favorite_overview(request):
    # Get top 3 promoted products
    top_three_favorites = Favorite.objects.filter(user=request.user, is_top_three=True)[:3]
    
    # Get all favorite products of the user
    all_favorites = Favorite.objects.filter(user=request.user)
    
    # Get all products
    all_products = Makanan.objects.all()

    context = {
        'top_three_favorites': top_three_favorites,
        'all_favorites': all_favorites,
        'all_products': all_products,
    }
    
    return render(request, 'favorite_overview.html', context)

@login_required
def toggle_top_three(request, product_id):
    # Toggle the top three status of the product
    favorite = get_object_or_404(Favorite, product__id=product_id, user=request.user)
    
    if favorite.is_top_three:
        # Remove from top three
        favorite.is_top_three = False
    else:
        # Add to top three if there are fewer than three items already
        if Favorite.objects.filter(user=request.user, is_top_three=True).count() < 3:
            favorite.is_top_three = True

    favorite.save()
    return redirect('favorite:favorite_overview')

@login_required(login_url='/login')
def add_favorite(request, product_id):
    # Ambil produk berdasarkan ID
    product = get_object_or_404(Makanan, id=product_id)
    
    # Cek apakah produk sudah ada di favorit pengguna
    favorite, created = Favorite.objects.get_or_create(user=request.user, product=product)
    
    # if created:
    #     # Beri notifikasi sukses jika ditambahkan
    #     messages.success(request, f"{product.food_name} telah ditambahkan ke favorit Anda.")
    # else:
    #     # Beri notifikasi info jika sudah ada
    #     messages.info(request, f"{product.food_name} sudah ada di favorit Anda.")

    return redirect('favorite:favorite_overview')

@login_required(login_url='/login')
def delete_favorite(request, product_id):
    # Ambil produk berdasarkan ID
    product = get_object_or_404(Makanan, id=product_id)
    
    # Cek apakah produk ada di favorit pengguna
    favorite = Favorite.objects.filter(user=request.user, product=product)
    
    if favorite.exists():
        # Hapus produk dari favorit
        favorite.delete()
        # Beri notifikasi sukses
        # messages.success(request, f"{product.food_name} telah dihapus dari favorit Anda.")
    else:
        # Beri notifikasi info jika produk tidak ada di favorit
        messages.info(request, f"{product.food_name} tidak ada di favorit Anda.")

    # Redirect ke halaman daftar favorit atau halaman lain yang sesuai
    return redirect('favorite:favorite_overview')

