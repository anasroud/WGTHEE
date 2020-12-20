from blog.models import Post
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView
from .forms import SignUpForm,SignUpForm_company,SignUpForm_teacher
from django.contrib.auth.models import User
from .models import Company,Teacher
#from .functions import handle_uploaded_file 

# Create your views here.
def signup(request):
    form = SignUpForm()
    user = request.user
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            ans = form.cleaned_data.get('choices_staff')
            #to render in another page for company and teacher
 #           handle_uploaded_file(request.FILES['CV'])  
            if ans == 'company':
                return redirect('signup_company')
            elif ans == 'teacher':
                return redirect('signup_teacher')
            else:
                return redirect('home')


    return render(request,'blog/signup.html', {'form' : form})

@login_required(login_url='login')
def signup_company(request):
    # form = SignUpForm_company()
    # if request.method == 'POST':
    #     form = SignUpForm_company(request.POST)
    #     if form.is_valid():
    #         user = form.save()
    #         auth_login(request, user)
    #         return redirect('home')
    # return render(request,'blog/signup_company.html', {'form' : form})

    # user = get_object_or_404(User,pk=User.id)
    user = request.user
    form = SignUpForm_company()
    if request.method=='POST':
        form =SignUpForm_company(request.POST)
        if form.is_valid():
            Company= form.save(commit=False) 
            Company.Created_by = user  
            Company.save()
            auth_login(request, user)
            return redirect('home')
    else:
         form = SignUpForm_company()
         return render(request,'blog/signup_company.html',{'form':form})

@login_required(login_url='login')
def signup_teacher(request):
    user=request.user
    form = SignUpForm_teacher()
    if request.method == 'POST':
        form = SignUpForm_teacher(request.POST)
        if form.is_valid():
            Teacher= form.save(commit=False) 
            Teacher.Created_by = user  
            Teacher.save()
            auth_login(request, user)
            return redirect('home')
    return render(request,'blog/signup_teacher.html', {'form' : form})