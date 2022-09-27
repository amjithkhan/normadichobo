from django.urls import path

from home.views import comment
from . import views


urlpatterns=[

    path('',views.details,name="detail_page"),
    path('cmt/',views.commenting,name="comment"),
    
    ]