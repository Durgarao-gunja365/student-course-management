from . import views
from django.urls import path

urlpatterns = [
    path('checkstudentlogin', views.checkstudentlogin, name='checkstudentlogin'),
    path('studenthome', views.studenthome, name='studenthome'),
    path('studentupdatepwd',views.studentupdatepwd,name='studentupdatepwd'),
    path('studentchangepassword', views.studentchangepassword, name="studentchangepassword"),
    path('studentcourses', views.studentcourses, name='studentcourses'),
    path('displaystudentcourses', views.displaystudentcourses, name='displaystudentcourses'),
path('dispalycoursecontent', views.dispalycoursecontent, name='dispalycoursecontent'),
    path('razor_index',views.razor_index,name='razor_index'),
    path('success',views.success,name='success'),

]