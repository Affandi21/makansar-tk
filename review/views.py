from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from account.models import User
from .models import Review, Makanan
from .forms import ReviewForm
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json

def show_reviews(request, makanan_id):
    makanan = get_object_or_404(Makanan, id=makanan_id)
    reviews = makanan.review_set.all().order_by('-date_created')
    return render(request, 'show_reviews.html', {'makanan': makanan, 'reviews': reviews})

@csrf_exempt
@login_required
def tambah_review(request, makanan_id):
    makanan = get_object_or_404(Makanan, id=makanan_id)
    existing_review = Review.objects.filter(food_item=makanan, buyer=request.user).first()
    if existing_review:
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'success': False, 'error': 'Anda sudah memberikan review untuk makanan ini.'})
        else:
            messages.warning(request, 'Anda sudah memberikan review untuk makanan ini.')
            return redirect('review:show_reviews', makanan_id=makanan.id)
        
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.buyer = request.user
            review.food_item = makanan
            review.save()

            makanan.jumlah_review += 1

            total_rating = (makanan.rating_default + sum(r.rating for r in makanan.review_set.all()))
            makanan.new_rating = total_rating / (makanan.jumlah_review + 1)
            makanan.save()

            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({
                    'success': True,
                    'review': {
                        'id': review.id,
                        'rating': review.rating,
                        'comment': review.comment,
                        'buyer': review.buyer.username,
                    },
                    'new_rating': makanan.new_rating
                })
            return redirect('review:show_reviews', makanan_id=makanan.id)
    else:
        form = ReviewForm()
    return render(request, 'tambah_review.html', {'form': form, 'makanan': makanan})

@csrf_exempt
@login_required
def edit_review(request, review_id):
    review = get_object_or_404(Review, id=review_id, buyer=request.user)
    makanan = review.food_item

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            updated_review = form.save(commit=False)
            updated_review.buyer = request.user
            updated_review.food_item = makanan
            updated_review.save()

            total_rating = (makanan.rating_default + sum(r.rating for r in makanan.review_set.all()))
            makanan.new_rating = total_rating / (makanan.jumlah_review + 1)
            makanan.save()

            return redirect('review:show_reviews', makanan_id=makanan.id)
    else:
        form = ReviewForm(instance=review)
    return render(request, 'edit_review.html', {'form': form, 'review': review})

@csrf_exempt
@login_required
def hapus_review(request, review_id):
    review = get_object_or_404(Review, id=review_id, buyer=request.user)
    makanan = review.food_item

    review.delete()
    
    makanan.jumlah_review -= 1

    if makanan.jumlah_review > 0:
        total_rating = makanan.rating_default + sum(r.rating for r in makanan.review_set.all())
        makanan.new_rating = total_rating / (makanan.jumlah_review + 1)
    else:
        makanan.new_rating = makanan.rating_default

    makanan.save()
    return redirect('review:show_reviews', makanan_id=makanan.id)

@csrf_exempt
@login_required
def get_current_username(request):
    if request.method == 'GET':
        return JsonResponse({'username': request.user.username})
    return JsonResponse({'error': 'Invalid request method.'}, status=400)

@csrf_exempt
@login_required
def create_review_flutter(request, pk):
    if request.method == 'POST':
        data = json.loads(request.body)
        food_id = data.get('food_id')
        food_id = int(food_id)
        # for debugging
        print(data)
        print(request.user)
        new_review = Review.objects.create(
            buyer = request.user,
            food_item = Makanan.objects.get(pk=food_id),
            rating=int(data["rating"]),
            comment=data["comment"],
        )
        new_review.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)
    
def show_json_reviews(request, makanan_id):
    reviews = Review.objects.filter(food_item__id=makanan_id).select_related('buyer')
    review_list = []
    for review in reviews:
        review_list.append({
            'model': review._meta.model_name,
            'pk': review.pk,
            'fields': {
                'buyer': review.buyer.username,  
                'food_item': review.food_item.pk,
                'rating': review.rating,
                'comment': review.comment,
                'date_created': review.date_created.isoformat(),
            }
        })
    return JsonResponse(review_list, safe=False)
