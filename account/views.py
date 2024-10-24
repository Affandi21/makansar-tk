from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# Create your views here.
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate, login
# Create your views here.


def index(request):
    return render(request, 'index.html')


def register(request):
    msg = None
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('account:login')
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
            user = form.get_user()  # Mendapatkan user yang sudah di-autentikasi oleh form
            login(request, user)  # Login user

            # Cek apakah user buyer atau seller dan redirect sesuai role-nya
            if user.seller:
                return redirect('account:sellerpage')
            elif user.buyer:
                return redirect('account:buyerpage')
        else:
            msg = 'Invalid credentials'

    return render(request, 'login.html', {'form': form, 'msg': msg})

# def login_user(request):
#     form = AuthenticationForm(request, data=request.POST or None)
#     msg = None

#     if request.method == 'POST':
#         if form.is_valid():
#             user = form.get_user()  # Dapatkan user yang valid dari form
#             login(request, user)
            
#             # Cek role user dan arahkan ke halaman yang sesuai
#             if user.role == 'buyer':
#                 return redirect('buyerpage')
#             elif user.role == 'seller':
#                 return redirect('sellerpage')
#         else:
#             msg = 'Invalid credentials'

#     return render(request, 'login.html', {'form': form, 'msg': msg})

# def login_user(request):
#     form = AuthenticationForm(request.POST or None)
#     msg = None
#     if request.method == 'POST':
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user is not None and user.buyer:
#                 login(request, user)
#                 return redirect('buyerpage')
#             elif user is not None and user.seller:
#                 login(request, user)
#                 return redirect('sellerpage')
#             else:
#                 msg= 'invalid credentials'
#         else:
#             msg = 'error validating form'
#     return render(request, 'login.html', {'form': form, 'msg': msg})


def buyer(request):
    return render(request,'buyer.html')


def seller(request):
    return render(request,'seller.html')

# def login_view(request):
#     # Logika untuk halaman login
#     return render(request, 'login.html')