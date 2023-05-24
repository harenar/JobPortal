from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate ,logout as auth_logout

# import model
from . models import User_register


# session import 
from django.contrib.sessions.backends.db import SessionStore

# import jobportal views function
# from jobportal.views import job_post_edit
# from jobportal.views import job_post

# import  jobportal model 
from jobportal.models import Employee
from jobportal.models import JobPost
from jobportal.models import User_details

# Create your views here.






# user register login
def user_register(request):
    if request.method == 'POST':
        user_name = request.POST['name']
        user_email = request.POST['email']
        password = request.POST['password']
        con_password = request.POST['conpassword']
        
        # print(user_name,user_email,password,con_password)
        
        if User_register.objects.filter(User_email = user_email).exists():
            messages.error(request,'email is already exist')
            return redirect('user-login')
        elif password != con_password:
            messages.error(request,'password dose not match')
            return redirect('user-register')
        else:
            register_details = User_register(User_name=user_name,
                                             User_email = user_email,
                                             Password = password,
                                             Con_password = con_password)
            register_details.save()
            return redirect('user-login')
    return render(request,'./user/user_register.html')



# user login logic
def user_login(request):
    if 'user_id' in request.session:
        return redirect('home')
    else:
        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']
        
        
            try:
                user_details = User_register.objects.get(User_email = email,
                                         Password = password)
                # create session variable
                request.session['user_id'] = user_details.id
                return redirect('home')
            except User_register.DoesNotExist:
                messages.error(request,'invalid Email and password')
                return redirect('user-login')
        
    return render(request,'./user/user_login.html')


def logout(request):
    print("logout success")
    auth_logout(request)
    return redirect("user-login")



# home logic
def user_home(request):
    job_list_for_all_company = JobPost.objects.all()
    
    
    return render(request,'./user/user_home.html',{'data':job_list_for_all_company})

# apply logic

def job_apply(request,id):
    title = JobPost.objects.get(id=id)
    if request.method == 'POST':
        user_name = request.POST['name']
        user_number = request.POST['number']
        user_col_uni = request.POST['college_university']
        user_resume = request.FILES['user_resume']
        
        user_id = request.session.get('user_id')
        user = User_register.objects.get(pk=user_id)
        
        user_details = User_details(User_name=user_name,
                                    User_phone_number=user_number,
                                    User_coll_univ = user_col_uni,
                                    User_resume = user_resume,
                                    jobpost = title,
                                    user = user)
        user_details.save()
        return redirect('home')
        
    
    
   
    
    return render(request,'apply.html')
