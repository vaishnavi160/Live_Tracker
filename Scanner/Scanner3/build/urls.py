from django.contrib import admin
from django.urls import path
from build import views


urlpatterns = {
    path('', views.index),
    path('scanner', views.scanner),
    path('scanner2', views.scanner),
    

}