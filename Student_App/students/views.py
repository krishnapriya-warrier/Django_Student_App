from django.shortcuts import render,redirect
from django.views import View
from .forms import LoginForm,RegistrationForm,StudentsModelForm
from django.contrib.auth import authenticate
from django.contrib import messages
from .models import Students
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView

class LoginView(View):
    def get(self,request):
        form=LoginForm()
        return render(request,"login.html",{"form":form})
    def post(self,request):
        formdata=LoginForm(data=request.POST)
        if formdata.is_valid():
            uname=formdata.cleaned_data.get('username')
            pswd=formdata.cleaned_data.get('password')
            user=authenticate(username=uname,password=pswd)
            if user:
                login(request,user)
                messages.success(request,"You have successfully logined to the portal!!")
                return redirect('home')
            else:
                messages.error(request,"Login failed due to Invalid username or password!!!")
                return redirect('login')
        return render(request,"login.html",{"form":formdata})
class Logout_view(View):
    def get(self,request):
        logout(request)
        return redirect('login')
    
class RegView(View):
    def get(self,request):
        form=RegistrationForm()
        return render(request,"reg.html",{"form":form})
    def post(self,request):
        formdata=RegistrationForm(data=request.POST)
        if formdata.is_valid():
            formdata.save()
            messages.success(request,"You have successfully Registered in to the portal!!")
            return redirect('login')
        return render(request,"reg.html",{"form":formdata})

class LandingView(View):
    def get(self,request):
        return render(request,"landing.html")
    
class StudentView(View):
    def get(self,request):
        data=Students.objects.all()
        print(data)
        return render(request,"student_list.html",{"data":data})
class AddStudentsView(View):
    def get(self,request):
        form=StudentsModelForm()
        return render(request,"add.html",{"form":form})
    def post(self,request):
        formdata=StudentsModelForm(data=request.POST,files=request.FILES)
        if formdata.is_valid():
            formdata.save()
            messages.success(request,"The student was added successfully!!")
            return redirect("students")
        messages.error(request,"oops!!unable to load...")
        return render(request,"add.html",{"form":formdata})
    
class DeleteStudentView(View):
    def get(self,request,*args,**kwargs):
        sid=kwargs.get('id')
        print(sid)
        student=Students.objects.get(id=sid)
        student.delete()
        return redirect("students")
    
class EditStudentView(View):
    def get(self,request,**kwargs):
        sid=kwargs.get('id')
        student=Students.objects.get(id=sid)
        form=StudentsModelForm(instance=student)
        return render(request,"edit.html",{"form":form})
    
    def post(self,request,**kwargs):
        sid=kwargs.get('id')
        student=Students.objects.get(id=sid)
        formdata=StudentsModelForm(data=request.POST,files=request.FILES,instance=student)
        if formdata.is_valid():
            formdata.save()
            messages.success(request,"Details updated successfully...")
            return redirect("students")
        messages.error(request,"Failed to update!!!")
        return render(request,"edit.html",{"form":formdata})
    


            
            


