from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as do_login
from forum.models import User, Subforum, Thread, Department
from random import randint
from django.core.mail import send_mail
import re
import json

# Create your views here.
def index(request):
    #if not request.user.is_authenticated():
    #    return redirect('/login/')
	return render(request, 'index.html',{'forum': None, 'threads': Thread.objects.order_by('date')[:10]});

def forum(request,forum_name): 
    #if not request.user.is_authenticated():
    #    return redirect('/login/')
    current_forum = get_object_or_404(Subforum,name=forum_name)
    render(request,'index.html',{'forum':current_forum, 'threads': current_forum.thread_set.order_by('date')[:10]})

def thread(request,id):
    #if not request.user.is_authenticated():
    #    return redirect('/login/')
    current_thread = get_object_or_404(Thread, id = id)
    return render(request, 'thread.html', {'thread': current_thread})

def login(request):
    if request.method == 'GET':
        if request.user.is_authenticated():
            return redirect('/')
        return render(request, 'loginpage.html')
    elif request.method == 'POST':
        email = request.POST['userlogin']
        password = request.POST['passlogin']
        user = authenticate(username = email, password = password)
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
        context = {'departments': Department.objects.all()}
        return render(request, 'post.html', context)
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
    else: render(request,'loginpage.html',{'invalid_email':True})

def validateEmail (email):
	if re.match(r'\w+@pomona.edu$',email) is not None:
		return True
	else: return False

def get_department(request, department_name):
    department = Department.objects.get(name = department_name)
    data = [(c.name, c.full_name) for c in department.class_set.all()]
    dump = json.dumps(dict(data))
    return HttpResponse(data, mimetype='application/json')
