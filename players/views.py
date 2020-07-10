from django.shortcuts import render
from django.views.generic.list import ListView
from .models import player
# Create your views here.


class home(ListView):
    model = player
    