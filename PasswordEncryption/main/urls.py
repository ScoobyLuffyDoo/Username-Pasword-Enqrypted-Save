from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('v2/', views.v2, name='view2'),
    path('login/', views.login, name='login'),
    ]