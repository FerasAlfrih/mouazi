from django.urls import path
from . import views


urlpatterns = [
    path('', views.bible, name='bible'),
    path('bible/', views.bible, name='bible'),
    #

]
