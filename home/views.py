from django.shortcuts import render
from bs4 import BeautifulSoup
import requests

# Create your views here.
def scarper(request):
	pass

def home(request):
	form = 'Sara'
	context={
	 'form': form,
	}
	return render(request, 'home/home.html', context)