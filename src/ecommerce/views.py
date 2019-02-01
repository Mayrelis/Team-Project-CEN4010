from django.contrib.auth import authenticate, login , get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect


from .forms import ContactForm , LoginForm, RegisterForm



def home_page(request):
    context = {
        "title":"We're working",
        "content":"Welcome to the homepage",
        #"premium_content":"YEEEAAAHHHH"
    }
    if request.user.is_authenticated():
        context["premium_content"]="YEEEAAAHHHH"
    return render(request, "home_page.html", context)

def about_page(request):
    context = {
        "title":"About page",
        "content":"Welcome to the about page"
    }
    return render(request, "home_page.html",context)

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title":"Contact Page",
        "content":"Welcome to the contact page",
        "form": contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    return render(request, "contact/view.html", context)

def login_page(request):
    login_form = LoginForm(request.POST or None)
    context = {
        "form": login_form
    }
    print("User Loged in")
    #print(request.user.is_authenticated())
    if login_form.is_valid():
        print(login_form.cleaned_data)
        username = login_form.cleaned_data.get("username")
        password = login_form.cleaned_data.get("password")
        user = authenticate(request, username = username, password = password)
        print(user)
        #print(request.user.is_authenticated())
        if user is not None:
            #print(request.user.is_authenticated())
            login(request, user)
            #context['form'] = LoginForm()
            return redirect("/login")
        else:
            print("Error")

    return render( request, "auth/login.html", context)

User = get_user_model()
def register_page(request):
    register_form = RegisterForm(request.POST or None)
    context = {
        "form": register_form
    }
    if register_form.is_valid():
        print(register_form.cleaned_data)
        email = register_form.cleaned_data.get("email")
        username = register_form.cleaned_data.get("username")
        password = register_form.cleaned_data.get("password")
        new_user = User.objects.create_user(username, email, password)
        print(new_user)
    return render( request, "auth/register.html", context)