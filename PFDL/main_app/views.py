# main_app/views.py
#main_app/views.py
from django.shortcuts import render
from .models import Proverbs

def index(request):
    proverb = Proverbs.objects.all()
    return render(request, 'index.html', {'proverbs':proverb})

def show(request, proverb_id):
    proverb = Proverb.objects.get(id=proverb_id)
    return render(request, 'show.html', {'proverb': proverb}) 
