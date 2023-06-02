from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *
import accounts

urlpatterns = [
    path('signup', accounts.views.signup, name='signup'),
    path('login', accounts.views.login, name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('home', accounts.views.home, name='home'),
]