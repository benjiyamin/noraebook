from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, RequestContext
from .forms import LoginForm, SignupForm
from django.contrib.auth.models import User
from search.models import UserProfile
from django.contrib.auth import authenticate, login, logout
from django import forms

# Create your views here.

def index(request, login_form=LoginForm(), signup_form=SignupForm()):
    template = loader.get_template('login/index.html')
    context = RequestContext(request, {
        'login_form': login_form,
        'signup_form': signup_form,
    })
    return HttpResponse(template.render(context))


def login_view(request):
    # If this is a POST request we need to process the form data
    if request.method == "POST":
        # Create a form instance and populate it with data from the request:
        login_form = LoginForm(request.POST)
        # Check whether it's valid:
        if login_form.is_valid():
            # Process the data in form.cleaned_data as required
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    # redirect to a success page
                    return HttpResponseRedirect('/favorites/')
                else:
                    # return to a 'disabled account error message
                    return HttpResponseRedirect('/diabled/')
            else:
                # Return an 'invalid login' error message.
                return HttpResponseRedirect('/login/invalid-login/')
        else:
            # Return an 'invalid login' error message.
            print(login_form.errors)
            #return HttpResponseRedirect('/login/invalid-login/')

    # If a GET (or any other method) we'll create a blank form
    else:
        login_form = LoginForm()
    signup_form = SignupForm()
    index(request, login_form, signup_form)


def signup_view(request):
    # If this is a POST request we need to process the form data
    if request.method == "POST":
        signup_form = SignupForm(request.POST)
        if signup_form.is_valid():
            # Process the data in form.cleaned_data as required
            username = signup_form.cleaned_data['username']
            email = signup_form.cleaned_data['email']
            password = signup_form.cleaned_data['password']
            confirm = signup_form.cleaned_data['confirm']
            if password == confirm:
                new_user = User.objects.create_user(username=username,
                                                    email=email,
                                                    password=password)
                new_user.save()
                new_user_profile = UserProfile(user=new_user)
                new_user_profile.save()
                user = authenticate(username=username, password=password)
                login(request, user)
                # redirect to a new URL:
                return HttpResponseRedirect('/favorites/')
            else:
                return HttpResponseRedirect('/login/')
        else:
            # Return an 'invalid login' error message.
            return HttpResponseRedirect('/invalid/')
    # If a GET (or any other method) we'll create a blank form
    else:
        signup_form = SignupForm()
    login_form = LoginForm()
    index(request, login_form, signup_form)


def logout_view(request):
    logout(request)
    # redirect to a success page
    return HttpResponseRedirect('/logout/success/')


def logout_success(request):
    template = loader.get_template('login/logout.html')
    context = RequestContext(request, {
    })
    return HttpResponse(template.render(context))