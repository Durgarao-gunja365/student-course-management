from django.db.models import Q
from django.shortcuts import render

from adminapp.models import Student,Course

from facultyapp.models import coursecontent
import razorpay
from .models import feepayment
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def studenthome(request):
    sname = request.session['sname']
    student=Student.objects.get(studentid=sname)
    return render(request,'studenthome.html',{'studentname':sname,'student':student})

def checkstudentlogin(request):
    studentname = request.POST.get('uname')
    studentpwd = request.POST.get('pwd')
    flag = Student.objects.filter(Q(studentid=studentname) & Q(password=studentpwd))

    print(flag)

    if flag:
        print("login successful")
        request.session['sname']=studentname
        student = Student.objects.get(studentid=studentname)
        return render(request,'studenthome.html',{'studentname':studentname,'student':student})
    else:
        msg='Username or Password Wrong'
        return render(request,'studentlogin.html',{'msg':msg})



def studentchangepassword(request):
    sname = request.session['sname']
    return render(request,'studentchangepassword.html',{'studentname':sname})
def studentupdatepwd(request):
    sname = request.session['sname']
    opwd=request.POST['opwd']
    npwd=request.POST['npwd']
    flag=Student.objects.filter(Q(studentid=sname)& Q(password=opwd))
    if flag:
        print("password is correct")
        Student.objects.filter(studentid=sname).update(password=npwd)
        print("update successfully.....")
        msg="student Password update successfully....."
    else:
        print("wrong password")
        msg = "Password update Failed....."
    return render(request,'studentchangepassword.html',{'msg':msg,'studentname':sname})

def studentcourses(request):
    sname = request.session['sname']
    return render(request,'studentcourses.html',{'studentname':sname})

def dispalycoursecontent(request):
    sname = request.session['sname']
    content=coursecontent.objects.all()
    return render(request, 'displaycoursecontent.html', {'studentname': sname,'coursecontent':content})

def displaystudentcourses(request):
    sname = request.session['sname']
    ay=request.POST['ay']
    sem= request.POST['sem']
    courses=Course.objects.filter(Q(academicyear=ay)&Q(semester=sem))

    return render(request,'displaystudentcourses.html',{'courses':courses,'studentname':sname})

def razor_index(request):
    sname = request.session['sname']
    student = Student.objects.get(studentid=sname)
    if request.method == "POST":
        stid = request.POST.get('stid')
        name = request.POST.get('name')
        program = request.POST.get('program')
        dept = request.POST.get('dept')
        year = request.POST.get('year')
        contact = request.POST.get('contact')
        amount = int(request.POST.get('amount'))*100
        purpose = request.POST.get('purpose')
        print(amount)
        client =razorpay.Client(auth=('rzp_test_SDRnWRhH19hudM','N6wxwJ9qwo8eyfYI35CoMupn'))
        payment = client.order.create({'amount':amount,'currency':'INR','payment_capture':'1'})
        print(payment)
        paymentlist=feepayment(stid=stid,name=name,program=program,dept=dept,year=year,contact=contact,amount=amount,purpose=purpose,payment_id=payment['id'])
        paymentlist.save()
        return render(request, 'razorpay_home.html', {'studentname': sname, 'student': student,'payment':payment})
    return render(request, 'razorpay_home.html', { 'studentname': sname,'student':student})

@csrf_exempt
def success(request):

    if request.method=="POST":
        a=request.POST
        order_id=''
        for key, val in a.items():
            if key =='razorpay_order_id':
                order_id = val
                break
        user = feepayment.objects.filter(payment_id=order_id).first()
        user.paid=True
        user.save()
        print(order_id)


    return render(request, 'successpage.html')