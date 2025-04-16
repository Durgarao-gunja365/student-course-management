from django.db import models
import calendar
from datetime import datetime
# Create your models here.
class Admin(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=100,blank=False,unique=True)
    password=models.CharField(max_length=100,blank=False)

    class Meta:
        db_table = "admin_table"

    def __str__(self):
        return self.username

class Course(models.Model):
    id=models.AutoField(primary_key=True)
    program_choice = (
        ("B-Tech", "B-Tech"),
        ("M-Tech", "M-Tech")
    )
    program = models.CharField(max_length=50, blank=False, choices=program_choice)
    department_choices=(
        ("CSE(R)","CSE(REGULAR)"),
        ("CSE(H)","CSE(HONORS)"),
        ("CSIT","CS&IT")
                        )
    department = models.CharField(max_length=100, blank=False,choices=department_choices)
    academic_year = (
        ("2023-2024", "2023-2024"),
        ("2022-2023", "2022-2023")
    )
    academicyear = models.CharField(max_length=20, blank=False,choices=academic_year)
    semister_choice=(
        ("odd","ODD"),
        ("even","EVEN")
    )
    semester = models.CharField(max_length=10, blank=False,choices=semister_choice)
    year_choice=(
        ("1","1st"),
        ("2", "2nd"),
        ("3", "3rd"),
        ("4", "4th"),
    )
    year = models.CharField(max_length=1, blank=False, choices=year_choice)
    coursecode=models.CharField(max_length=100,blank=False)
    coursetitle=models.CharField(max_length=100,blank=False)
    ltps=models.CharField(max_length=20,blank=False)
    credits=models.FloatField(max_length=10,blank=False,null=True,default=False)

    class Meta:
        db_table ="course_table"

    def __str__(self):
        return self.coursecode

class Student(models.Model):
    id=models.AutoField(primary_key=True)
    studentid=models.BigIntegerField(blank=False,unique=True)
    fullname= models.CharField(max_length=100,blank=False)
    gender_choices = (
        ("Male", "Male"),
        ("Female", "Female"),
        ("Others", "Other"),
    )
    gender = models.CharField(max_length=10, choices=gender_choices, blank=False)

    department_choices = (
        ("CSE(R)", "CSE(REGULAR)"),
        ("CSE(H)", "CSE(HONORS)"),
        ("CSIT", "CS&IT")
    )

    department = models.CharField(max_length=100, blank=False, choices=department_choices)
    program_choice = (

        ("B-Tech", "B-Tech"),
        ("M-Tech", "M-Tech")
    )
    program = models.CharField(max_length=50, blank=False,choices=program_choice)
    semister_choice = (
        ("odd", "ODD"),
        ("even", "EVEN")
    )
    semester = models.CharField(max_length=10, blank=False, choices=semister_choice)
    year_choice = (
        ("1", "1st"),
        ("2", "2nd"),
        ("3", "3rd"),
        ("4", "4th"),
    )
    year = models.CharField(max_length=1, blank=False, choices=year_choice)
    password= models.CharField(max_length=100,blank=False,default="klu123")
    email=models.EmailField(unique=True)
    contact=models.CharField(max_length=20,blank=False)
    image=models.ImageField(upload_to='')

    class Meta:
        db_table ="student_table"

    def __str__(self):
        return str(self.studentid)



class faculty(models.Model):
    id=models.AutoField(primary_key=True)
    facultyid=models.BigIntegerField(blank=False,unique=True)
    fullname= models.CharField(max_length=100,blank=False)
    gender_choices = (
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
    )
    gender = models.CharField(max_length=10, choices=gender_choices, blank=False)

    department_choices = (
        ("CSE(R)", "CSE(REGULAR)"),
        ("CSE(H)", "CSE(HONORS)"),
        ("CSIT", "CS&IT")
    )

    department = models.CharField(max_length=100, blank=False, choices=department_choices)
    qualification = models.CharField(max_length=50, blank=False)
    designation_choice = (

        ("Professor", "PROFESSOR"),
        ("Associate Professor", "ASSOCIATE PROFESSOR")
    )
    designation = models.CharField(max_length=50, blank=False,choices=designation_choice)
    password= models.CharField(max_length=100,blank=False,default="klu123")
    email=models.EmailField(unique=True,blank=False)
    contact=models.CharField(max_length=20,blank=False)

    class Meta:
        db_table ="faculty_table"
    def __str__(self):
        return str(self.facultyid)

class FacultyCourseMapping(models.Model):
    mappingid= models.AutoField(primary_key=True)
    course= models.ForeignKey(Course,on_delete=models.CASCADE)
    faculty=models.ForeignKey(faculty,on_delete=models.CASCADE)
    component_choice=(

        ("L", "LECTURE"),
        ("T", "TUTORIAL"),
        ("P","PRACTICAL"),
        ("S", "SKILLING")
    )
    component=models.CharField(max_length=15,blank=False,choices=component_choice)
    type=models.BooleanField(blank=False,verbose_name='Main Faculty/Not')
    section=models.IntegerField(blank=False)

    class Meta:
        db_table = "facultycoursemapping"

    def __str__(self):
        return f"{self.course.coursetitle}-{self.faculty.fullname}"



# Create your models here.
class contactus(models.Model):
    fn = models.CharField(max_length=255)
    ln= models.CharField(max_length=255)
    email = models.EmailField(primary_key = True)
    mob = models.TextField(max_length=255)
    msg = models.TextField()
    class Meta:
        db_table="contactus"


