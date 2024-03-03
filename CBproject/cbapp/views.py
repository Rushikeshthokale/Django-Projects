from django.shortcuts import render,HttpResponse,redirect
from django.views.generic import View
from cbapp.models import Student
# Create your views here.
class MyView(View):
    def get(self,request):
        # return HttpResponse("Welcome to CB views!!")
        return render(request,'template1.html')
    def post(self,request):
        pass

class AddStudent(View):
    def get(self,request):
        #Display the empty form to user
        return render(request,'addstudent.html')
    
    def post(self,request):
        #Process the form
        #retreive data
        #and store data in database
        n=request.POST['name']
        b=request.POST['branch']
        p=request.POST['percent']
        stu=Student.objects.create(name=n,branch=b,perc=p)
        stu.save()
        # return HttpResponse("STudent added !!!")
        return redirect('/')

class StudentList(View):
    def get(self,request):
        data=Student.objects.all()
        context={'students':data}
        return render(request,'studentlist.html',context)

class DeleteStudent(View):
    def get(self,request,sid):
        stu=Student.objects.get(id=sid)
        stu.delete()
        return redirect('/')
    
class UpdateStudent(View):
    def get(self,request,sid):
        stu=Student.objects.get(id=sid)
        context={'stu':stu}
        return render(request,'updatestudent.html',context)
    def post(self,request,sid):
        stu=Student.objects.filter(id=sid)
        n=request.POST['name']
        b=request.POST['branch']
        p=request.POST['percent']
        stu.update(name=n,branch=b,perc=p)
        return redirect('/')
