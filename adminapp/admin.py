from django.contrib import admin
from .models import Admin,Student,faculty,Course,FacultyCourseMapping
# Register your models here.

admin.site.register(Admin)
admin.site.register(Student)
admin.site.register(faculty)
admin.site.register(Course)
admin.site.register(FacultyCourseMapping)