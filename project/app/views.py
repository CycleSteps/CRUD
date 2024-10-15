from django.shortcuts import render, redirect
from .models import Student
from django.contrib import messages

# Create your views here.


def index(request):
    data=Student.objects.all()
    print(data)
    context={"data":data}
    return render(request,"index.html",context)





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
        messages.info(request,"Data inserted Successfully")
        return redirect("/")
        # return render(request,"index.html",{"message":"Data inserted successfully"})
    
def updateData(request,id):
    
    if request.method == "POST":
        
        studentId = request.POST["studentId"]
        studentName = request.POST["studentName"]
        gender = request.POST["gender"]
        studentAge = request.POST["studentAge"]
        studentAddress = request.POST["studentAddress"]
        
        edit=Student.objects.get(id=id)
        edit.studentId = studentId
        edit.studentName=studentName
        edit.gender=gender
        edit.studentAge=studentAge
        edit.studentAddress=studentAddress
        edit.save()
        messages.warning(request,"Data updated Successfully")
    
        return redirect("/")
    d=Student.objects.get(id=id)
    context={"d":d}
    return render(request,"edit.html",context)

def deleteData(request,id):
    d=Student.objects.get(id=id)
    d.delete()
    messages.error(request,"Data deleted Successfully")
    return redirect("/")
    # context={"data":data}
    # return render(request,"index.html",context)
        
    # return render(request,"index.html") 