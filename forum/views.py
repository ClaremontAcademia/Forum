from django.shortcuts import render,redirect
from django.http import HttpResponse
from forum.models import User
from random import randint
from django.core.mail import send_mail

# Create your views here.
def index(request):
	return render(request, 'base.html');

def forum(request,forum_name): pass

def thread(request,id): pass

def login(request):
	return render(request, 'login.html')

def post(request):pass

def register(request):
	email = request.POST['email']

	user = User(email = email,display_name = email)
	user.save();
	raw_password = randint(1000000,9999999)
    user.set_password(raw_password)
    send_mail('Welcome to Claremont Academia!','You temporary password is '+ raw_password+'.', \
    	'claremont_academia@yahoo.com',[email],fail_silently=False)
    return redirect('login/')



