from django.urls import path
from.import views

urlpatterns = [
    
    path('', views.index,name='Homepage'),
    path('testing/', views.content),
    path('login/', views.login,name='loginpage'),
    path('registration/', views.registration,name='registration_page'),
    path('login/Loginsub/',views.loginsub),
    
    
    path('logout/', views.logout),

]
