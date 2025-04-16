from django.db import models
from adminapp.models import faculty,Course



# Create your models here.
class coursecontent(models.Model):
    id = models.AutoField(primary_key=True)
    faculty=models.ForeignKey(faculty,blank=False,on_delete=models.CASCADE)
    course=models.ForeignKey(Course,blank=False,on_delete=models.CASCADE)
    description=models.TextField(max_length=1000,blank=False)
    link=models.CharField(max_length=100,blank=False)
    contentimage=models.FileField(blank=False,upload_to='coursecontent')

    class Meta:
        db_table="coursecontent_table"