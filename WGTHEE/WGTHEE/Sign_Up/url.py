from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls import url
urlpatterns = [
    path('signup/', views.signup , name='signup'),
    path('company_signup/', views.signup_company, name='signup_company'),
    path('teacher_signup', views.signup_teacher, name='signup_teacher'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/',auth_views.LoginView.as_view(template_name='blog/login.html'),name='login'),
]