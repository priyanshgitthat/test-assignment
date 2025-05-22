from django.urls import path
from . import views

urlpatterns = [
    path('doctor/create/', views.create_blog, name='create_blog'),
    path('doctor/blogs/', views.doctor_blogs, name='doctor_blogs'),
    path('patient/blogs/', views.patient_blog_list, name='patient_blog_list'),
]