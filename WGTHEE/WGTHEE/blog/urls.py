from django.urls import path
from django.conf.urls import include, url
from . import views

urlpatterns = [
    path('register/', views.registerPage, name="register"),
	path('logout/', views.logoutUser, name="logout"),
    path('', views.home, name='home'),
    path('posts', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('courses/', views.courses, name='courses'),
    path('dashboard/',views.dashboard, name="dashboard"),
]
