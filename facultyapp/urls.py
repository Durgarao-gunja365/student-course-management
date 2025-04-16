from django.urls import path

from . import views


urlpatterns = [
path('checkfacultylogin',views.checkfacultylogin,name='checkfacultylogin'),
    path('facultyhome',views.facultyhome,name='facultyhome'),
    path('facultycourse', views.facultycourse, name='facultycourse'),
path('facultyupdatepwd',views.facultyupdatepwd,name='facultyupdatepwd'),
    path('facultychangepassword', views.facultychangepassword, name="facultychangepassword"),

    path('facultyupload', views.facultyupload, name='facultyupload'),

]