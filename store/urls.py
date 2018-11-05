from django.urls import path
from django.contrib import admin
from store.models import Music
from django.urls import include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('store/', views.store, name="store"),
    path('store/<genre>/', views.genre.as_view()),
    path('store/<name>/play/', views.player),
    path('admin/', include(admin.site.urls), name="admin"),
]