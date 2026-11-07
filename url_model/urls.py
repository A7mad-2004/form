from django.conf.urls import static
from django.urls import path

from week_5 import settings
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('form/', views.form, name='form'),
    path('form_submit/', views.form_submit, name='form_submit'),
 
    path('add_student/', views.add_student, name='add_student'),
    path('list/', views.student_list, name='student_list'),
]