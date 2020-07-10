from django.urls import path
from .views import  signup,getin,userout

app_name = 'register'

urlpatterns = [
    path('',getin,name='login'),
    path('signup',signup,name='signup'),
    path('logout',userout,name='logout'),
]