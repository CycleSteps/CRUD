from django.shortcuts import render
from .models import Student

# Create your views here.
def index(request):
    return render(request,"index.html")
def insertData(request):
    if request.method == "POST":
        studentId = request.POST.get("studentId")
        studentName = request.POST.get("studentName")
        gender = request.POST.get("gender")
        studentAge = request.POST.get("studentAge")
        studentAddress = request.POST.get("studentAddress")
        print(studentId,studentName,gender,studentAge,studentAddress)
        query=Student(studentId=studentId,studentName=studentName,gender=gender,studentAge=studentAge,studentAddress=studentAddress)
        query.save()
        return render(request,"index.html",{"message":"Data inserted successfully"})
        
    return render(request,"index.html")