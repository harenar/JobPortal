from django.db import models

# import model
from users.models import User_register

# Create your models here

# employee model
class Employee(models.Model):
    Company_Name = models.CharField(max_length=50)
    Email = models.EmailField()
    Password = models.CharField( max_length=50)
    
    
    def __str__(self):
        return self.Company_Name


# job post model
class JobPost(models.Model):
    Company_logo = models.ImageField(upload_to='image/', blank=True)
    Title = models.CharField(max_length=50)
    Description = models.TextField()
    Skills_required = models.CharField(max_length=50)
    Job_salary = models.IntegerField()
    Job_location = models.CharField( max_length=50)
    # new field
    Experience = models.CharField(max_length=50)
    Status = models.BooleanField(default=True)
    
    
    
    # foreign key
    employee = models.ForeignKey(Employee,  on_delete=models.CASCADE,null=True,blank=True)
    
    
    
    
    def __str__(self):
        return self.Title
    
# user_job_post apply details
class User_details(models.Model):
    User_name = models.CharField(max_length=50)
    User_phone_number = models.CharField(max_length=50)
    User_coll_univ = models.CharField(max_length=50)
    User_resume = models.FileField(upload_to='user_resume/')
    
    jobpost = models.ForeignKey(JobPost, on_delete=models.CASCADE, null=True, blank=False)
    user = models.ForeignKey(User_register,  on_delete=models.CASCADE,null=True,blank=True)
    
    def __str__(self):
        return self.User_name
    
