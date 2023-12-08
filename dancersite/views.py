from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import auth, User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator
from .models import *

# Create your views here.

def home(request):
    classes = danceClasse.objects.order_by('-id')[:4]
    events = Event.objects.order_by('-id')[:4]
    
    context = {'classes': classes, 'events': events}
    return render(request, 'index.html', context)

def classes(request):
    # Default ordering if no search query
    classes = danceClasse.objects.order_by('-id')

    search_query = request.GET.get('search')
    
    if search_query:
        classes = classes.filter(name__icontains=search_query)

    paginator = Paginator(classes, 10)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    if page.has_next():
        next_url = f'?page={page.next_page_number()}'
        if search_query:
            next_url += f'&search={search_query}'
    else:
        next_url = ''

    if page.has_previous():
        previous_url = f'?page={page.previous_page_number()}'
        if search_query:
            previous_url += f'&search={search_query}'
    else:
        previous_url = ''

    # Pass only the classes for the current page to the template
    current_classes = page.object_list
    
    # Add a message when no results are found
    if not current_classes and search_query:
        not_found_message = f'No results found for "{search_query}"'
    else:
        not_found_message = ''
    
    return render(request, 'pages/classes.html', {'classes': current_classes, 'page': page, 'next_url': next_url, 'previous_url': previous_url, 'search_query': search_query, 'not_found_message': not_found_message})

def events(request):
    events = Event.objects.all()
    paginator = Paginator(events, 10)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    search_query = request.GET.get('search')

    if search_query:
        events = Event.objects.filter(name__icontains=search_query).order_by('-id')
        paginator = Paginator(events, 12)
        page_number = request.GET.get('page', 1)
        page = paginator.get_page(page_number)

    if page.has_next():
        next_url = f'?page={page.next_page_number()}'
        if search_query:
            next_url += f'&search={search_query}'
    else:
        next_url = ''

    if page.has_previous():
        previous_url = f'?page={page.previous_page_number()}'
        if search_query:
            previous_url += f'&search={search_query}'
    else:
        previous_url = ''

    current_events = page.object_list
    
    # Add a message when no results are found
    if not current_events and search_query:
        not_found_message = f'No results found for "{search_query}"'
    else:
        not_found_message = ''
    
    return render(request, 'pages/events.html', {'events': current_events, 'page': page, 'next_url': next_url, 'previous_url': previous_url, 'search_query': search_query, 'not_found_message': not_found_message})

def about(request):
    return render(request, 'pages/about.html')

def contact(request):
    return render(request, 'pages/contacts.html')

def register(request):

    # If request is post then get user details from request
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        # Check if password and confirm password matches
        if password == confirm_password:

            # Check if username or email already exists
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already exist")
                return redirect("register")

            # Check if email already exists
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email already registered")
                return redirect("register")

            # If phone and email does not exists then create user
            else:

                # Create user
                user = User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    email=email,
                    password=password,
                )

                # Save user
                user.save()
                # login the user
                auth.login(request, user)

                # Redirect to login page
                return redirect("login")
        else:

            # If password and confirm password does not matches then show error message
            messages.info(request, "Password does not match")
            return redirect("register")
    else:

        # If request is not post then render register page
        return render(request, "register/register.html")

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)


        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, "Invalid Credential")
            return redirect("login")
    else:
        return render(request, 'register/login.html')


# Logout view to logout user
def logout(request):
    # Logout user and redirect to home page
    auth.logout(request)
    return redirect("/login")

@login_required(login_url="login")
def user_profile(request):
    
    # Get the current authenticated user
    user = request.user
    return render(request, 'user_profile.html', {"user": user})
