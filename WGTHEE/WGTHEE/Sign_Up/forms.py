from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models
from django.forms.widgets import DateInput
from .models import Company,Teacher
#from .functions import handle_uploaded_file
Staff_CHOICES= [
    ('student', 'Students'),
    ('teacher', 'Teachers'),
    ('company', 'Companies'),
    ]
YEARS= [x for x in range(1940,2020)]

class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=255,required=True,widget=forms.EmailInput())
    choices_staff= forms.CharField(label='Who are you?', widget=forms.Select(choices=Staff_CHOICES)) 
    #firstname = forms.CharField(max_length=255)
    #lastname = forms.CharField(max_length=255)
    class Meta:
        model=User
        fields = {'first_name','last_name','username','email','password1','password2','choices_staff'}
    field_order = ['first_name','last_name','username','email','password1','password2','choices_staff']

class SignUpForm_company(forms.ModelForm):
    company_name=forms.CharField(max_length=255,required=True,label='Company name')
    company_creation_year=forms.DateField(label='when did the company start',widget=forms.SelectDateWidget(years=YEARS))
    #id=models.ForeignKey(SignUpForm, related_name='id',on_delete=models.CASCADE)
    field_of_company=forms.CharField(max_length=255,required=True,label='Field of company')
    date_of_birth= forms.DateField(label='What is your birth date?', initial="1998-05-08", widget=forms.SelectDateWidget(years=YEARS))
    class Meta:
        model= Company
        fields = {'company_name','field_of_company','company_creation_year','date_of_birth'}
    field_order = ['company_name','field_of_company','company_creation_year','date_of_birth']

class SignUpForm_teacher(forms.ModelForm):
    #company_creation_year=forms.DateField(label='when did the company start',widget=forms.SelectDateWidget(years=YEARS))
    tid = models.ForeignKey(User,related_name='tid',on_delete=models.CASCADE)
    field_of_study=forms.CharField(max_length=255,required=True,label='Field of Study')
    graduation_year=forms.DateField(label='when did you graduate?',widget=forms.SelectDateWidget(years=YEARS))
    date_of_birth= forms.DateField(label='What is your birth date?', initial="1998-05-08", widget=forms.SelectDateWidget(years=YEARS))
    class Meta:
        model=Teacher
        fields = {'field_of_study','graduation_year','date_of_birth'}
    field_order = ['field_of_study','graduation_year','date_of_birth']