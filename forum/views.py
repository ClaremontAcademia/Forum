from django.shortcuts import render as oldrender, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as do_login

from forum.models import User, Subforum, Thread, Department,Class,Comment

from random import randint
from django.core.mail import send_mail
import re
import json

def render(request, template_name, dictionary = dict([])):
    dictionary.update({'departments': Department.objects.all(), 'classes': Class.objects.all()})
    return oldrender(request, template_name, dictionary)

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
        return render(request, 'post.html')
    elif request.method == 'POST':
        subforum = Subforum.objects.get(name = request.POST['course'])
        title = request.POST['title']
        content = request.POST['text']
        thread = Thread(poster = request.user, content = content, title = title, subforum = subforum)
        thread.save()
        return redirect(thread.get_url())
        

def register(request):
    email = request.POST['emailRegister']
    if validateEmail(email):
        user = User(email = email,display_name = email)
        user.save();
        raw_password = randint(1000000,9999999)
        user.set_password(str(raw_password))
        user.save()
        send_mail('Welcome to Claremont Academia!','You temporary password is '+ str(raw_password) +'.', \
        'claremont_academia@yahoo.com',[email],fail_silently=False)
        return redirect('/login/')
    else: return render(request,'loginpage.html',{'invalid_email':True})

def validateEmail (email):
	if re.match(r'^[a-zA-Z0-9_.]+@pomona.edu$',email) is not None:
		return True
	else: return False

def get_department(request, department_name):
    department = Department.objects.get(name = department_name)
    data = [(c.name, c.full_name) for c in department.class_set.all()]
    dump = json.dumps(dict(data))
    return HttpResponse(data, mimetype='application/json')

def comment(request, thread_id):
    #if not request.user.is_authenticated():
    #    return redirect('/login/')
    thread = Thread.objects.get(id = thread_id)
    c = Comment(poster = request.user, content = request.POST['content'], thread = thread)
    c.save()
    #return?
    return render(request,'thread.html',{'thread':thread})
