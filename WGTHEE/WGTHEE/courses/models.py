from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Company(models.Model):
    course_name=models.CharField(max_length=500)
    course_field=models.CharField(max_length=255)
    course_duration=models.CharField(max_length=100)
    # created_year =models.
    create_by = models.ForeignKey(User,related_name="Course",on_delete=models.CASCADE)

class Teacher(models.Model):
	field_of_study=models.CharField(max_length=255)
	Created_by=models.ForeignKey(User,related_name="Teacher",on_delete=models.CASCADE)
	graduation_year=models.DateTimeField()

	def __str__(self):
		return self.field_of_study