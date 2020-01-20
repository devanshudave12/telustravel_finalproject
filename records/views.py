from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.db import IntegrityError


# Create your views here.
# defined the variable login
def login(request):
    if request.method == 'POST':   # if the request is post then follow this
        username = request.POST['username']    # username set to post
        password = request.POST['password']    # password set to post
        # using the django authentic system
        user = auth.authenticate(request, username=username, password=password)

        if user is not None:     # if the user is not none then follow this
            auth.login(request, user)      # set request to user
            return redirect('/')   # return to the home page
        else:
            # else password or anything is wrong then print not valid
            messages.info(request, "NOT VALID ")
            return redirect('login')   # return the user to login page

    else:
        return render(request, 'login.html')   # else to login html page


def register(request):
    # for register if request by user is post then follow this
    if request.method == 'POST':
        first_name = request.POST['first_name']   # firstname set to post
        last_name = request.POST['last_name']     # last name  set to post
        username = request.POST['username']       # user name  set to post
        password1 = request.POST['password1']     # password set to post
        # password 2 confirm the passsword  set to post
        password2 = request.POST['password2']
        email = request.POST['email']              # email set to post

        # if password matches to confirm password then follow this
        if password1 == password2:
            # if username already exists in database
            if User.objects.filter(username=username).exists():
                # then print user already taken
                messages.info(request, 'User already taken')
                return redirect('register')      # return to register page
                # if email already exists then do this
            elif User.objects.filter(email=email).exists():
                # print this
                messages.info(request, 'Email id already in the system')
                return redirect('register')   # return register page
            else:
                user = User.objects.create_user(username=username,
                                                password=password1,
                                                email=email,
                                                first_name=first_name,
                                                last_name=last_name)
                user.save()   # save it
                print("user created")
                return redirect('/')   # redirect it to home
        else:
            print('password not matching')  # print this
            return redirect('register')   # return user to register
            # return redirect( "/" )
    else:
        return render(request, 'register.html')   # else everything print this


def logout(request):
    auth.logout(request)  # for logout
    return redirect('/')  # return the user to home page
