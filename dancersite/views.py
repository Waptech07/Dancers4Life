from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import auth, User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
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