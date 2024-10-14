from django.db import models

# Create your models here.
class Student(models.Model):
    studentId=models.IntegerField()
    studentName=models.CharField(max_length=25,blank=False,null=False)
    gender=models.CharField(max_length=20)
    studentAge=models.IntegerField()
    studentAddress=models.CharField(max_length=80,blank=False,null=False)
    
    def __str__(self):
        return self.studentName
    