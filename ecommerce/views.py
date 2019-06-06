from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, HttpResponse, redirect

from .forms import ContactForm, LoginForm, RegisterForm  # import the forms.py


def home_page(request):
    # you can actually render with html tag inside python
    context = {
        "title": "This is title",
        "content": "Welcome to homepage",
    }
    # context is dictionary
    if request.user.is_authenticated:
        context["premium_content"] = "YEEEAAHH"
    return render(request, "index.html", context)


def about_page(request):
    context = {
        "title": " This is about !",
        "content": "Welcome to About"
    }
    # you can actually render with html tag inside python
    return render(request, "index.html", context)


def contact_page(request):
    # createInstance of the form
    # and then pass post request if there is or None if there isn't
    contact_form = ContactForm(request.POST or None)
    # print(contact_form.cleaned_data) this doesn't work if your form is not valid
    context = {
        "title": "Contact",
        "content": "Welcome to Contact page.",
        "form": contact_form
    }
    # you only has access to cleaned_data if form is valid !
    if contact_form.is_valid():
        print(contact_form.cleaned_data)

    # to print out what posted from form:
    # if request.method == "POST":
    #     print(request.POST)
    #     # to get value from a key in the POST queryDict its dictionary
    #     print(request.POST.get('firstname'))
    #     print(request.POST.get('lastname'))
    return render(request, "contact/contact.html", context)


def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        'form': form
    }
    print('login page check is_auth='+str(request.user.is_authenticated()))
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        print(user)
        # print(request.user.is_authenticated())
        if user is not None:
            print(request.user.is_authenticated())
            # this call backend authenticated the credentials
            login(request, user)
            return redirect("/")  # redirect to home page
            # context['form'] = LoginForm()  # clear the form by creating new inst
        else:
            # No backend authenticated the credentials
            print("Error")

    return render(request, 'auth/login.html', context)


User = get_user_model()


def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        'form': form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        new_user = User.objects.create_user(username, email, password)
        print('before check new_user')
        print(new_user)
    return render(request, 'auth/register.html', context)
