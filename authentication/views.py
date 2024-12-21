import json
from django.http import JsonResponse
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as auth_logout
from account.models import User
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render

@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            return JsonResponse({
                "status": False,
                "message": "Username and password are required."
            }, status=400)

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                response = JsonResponse({
                    "username": user.username,
                    "status": True,
                    "message": "Login sukses!"
                }, status=200)
                # Set cookie user
                response.set_cookie('user', user.username, httponly=True, samesite='Lax')
                print("Cookie set for user:", user.username)  # Log tambahan
                return response
            else:
                return JsonResponse({
                    "status": False,
                    "message": "Login gagal, akun dinonaktifkan."
                }, status=403)
        else:
            return JsonResponse({
                "status": False,
                "message": "Login gagal, periksa kembali username atau password."
            }, status=401)

    elif request.method == 'GET':
        return render(request, 'login.html', {
            'next': request.GET.get('next', '/')  # Redirection setelah login
        })

    return JsonResponse({
        "status": False,
        "message": "Invalid request method."
    }, status=405)


@csrf_exempt
def register(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data['username']
        password1 = data['password1']
        password2 = data['password2']
        nama = data['nama']
        no_telp = data['no_telp']
        tanggal_lahir = data['tanggal_lahir']
        buyer = data['buyer']
        seller = data['seller']

        # Check if the passwords match
        if password1 != password2:
            return JsonResponse({
                "status": False,
                "message": "Passwords do not match."
            }, status=400)
        
        # Check if the username is already taken
        if User.objects.filter(username=username).exists():
            return JsonResponse({
                "status": False,
                "message": "Username already exists."
            }, status=400)
        
        # Create the new user
        user = User.objects.create_user(username=username, password=password1, nama=nama, no_telp=no_telp, tanggal_lahir=tanggal_lahir, buyer=buyer, seller=seller)
        user.save()
        
        return JsonResponse({
            "username": user.username,
            "status": 'success',
            "message": "User created successfully!"
        }, status=200)
    
    else:
        return JsonResponse({
            "status": False,
            "message": "Invalid request method."
        }, status=400)
    
@csrf_exempt
def logout(request):
    username = request.user.username

    try:
        auth_logout(request)
        return JsonResponse({
            "username": username,
            "status": True,
            "message": "Logout berhasil!"
        }, status=200)
    except:
        return JsonResponse({
        "status": False,
        "message": "Logout gagal."
        }, status=401)