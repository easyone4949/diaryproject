from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name="main"),
    path('home/', views.home, name="home"), 
    path('zimonList/', views .zimonList, name="zimonList"),
    path('zimonList/<int:zimon_id>/', views.z_detail, name="z_detail"),
    path('zimonList/z_create/', views.z_create, name="z_create"),
    path('zimonList/z_new', views.z_new, name="z_new"),

    path('mumList/', views.mumList, name="mumList"),
    path('mumList/<int:mum_id>/', views.m_detail, name="m_detail"),
    path('mumList/m_create/', views.m_create, name="m_create"),
    path('mumList/m_new', views.m_new, name="m_new"),
   
]

