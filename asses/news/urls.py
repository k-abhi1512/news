from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name="login" ),
    path('', views.home, name="home" ),
    path('insert/', views.listng, name="insert" ),
    path('logout', views.logout, name="logout")
]