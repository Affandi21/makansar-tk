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
                return JsonResponse({
                    "username": user.username,
                    "status": True,
                    "message": "Login sukses!"
                }, status=200)
            else:
                return JsonResponse({
                    "status": False,
                    "message": "Login gagal, akun dinonaktifkan."
                }, status=403)
        else:
            return JsonResponse({
                "status": False,
                "message": "Login gagal, periksa kembali email atau kata sandi."
            }, status=401)
    
    elif request.method == 'GET':
        # Render a simple login form for GET requests (for testing or redirection handling).
        return render(request, 'login.html', {
            'next': request.GET.get('next', '/')  # Pass the next parameter for redirection after login
        })

    else:
        return JsonResponse({
            "status": False,
            "message": "Invalid request method."
        }, status=405)
@csrf_exempt
def register(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({
                "status": False,
                "message": "Invalid JSON data."
            }, status=400)

        username = data.get('username')
        password1 = data.get('password1')
        password2 = data.get('password2')
        nama = data.get('nama')
        no_telp = data.get('no_telp')
        tanggal_lahir = data.get('tanggal_lahir')
        buyer = data.get('buyer')
        seller = data.get('seller')

        # Validate required fields
        if not all([username, password1, password2, nama, no_telp, tanggal_lahir, buyer, seller]):
            return JsonResponse({
                "status": False,
                "message": "All fields are required."
            }, status=400)

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
        user = User.objects.create_user(
            username=username,
            password=password1,
            nama=nama,
            no_telp=no_telp,
            tanggal_lahir=tanggal_lahir,
            buyer=buyer,
            seller=seller
        )
        user.save()

        return JsonResponse({
            "username": user.username,
            "status": 'success',
            "message": "User created successfully!"
        }, status=201)

    return JsonResponse({
        "status": False,
        "message": "Invalid request method."
    }, status=405)

@csrf_exempt
def logout(request):
    if not request.user.is_authenticated:
        return JsonResponse({
            "status": False,
            "message": "You are not logged in."
        }, status=401)

    try:
        username = request.user.username
        auth_logout(request)
        return JsonResponse({
            "username": username,
            "status": True,
            "message": "Logout berhasil!"
        }, status=200)
    except Exception as e:
        return JsonResponse({
            "status": False,
            "message": f"Logout gagal: {str(e)}"
        }, status=500)
