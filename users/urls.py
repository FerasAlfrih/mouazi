from django.urls import path
from .views import UsersV


urlpatterns = [
    path('login/', UsersV.login, name='login')
]
