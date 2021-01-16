from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name="login" ),
    path('home/', views.home, name="home" ),
    path('insert/', views.listng, name="insert" ),
]