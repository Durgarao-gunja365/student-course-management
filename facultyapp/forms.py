from django import forms
from .models import coursecontent

class AddCourseContentForm(forms.ModelForm):
    class Meta:
        model = coursecontent
        fields = "__all__"

