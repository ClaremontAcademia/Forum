from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as do_login
from forum.models import User, Subforum, Thread
from random import randint
from django.core.mail import send_mail
import re

# Create your views here.
def index(request):
    #if not request.user.is_authenticated():
    #    return redirect('/login/')
	return render(request, 'index.html');

def forum(request,forum_name): 
    #if not request.user.is_authenticated():
    #    return redirect('/login/')
    current_forum = get_object_or_404(Subforum,name=forum_name)
    render(request,'forum.html',{"forum":current_forum})

def thread(request,id):
    #if not request.user.is_authenticated():
    #    return redirect('/login/')
    current_thread = get_object_or_404(Thread, id = id)
    return render(request, 'thread.html', {'thread': current_thread})

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

def post(request):
    #if not request.user.is_authenticated():
    #    return redirect('/login/')
    if request.method == 'GET':
        return render(request, 'post.html')
    elif request.method == 'POST':
        subforum = request.POST['subforum']
        tags = request.POST['tags']
        title = request.POST['title']
        content = request.POST['text']
        taglist = re.split(r', ', tags)
        thread = Thread(poster = request.user, content = content, title = title, subforum = subforum)
        thread.save()
        for tag in taglist:
            t = Tag.objects.get(name = tag)
            thread.tags.add(t)
        thread.save()
        return redirect(thread.get_url())
        

def register(request):
	email = request.POST['email']
    if validateEmail(email):
	  user = User(email = email,display_name = email)
	  user.save();
	  raw_password = randint(1000000,9999999)
      user.set_password(raw_password)
      send_mail('Welcome to Claremont Academia!','You temporary password is '+ raw_password+'.', \
    	'claremont_academia@yahoo.com',[email],fail_silently=False)
      return redirect('/login/')
    else: render(request,'login.html',{'invalidate_email':True})

def validateEmail (email):
	if re.match(r'\w+@pomona.edu$',email) ! = None:
		return True
	else return False



