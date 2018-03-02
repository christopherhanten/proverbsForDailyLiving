from django.shortcuts import render
from .models import Proverb
from .forms import ProverbForm
from django.http import HttpResponse

def index(request):
    proverb = Proverb.objects.all()
    form = ProverbForm()
    return render(request, 'index.html', {'form':form, 'proverb':proverb})


def show(request, proverb_id):
    proverb = Proverb.objects.get(id=proverb_id)
    return render(request, 'show.html', {'proverb': proverb})

def post_proverb(request):
    form = ProverbForm(request.POST)
    if form.is_valid():
        proverb.save(commit = True)
    return HttpResponseRedirect('/')
