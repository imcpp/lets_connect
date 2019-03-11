from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,get_object_or_404
from  django.contrib import messages,auth
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.http import HttpResponse, JsonResponse
from django.utils.safestring import mark_safe
import json
from googletrans import Translator
import enchant
from django.utils import timezone
from .models import *

@login_required
def index(request):

    users = User.objects.exclude(username=request.user).exclude(is_superuser=True)

    return render(request, 'chat/index.html', {
    'users': users,
    })


@login_required
def room(request, room_name):
    use1=room_name.split("-")
    use=use1[-1]
    #print(use)
    detail=User.objects.get(username=use)
    print(detail)
    users = User.objects.exclude(username=request.user).exclude(is_superuser=True)
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(use1[0])),
        'username': mark_safe(json.dumps(request.user.username)),
        'users': users,
        'use':detail,
    })


def home(request):
    return render(request,"home.html")
def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None :
            auth.login(request,user)

            return redirect('post')
        else:
            return render(request,'landing.html',{'error':'username or password is incorrect'})
    return render(request,'post.html')

def logout(request):
    if request.method=='GET':
        auth.logout(request)
        return redirect('post')

def signup(request):
    if request.method == 'POST':
        if request.POST['password']==request.POST['password1'] :
                try:
                    user=User.objects.get(username=request.POST['username'])
                    return render(request,'landing.html',{'error':'Username already exist !! Please choose a different one :'})
                except:
                    signup_data = request.POST.dict()
                    p = User()
                    p.username = signup_data.get('username')
                    p.first_name = signup_data.get('fname')
                    p.last_name = signup_data.get('lname')
                    p.email = signup_data.get('email')
                    p.enroll_no = signup_data.get('enroll_no')
                    p.bio = signup_data.get('bio')
                    p.photo = request.FILES['photo']
                    p.set_password(signup_data.get('password'))
                    p.save()
                    #return redirect('index')
                    #user=User.objects.create_user(username=request.POST['name'],password=request.POST['password'])
                    #auth.login(request,user)
                    #return HttpResponse('<h1>Home Page<h1>')
                    #return redirect('home')
                    return render(request,'landing.html',{'error':'signup successful !!'})

        else:
            return render(request,'landing.html',{'error':'password does not match'})
    return redirect('landing')


@login_required
def search(request):
    if request.method=='GET':
        lang=request.GET['lang']
        name=request.GET['name']
        print(lang)
        if lang=="hinglish":
            translator = Translator()
            #translator = Translator()
            name=name.strip()
            s=name.split(" ")
            n=s.pop()
            d=enchant.Dict("en_us")
            #s.append("haa ")
            #name=" ".join(s)
            if(d.check(n)):#or if(translator.detect(n)!='en')
                 n=n
            else:
                 n=translator.translate(n,dest='hi').text
                 #r=r.join(s)
                 s.append(n+" ")
                 name=" ".join(s)

            name=name+ " "
            return JsonResponse({'name':name})

        elif lang=="deafult":

            return JsonResponse({'name':name})

        else:
            translator = Translator()
            name=name.strip()
            s=name.split(" ")
            n=s.pop()

            n=translator.translate(n,dest=lang).text
            s.append(n+" ")
            name=" ".join(s)



            return JsonResponse({'name':name+" "})

@login_required
def profile(request):
    users = User.objects.exclude(username=request.user).exclude(is_superuser=True)

    #user=User.objects.filter(username=request.user)
    return render(request,"profile.html",{"users":users})

def create_post(request):
    return render(request, 'create_post.html')


def create_new_post(request):
    if request.method == 'POST':
        post_data = request.POST.dict()
        print(post_data,request.user)
        p=Post()
        p.author = request.user
        p.title = post_data.get('title')
        p.text = post_data.get('text')
        p.create_date = timezone.now()
        p.save()
    return redirect('index')

def user_post(request):
    pt = Post.objects.filter(author=request.user).order_by('-create_date')
    c = len(pt)
    return render(request, 'viewpost.html', {'posts':pt, 'count':c})

def delete_post(request, pk):
    p = Post.objects.get(pk=pk)
    p.delete()
    return redirect('user_post')
def post(request):
    if request.user.is_authenticated:
        p=Post.objects.all().order_by('-create_date')
        users = User.objects.exclude(username=request.user)
        return render(request, 'post.html', {'post':p,'users':users})
    else:
        return render(request,'landing.html')


def add_comment(request, pk):
    p = Post.objects.all()
    if request.method == 'POST':
        comment_data = request.POST.dict()
        pt = get_object_or_404(Post, pk=pk)
        comm = Comment()
        comm.poet = pt
        comm.text = comment_data.get('text')
        comm.author = request.user
        comm.create_date = timezone.now()
        comm.save()
    return redirect('index')
