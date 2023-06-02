from django.shortcuts import render

# Create your views here.
from django.contrib import auth
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# 회원가입
def signup(request):
    if request.method == 'POST':
        if request.method == 'POST':
            if request.POST['password1'] == request.POST['password2']:
                user = User.objects.create_user(
                                                username=request.POST['username'],
                                                password=request.POST['password1'],)
        auth.login(request, user)
        return redirect('/')

        return render(request, 'signup.html')
    return render(request, 'signup.html')

# 로그인
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('login')
        else:
            return render(request, 'login.html', {'error': '아이디나 비밀번호가 올바르지 않습니다.'})
    else:
        return render(request, 'login.html')

# 로그아웃
def logout(request):
    auth.logout(request)
    return redirect('home')

# home
def home(request):
    return render(request, 'home.html')
