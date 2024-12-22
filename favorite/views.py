# favorite/views.py
from pyexpat.errors import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from yaml import serialize
from .models import Favorite
from .models import Makanan  # Ganti dengan model produk yang sesuai
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import HttpResponseForbidden
from django.core import serializers

@csrf_exempt
@login_required
def favorite_overview(request):
    if not request.user.buyer:
        return HttpResponseForbidden("You do not have permission to access this page.")
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
@csrf_exempt
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

@csrf_exempt
@login_required(login_url='/login')
def add_favorite(request, product_id):
    # Ambil produk berdasarkan ID
    product = get_object_or_404(Makanan, id=product_id)
    
    favorite, created = Favorite.objects.get_or_create(user=request.user, product=product)
    if created:
        favorite.is_favorite = True
    else:
        favorite.is_favorite = False

    favorite.save()
    return redirect('favorite:favorite_overview')

@csrf_exempt
@login_required(login_url='/login')
def delete_favorite(request, product_id):
    # Ambil produk berdasarkan ID
    product = get_object_or_404(Makanan, id=product_id)
    
    favorite = Favorite.objects.filter(user=request.user, product=product)
    
    if favorite.exists():
        # Hapus produk dari favorit
        favorite.delete()
        # messages.success(request, f"{product.food_name} telah dihapus dari favorit Anda."

    # Redirect ke halaman daftar favorit atau halaman lain yang sesuai
    return redirect('favorite:favorite_overview')

@csrf_exempt
@login_required(login_url='/login')
def toggle_favorite(request, product_id):
    if request.method != 'POST':
        return JsonResponse({'error': 'Invalid HTTP method'}, status=400)

    product = get_object_or_404(Makanan, id=product_id)

    favorite, created = Favorite.objects.get_or_create(user=request.user, product=product)
    
    if created:
        favorite.is_favorite = True
        favorite.save()
        return JsonResponse({
            'success': True,
            'status': 'added',
        }, status=200)
    else:
        favorite.is_favorite = not favorite.is_favorite
        favorite.save()
        status_action = 'added' if favorite.is_favorite else 'removed'
        return JsonResponse({
            'success': True,
            'status': status_action,
        }, status=200)


@csrf_exempt
@login_required
def toggle_top_three_json(request, product_id):
    if request.method != 'POST':
        return JsonResponse({'error': 'Invalid HTTP method'}, status=400)
    
    favorite = get_object_or_404(Favorite, product__id=product_id, user=request.user)
    
    if favorite.is_top_three:
        favorite.is_top_three = False
        favorite.save()
        return JsonResponse({'success': True, 'status': 'removed_from_top_three'}, status=200)
    else:
        # Cek apakah sudah ada 3 favorit teratas
        top_three_count = Favorite.objects.filter(user=request.user, is_top_three=True).count()
        if top_three_count < 3:
            favorite.is_top_three = True
            favorite.save()
            return JsonResponse({'success': True, 'status': 'added_to_top_three'}, status=200)
        else:
            return JsonResponse({
                'success': False,
            }, status=400)

@csrf_exempt
@login_required
@require_POST
def update_note(request, product_id):
    user = request.user
    try:
        favorite = Favorite.objects.get(user=user, product_id=product_id)
        note = request.POST.get('note', '')
        favorite.note = note
        favorite.save()
        return JsonResponse({'success': True})
    except Favorite.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Favorite not found.'})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})
    
@csrf_exempt
def show_json_all_favorites(request):

    data = Favorite.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")