from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout
from .models import postajob,candidate_info,Blog,Shortlist,Message


# Create your views here.
def post_job(request):
    if request.method == 'POST':
        newjob = postajob()
        newjob.job_title = request.POST['job_title']
        newjob.field = request.POST['field']
        newjob.company = request.POST['company']
        newjob.location = request.POST['location']
        newjob.desc = request.POST['desc']
        newjob.pay = request.POST['pay']

        newjob.type = request.POST['job-type']
        newjob.save()
        messages.info(request, 'thanks for posting job!!')
        return redirect('/')
    else:
        return render(request, 'dappx/new-post.html')


def find_job(request):
    if request.method == 'POST':
        type = request.POST['job-type']
        location = request.POST['location']
        nameofjob = request.POST['field']

        item = postajob.objects.filter(location=location, type=type, field=nameofjob)
        if item is not None:
           return  render(request, 'dappx/job.html', {'jobs': item})

        else:
            return render(request, 'dappx/job.html', {'jobs': item})
            messages.info(request, 'you will remain jobless forever')
    else :
        return render(request,'dappx/job-post.html')



def find_candidate(request):
    if request.method == 'POST':
        type = request.POST['job-type']
        location = request.POST['location']
        name = request.POST['field']

        item = candidate_info.objects.filter(location=location, type=type,fieldofinterest=name)
        if item is not None:
           return  render(request, 'dappx/profile.html', {'cands': item})
        else:
            messages.info(request, 'cannot find any matching results')
            return render(request, 'dappx/profile.html', {'cand': item})

    else :
        return render(request,'dappx/job-post.html')

def index(request):
    return render(request,'dappx/index.html')
def about(request):
    return render(request,'dappx/about.html')
def blog(request):
    if request.method == 'POST':
        blog1=Blog()
        blog1.title= request.POST['title']
        blog1.author=request.POST['author']
        blog1.desc=request.POST['desc']
        blog1.save()
        return redirect('/')
    else :
        blogs= Blog.objects.all()
        user1=request.user.username
        short =Shortlist.objects.filter(nameofemp=user1)
        context={
            "blogs":blogs,
            "short":short,
        }



        return render(request,'dappx/blog.html',context)



def candidates(request):
    candidate= candidate_info.objects.all()

    return render(request,'dappx/candidates.html',{'cands':candidate})
def blog_single(request):
    return render(request,'dappx/blog-single.html')
def contact(request):
    return render(request,'dappx/contact.html')

def new_post(request):
    return render(request,'dappx/new-post.html')




def register(request):
    if request.method == 'POST':
        username1 = request.POST['user_name']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        password_check = request.POST['password1']


        if password == password_check:
            if User.objects.filter(username=username1).exists():
                messages.info(request,'user already exists')
                return   redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email already exists')
                return   redirect('/register')
            else :

                user= User.objects.create_user(username=username1,password=password,email=email,first_name=first_name,last_name=last_name)
                user.save();
                cand=candidate_info()
                cand.username=username1
                cand.user=user
                cand.first_name=first_name
                cand.location=request.POST['location']
                cand.type=request.POST['job-type']
                cand.cv=request.POST['cv']
                cand.fieldofinterest=request.POST['field']
                cand.college_name=request.POST['collegename']
                if 'profile_pic' in request.FILES:
                    print('found it')
                    cand.image = request.FILES['profile_pic']
                cand.save()
                print("user created")
                return  redirect('/')

        else :
            messages.info(request, 'passsword not matching')
            return redirect('dappx:register')
    else:

        return render(request,'dappx/register.html')
def login(request):
    if request.method =='POST':
        username1= request.POST['username1']
        password1=request.POST['password']
        user = auth.authenticate(username=username1,password=password1)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else :
            messages.info(request,'invalid credentials')
            return render(request,'dappx/login.html')
    else:
        return render(request,'dappx/login.html')



def logout(request):
    auth.logout(request)
    return redirect('/')


def shortlist(request):

    if request.method == 'POST':
        short=Shortlist()
        short.nameofemp=request.POST['username']
        short.email=request.POST['email']
        short.name_of_company=request.POST['company']
        short.stipend=request.POST['stipend']
        short.save()
        return redirect('/')
    else :
        return render(request,'dappx/shortlist.html')

def message(request):
    m=Message()
    m.name=request.POST['name']
    m.email=request.POST['email']
    m.subject=request.POST['subject']
    m.mess=request.POST['message']
    m.save()
    return redirect('/')
