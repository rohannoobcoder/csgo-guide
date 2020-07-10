from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import Profile
from django.contrib.auth.decorators import login_required
# Create your views here.




@login_required
def userout(request):
    logout(request)
    return redirect('register:login')

    return render(request,'home.html')


def getin(request):
    if request.method=="POST":
        username= request.POST.get("uname")
        password = request.POST.get("password")
        user = authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('players:home')
        
        else:
            return render(request,'login.html',{'error':'Username and Password not matching! Try again!'})
    
    else:
        return render(request,'login.html')






def signup(request):
    if request.method == "POST":
        fname = request.POST.get('fname') 
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        image = request.POST.get('image')
        bod = request.POST.get('bod')
        uname = request.POST.get('uname')

        if password1 == password2 :
            try:
                user= User.objects.get(username=uname)
                return render(request,'form.html',{'error':"This Username is already taken!"})
            except User.DoesNotExist:
                user = User.objects.create_user(username=uname,password=password1,first_name=fname,last_name=lname,email=email)
                user.save()
                profile = Profile(profile_pic=image,bday=bod,user=user)
                profile.save()
                login(request,user)
                return redirect('players:home')
        else:
            return render(request,'form.html',{'error':'Your Password did not matched!'})
    
        
    
    return render(request,'form.html')