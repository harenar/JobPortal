from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.http import HttpResponse
# from django.shortcuts import get_object_or_404
# from django.contrib.auth.decorators import login_required
# from django.urls import reverse

# login page authentication
# from django.contrib.auth import authenticate ,logout as auth_logout

# import models
from .models import Employee, JobPost,User_details


# create own decorators 
def login_required(view_fun):
    def wrapper(request, *args, **kwargs):
        if request.session.get('employee_id'):
            return view_fun(request, *args, **kwargs)
        else:
            return redirect('login')
    return wrapper





# Create your views here.

def welcome_page(request):
    return render(request,'welcome.html')


def employee_signup(request):
    if request.method == 'POST':
        company_name = request.POST['companyName']
        company_email = request.POST['companyEmail']
        password = request.POST['password']
        conf_password = request.POST['confPassword']
 
 

    # print(company_name,company_email,password,conf_password)
        if Employee.objects.filter(Email = company_email).exists():
            messages.error(request,"email is already taken")
            return redirect('register')
        elif password == conf_password:
            employer = Employee(Company_Name = company_name,
                                Email = company_email,
                                Password=conf_password)
            employer.save()
            return redirect('login')
        else:
            messages.error(request,"Invalid Password!")
            return redirect('register')
    return render(request,"register.html")


# login view logic
def employee_login(request):
    if 'employee_id' in request.session:
        return redirect('jobdetails')
    else:
        if request.method == 'POST':
            email = request.POST['companyEmail']
            password = request.POST['password']
            try:
                employee = Employee.objects.get(Email=email,Password = password)
                request.session['employee_id'] = employee.id
                return redirect('jobdetails')


            except Employee.DoesNotExist:
                messages.error(request,'Invalid username or password!')
                return render(request,'login.html')

    return render(request,'login.html')




# logout view
def employer_logout(request):
    del request.session['employee_id']
    messages.success(request,'logout success')
    return redirect('login')






@login_required
def job_details(request):
    employee_id = request.session.get('employee_id')
    get_data = JobPost.objects.filter(employee=employee_id)
        
    context={
       
      'jobpost':get_data,
    }
    return render(request,'jobdetails.html',context)





# recuter profile
@login_required
def Profile(request) :
    if 'employee_id' in request.session:
        get_data = User_details.objects.all()
        
        context={
       
        'user_list':get_data,
        }
    return render(request,'profile.html',context)





# job post
@login_required
def job_post(request):
    if request.method == 'POST':
        company_logo = request.FILES['image']
        title = request.POST['title']
        description = request.POST['description']
        skills = request.POST['skills']
        salary = request.POST['salary']
        exp = request.POST['exp']
        location = request.POST['location']
        # company_id = request.POST['companyname']
        
        employee_id = request.session.get('employee_id')
        company = Employee.objects.get(id=employee_id)
        
        
        post_details = JobPost(Company_logo = company_logo,
                                Title = title,
                                Description = description,
                                Skills_required = skills,
                                Job_salary = salary,
                                Experience=exp,
                                Job_location = location,
                                employee = company
                                )
        post_details.save()
        
        return redirect('jobdetails')
       
    
    return render(request,'jobpost.html',{'companyName':Employee.objects.all()})



# job update
@login_required
def job_post_edit(request, id):
    profile = JobPost.objects.get(id=id)
    if request.method == 'POST':
        profile.Title = request.POST['title']
        profile.Description = request.POST['description']
        profile.Skills_required = request.POST['skills']
        profile.Job_salary = request.POST['salary']
        profile.Experience = request.POST['exp']
        profile.Job_location = request.POST['location']
        profile.save()
        return redirect('jobdetails')
    return render(request, 'edit.html', {'data': profile})



# delete job post
@login_required
def job_post_delete(request):
    id = request.GET['id']
    delete_job_post = JobPost.objects.filter(id=id)
    delete_job_post.delete()
    return redirect('jobdetails')
    

































        
    