from django.urls import path
from .views import AuthenticatedUser, users, register, login, logout

urlpatterns = [
    path('users', users),
    path('register', register),
    path('login', login),
    path('login', logout),
    path('user', AuthenticatedUser.as_view())
]