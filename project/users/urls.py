from django.urls import path
from . import views


urlpatterns = [
    # authentication urls
    path('',views.user_register,name='user-register'),
    path('user-login',views.user_login,name='user-login'),
    path('user-logout',views.logout, name='logout'),
    
    # home, profile and other urls
    path('user-home', views.user_home, name='home'),
    path('job-details-apply-form/<int:id>/', views.job_apply, name='apply')
]