
from django.urls import path, include

from . import views

urlpatterns = [
    path('',views.adminhome,name="adminhome"),
    path('adminlogout', views.adminlogout, name="adminlogout"),
    path('adminlogin',views.adminlogin,name='adminlogin'),
    path('changepassword', views.changepassword, name="changepassword"),
path('adminupdatepwd',views.adminupdatepwd,name='adminupdatepwd'),

    path('adminstudent', views.adminstudent, name='adminstudent'),
    path('viewstudent',views.viewstudent,name='viewstudent'),
    path('addstudent', views.addstudent, name='addstudent'),
    path('deletestudent', views.deletestudent, name='deletestudent'),
    path('studentdelete/<int:studentid>', views.studentdelete, name='studentdelete'),
    path('updatestudent', views.updatestudent, name='updatestudent'),

path('studentupdate/<int:studentid>/', views.studentupdate, name='studentupdate'),
    #path('checkstudentlogin',views.checkstudentlogin,name='checkstudentlogin'),
   #path('studenthome', views.studenthome, name='studenthome'),



    path('adminfaculty', views.adminfaculty, name='adminfaculty'),
    path('viewfaculty',views.viewfaculty,name='viewfaculty'),
    path('addfaculty', views.addfaculty, name='addfaculty'),
    path('deletefaculty', views.deletefaculty, name='deletefaculty'),
    path('facultydelete/<int:facultyid>', views.facultydelete, name='facultydelete'),
    path('updatefaculty', views.updatefaculty, name='updatefaculty'),
   # path('checkfacultylogin',views.checkfacultylogin,name='checkfacultylogin'),
    path('faculty_update/<int:facultyid>/', views.faculty_update, name='faculty_update'),

    path('viewcourses',views.viewcourses,name='viewcourses'),
    path('admincourse', views.admincourse, name='admincourse'),
    path('addcourse', views.addcourse, name='addcourse'),
    path('insertcourse',views.insertcourse,name='insertcourse'),
    path('deletecourse', views.deletecourse, name='deletecourse'),
    path('coursedelete/<int:cid>', views.coursedelete, name='coursedelete'),
    path('updatecourse',views.updatecourse,name='updatecourse'),
    path('courseupdate/<int:cid>', views.courseupdate, name='courseupdate'),
    path('updatecourse_by_id', views.updatecourse_by_id, name='updatecourse_by_id'),

    path('facultycoursemapping', views.facultycoursemapping, name="facultycoursemapping"),
    path('add_faculty_course_mapping', views.add_faculty_course_mapping, name='add_faculty_course_mapping'),

]
