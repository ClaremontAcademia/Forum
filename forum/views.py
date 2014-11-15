from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	return render(request, 'base.html');

def forum(request,forum_name): pass

def thread(request,id): pass

def login(request):
	return render(request, 'login.html')

def post(request):pass