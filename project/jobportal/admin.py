from django.contrib import admin
from . models import Employee, JobPost,User_details
# Register your models here.
admin.site.register(Employee)
admin.site.register(JobPost)
admin.site.register(User_details)

