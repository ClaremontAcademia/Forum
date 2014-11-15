from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as do_login

# Create your views here.
def index(request):
	return render(request, 'base.html');

def forum(request,forum_name): pass

def thread(request,id): pass

def login(request):
    if request.method == 'GET':
        if request.user.is_authenticated():
            return redirect('/')
    	return render(request, 'login.html')
    elif request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email = email, password = password)
        if user:
            do_login(request, user)
            return redirect('/')
        else:
            context = {'invalid_login': True}
            return render(request, 'loginpage.html', context)

def post(request):pass