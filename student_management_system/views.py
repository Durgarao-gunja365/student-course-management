from django.http import HttpRequest, HttpResponse
from django.shortcuts import render,redirect

from adminapp.models import Student,faculty,Course,contactus
from django.core.mail import send_mail
from django.conf import settings
def demo(request):
    student_count = Student.objects.count()
    faculty_count = faculty.objects.count()
    course_count = Course.objects.count()
    context = {
        'student_count': student_count,
        'faculty_count': faculty_count,
        'course_count': course_count}
    return render(request,'sample.html',context)
def home(request):
    student_count = Student.objects.count()
    faculty_count = faculty.objects.count()
    course_count = Course.objects.count()
    context = {
        'student_count': student_count,
        'faculty_count': faculty_count,
        'course_count':course_count
    }
    return render(request,'index.html',context)
def about(request):
    return render(request,'about.html')

def logout(request):
    return render(request,'sample.html')

def explore(request):
    return render(request,'index.html')
def contact(request):
    return render(request,'contact.html')
def login(request):
    return render(request,'login.html')
def facultylogin(request):

    return render(request,'facultylogin.html')
def studentlogin(request):

    return render(request,'studentlogin.html',)

def mails(request):
    if request.method == 'POST':
        fn = request.POST.get('fn')
        ln = request.POST.get('ln')
        email = request.POST.get('email')
        mob = request.POST.get('mob')
        msg = request.POST.get('msg')
        data = contactus(fn=fn,ln=ln,email=email,mob=mob,msg=msg)
        data.save()
        send_mail(
            'message from '+fn +' '+ln, #subject
            msg, #message
            email, # from email
            ['durgaraogunja02@gmail.com','dgunja390@gmail.com'], # To mail
            fail_silently=False
        )


        msg="sent message sucessful"
        return render(request,'contact.html',{'message':msg})
    else:
        HttpResponse('Invalid request')