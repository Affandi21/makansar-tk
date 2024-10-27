# favorite/context_processors.py

from .models import Favorite

def favorite_product_ids(request):
    if request.user.is_authenticated:
        favorite_ids = set(Favorite.objects.filter(user=request.user).values_list('product_id', flat=True))
    else:
        favorite_ids = set()
    
    return {'favorite_product_ids': favorite_ids}
