from django.urls import path
from . import views


urlpatterns = [
    # AUTHENTICATION URL
    path('',views.welcome_page),
    path('register', views.employee_signup, name='register'),
    path('login', views.employee_login, name='login'),
    path('logout', views.employer_logout, name='emp-logout'),
    
    # ANOTHER URL LIKE(DELETE,POST,PROFILE,DETAILS)
    path('job-details', views.job_details, name='jobdetails'),
    path('rec-profile', views.Profile, name="profile"),
    path('job-post', views.job_post, name='job-post'),
    path('job-post-delete',views.job_post_delete, name="delete"),
    path('job-post-edit/<int:id>/', views.job_post_edit, name='edit'),
    
    
    
]
