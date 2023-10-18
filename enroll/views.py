from django.shortcuts import render , HttpResponseRedirect
from django.http import HttpResponse 
from .forms import StudentRegistration
from .models import User

def add_show(request):
  
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            fm = StudentRegistration()
        
    else:
        fm = StudentRegistration()
       
        
    stud = User.objects.all()

    return render(request, 'enroll/addandshow.html',{'form':fm,'stu':stud})


def update_data(request,id):
    if request.method == 'POST':
        pi= User.objects.get(pk=id)
        fm= StudentRegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            fm = StudentRegistration() 
    else:
        pi= User.objects.get(pk=id)
        
        fm= StudentRegistration(instance=pi) 

    return render(request, 'enroll/updatestudent.html', {'form':fm,})

def delete_data(request, id):
    if request.method =='POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
    

