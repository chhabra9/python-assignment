import json
from django.http import HttpResponse
from django.shortcuts import render
from crud_operation.models import Department,Employee
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def insertEmployee(request):
    if request.method=="POST":
        name=request.POST.get("name")
        sal=int(request.POST.get("sal"))
        dId=request.POST.get("dId")
        mId=request.POST.get("mId")

        e=Employee(name=name,salary=sal,departmentId=Department(dId),managerId=mId)
        e.save()
        return HttpResponse("bye bye")
@csrf_exempt
def getEmployee(request):
    myData=Employee.objects.all().values()
    return HttpResponse(myData)
@csrf_exempt
def updateEmployee(request,id):
    if request.method=="PUT":
        obj=Employee.objects.get(id=id)
        print(id)
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        obj.name = body['name']
        obj.salary=body['sal']
        obj.departmentId=Department(body['dId'])
        obj.managerId=body['mId']
        obj.save()
    return HttpResponse("success")
    
@csrf_exempt
def deleteEmployee(request,id):
    if request.method=="DELETE":
        object=Employee.objects.get(id=id)
        print(object)
        object.delete()
        return HttpResponse("deleted")
    return HttpResponse('Helo there')
@csrf_exempt
def insertDepartment(request):
    if request.method=="POST":
        dName=request.POST.get("dName")
        d=Department(departmentName=dName)
        d.save()
        return HttpResponse("bye bye")
@csrf_exempt
def getDepartment(request):
    myData=Department.objects.all().values()
    return HttpResponse(myData)
@csrf_exempt
def updateDepartment(request,id):
    if request.method=="PUT":
        print(id)
        obj=Department.objects.get(DepartmentId=id)
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        obj.departmentName=body['dName']
        obj.save()
        return HttpResponse("hello hello")
@csrf_exempt
def deleteDepartment(request,id):
    if request.method=="DELETE":
        object=Department.objects.get(DepartmentId=id)
        print(object)
        object.delete()
        return HttpResponse("deleted")

