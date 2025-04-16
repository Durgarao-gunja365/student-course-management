from django import forms
from .models import faculty,Student,FacultyCourseMapping

class addFacultyForm(forms.ModelForm):
    class Meta:
        model=faculty
        fields="__all__"
        exclude={"password"}
        labels={"facultyid":"Enter Faculty Id"}

class addStudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields="__all__"
        exclude={"password"}
        labels={"studentid":"Enter Student Id"}


class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields="__all__"

class AddFacultyCourseMapping(forms.ModelForm):
    class Meta:
        model=FacultyCourseMapping
        fields="__all__"

class facultyform(forms.ModelForm):
    class meta:
        model=faculty
        fields="__all__"