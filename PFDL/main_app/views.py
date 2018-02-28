# main_app/views.py
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html', {'proverbs': proverbs})


class Proverb:
    def __init__(self, date, proverb):
        self.date = date
        self.proverb = proverb
proverbs = [
    Proverb ('1-Jan', "The generous man enriches himself by giving, whilst the miser hoards himself poor."),
	Proverb ('2-Jan', "A slip of the foot you may soon recover, but a slip 	of the tongue you may never get over."),
	Proverb ('3-Jan', "The greatest wealth is contentment with a little."),
]

# Create your views here.
