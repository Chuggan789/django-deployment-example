from django.shortcuts import render
from basic_app.forms import UserProfileInfoForm,UserForm
from basic_app.models import UserProfileInfo

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def profile_page(request):
    user_info = UserProfileInfo.objects.all()
    return render(request,'basic_app/profile_page.html',
                  {'user_info':user_info})

def index(request):
    return render(request, 'basic_app/index.html')

@login_required
def special(request):
    return HttpResponse("you are logged in!")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):

    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request,'basic_app/registration.html',
                            {'user_form':user_form,
                             'profile_form':profile_form,
                             'registered':registered})

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active: 
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            
            else:
                return HttpResponse("Account not active!!")
        
        else:
            print("Someone tried to login and failed")
            print("Username: {} and \nPassword: {}"
                  .format(username,password))

    else:
        return render(request,'basic_app/user_login.html',{})















