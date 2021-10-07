
from django.conf.urls import url
from django.urls import path
from dappx import views

app_name = 'dappx'


urlpatterns=[
path('',views.index,name='home'),



path('candidates.html',views.candidates,name='candidates'),

    path('about.html',views.about,name='about'),
    path('contact.html',views.contact,name='contact'),
    path('blog.html',views.blog,name='blog'),
    path('new-post',views.post_job,name='new-post'),
    path('job-post.html',views.find_job,name='job-post'),
path('cand-post',views.find_candidate,name='cand-post'),
    path('blog-single.html',views.blog_single,name='blog-single'),
path('logout',views.logout,name='logout'),
path('login',views.login,name='login'),
path('register',views.register,name='register'),
path('shortlist',views.shortlist,name='shortlist'),
path('message',views.message,name='message'),
]
