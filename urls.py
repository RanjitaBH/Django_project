
 
from django.urls import path
from .views import appraisal_success_view, faculty_appraisal_view, register_faculty, faculty_dashboard, appraisal_form, login_faculty, logout_faculty,appraisal_list,appraisal_detail
from django.contrib.auth import views as auth_views

from appraisal import views

urlpatterns = [
 
    path('dashboard/', faculty_dashboard, name='faculty_dashboard'),
    path('appraisal/', appraisal_form, name='appraisal_form'),
    path('register/', register_faculty, name='register_faculty'),
    path('login/', login_faculty, name='login_faculty'),
    path('logout/', logout_faculty, name='logout_faculty'),
    path('fappraisal/', faculty_appraisal_view, name='faculty_appraisal_view'),
    path('success/', appraisal_success_view, name='appraisal_success'),
    path('ss', views.appraisal_list, name='appraisal_list'),
    path('appraisald/<int:pk>/', views.appraisal_detail, name='appraisal_detail'),
   
]
