from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, RequestContext
from .forms import LoginForm, SignupForm
from django.contrib.auth.models import User
from search.models import UserProfile
from django.contrib.auth import authenticate, login, logout
from django import forms

# Create your views here.


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
                login(request, user)
                # redirect to a success page
                return HttpResponseRedirect('/favorites/')
            else:
                # Return an 'invalid login' error message.
                show_login_error = True
        else:
            # Return an 'invalid login' error message.
            show_login_error = True
    # If a GET (or any other method) we'll create a blank form
    else:
        login_form = LoginForm()
        show_login_error = False
    signup_form = SignupForm()
    template = loader.get_template('login/index.html')
    context = RequestContext(request, {
        'login_form': login_form,
        'signup_form': signup_form,
        'show_login_error': show_login_error,
        'show_signup_error': False,
        'signup_tab': False
    })
    return HttpResponse(template.render(context))


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
                show_signup_error = True
        else:
            # Return an 'invalid login' error message.
            show_signup_error = True
    # If a GET (or any other method) we'll create a blank form
    else:
        signup_form = SignupForm()
        show_signup_error = False
    login_form = LoginForm()
    template = loader.get_template('login/index.html')
    context = RequestContext(request, {
        'login_form': login_form,
        'signup_form': signup_form,
        'show_login_error': False,
        'show_signup_error': show_signup_error,
        'signup_tab': True
    })
    return HttpResponse(template.render(context))


def logout_view(request):
    logout(request)
    # redirect to a success page
    return HttpResponseRedirect('/logout/success/')


def logout_success(request):
    template = loader.get_template('login/logout.html')
    context = RequestContext(request, {
    })
    return HttpResponse(template.render(context))