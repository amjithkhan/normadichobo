from django.urls import path
from.import views

urlpatterns = [
    
    path('', views.index,name='homepage'),
    path('testing/', views.content),
    path('login/', views.login,name='loginpage'),
    path('registration/', views.registration,name='registration_page'),
    path('login/Loginsub/',views.loginsub),
    path('Loginsub/',views.loginsub),
    path('registration/registersub',views.registersub),

]
