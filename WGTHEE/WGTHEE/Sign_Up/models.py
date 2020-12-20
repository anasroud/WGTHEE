from django.db import models
from django.contrib.auth.models import User



class Company(models.Model):
    company_name= models.CharField(max_length=255)
    Created_by = models.ForeignKey(User,related_name="Company",on_delete=models.CASCADE)
    company_creation_year=models.DateTimeField()
    field_of_company = models.CharField(max_length=255)
    
    def __str__(self):
        return self.company_name

class Teacher(models.Model):
	field_of_study=models.CharField(max_length=255)
	Created_by=models.ForeignKey(User,related_name="Teacher",on_delete=models.CASCADE)
	graduation_year=models.DateTimeField()

	def __str__(self):
		return self.field_of_study


