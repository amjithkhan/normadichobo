from django.urls import path
from.import views

urlpatterns = [
    
    path('', views.index),
    path('testing/', views.content),
    path('login/', views.login),
    path('registration/', views.registration),
    path('login/Loginsub/',views.loginsub),
    path('Loginsub/',views.loginsub),
    path('registration/registersub',views.registersub),

]
