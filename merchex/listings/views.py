from django.http import HttpResponse
from django.shortcuts import render, redirect
from listings.models import Ticket, Review
from listings.forms import SubscribeForm
from listings.forms import LoginForm
from django.contrib.auth import login, authenticate

def base(request):
    return render(request, 'base.html')

def home(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        #if form.is_valid():
        user = authenticate(
            username=request.POST.get('username'),
            password=request.POST.get('password'),
        )
        if user is not None:
            login(request, user)
            message = f'Bonjour, {user.username}! Vous êtes connecté.'
            print(message)
            return redirect('flux')
        else:
            message = 'Identifiants invalides.'
            print(message)
    else:
        form = LoginForm()
    return render(request, 'home.html', context={'form': form})

def subscribe(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            user = form.save()
            return render(request,'home.html')
    else:
        form = SubscribeForm()
    return render(request,
            'subscribe.html',
            {'form': form})

def flux(request):
    reviews = Review.objects.all()
    tickets = Ticket.objects.all()
    return render(request, 'flux.html', {"reviews": reviews, "tickets": tickets})

def abonnements(request):
    return render(request, 'abonnements.html')

def tickets(request):
    error = False
    is_save = False
    if request.method == "POST":
        title = request.POST.get('title', None)
        print(title)
        description = request.POST.get('description', None)
        print(description)
        image = request.FILES.get('image', None)
        if title is None or description is None or len(title) < 2 or len(description) < 2:
            error = True
        print('des données ont été postées sur cette route')
        if error == False:
            t = Ticket(title = title, description = description, user = request.user)
            if image:
                t.image = image
            t.save()
            is_save = True
    return render(request, 'tickets.html', {'error': error, 'is_save': is_save})

def ticketsModify(request):
    return render(request, 'tickets-modify.html')

def critics(request):
    error = False
    is_save = False
    if request.method == "POST":
        title = request.POST.get('title', None)
        print(title)
        description = request.POST.get('description', None)
        print(description)
        image = request.FILES.get('image', None)
        if title is None or description is None or len(title) < 2 or len(description) < 2:
            error = True
        print('des données ont été postées sur cette route')
        headline = request.POST.get('headline', None)
        print(headline)
        body = request.POST.get('body', None)
        print(body)
        rating = request.POST.get('rating', None)
        print(rating)
        if headline is None or body is None or len(headline) < 2 or len(body) < 2 or rating is None:
            error = True
        print('des données ont été postées sur cette route')
        if error == False:
            t = Ticket(title = title, description = description, user = request.user)
            if image:
                t.image = image
            t.save()
            is_save = True
            r = Review(headline = headline, body = body, rating = rating, user = request.user, ticket=t)
            r.save()
            is_save = True
    return render(request, 'critics.html', {'error': error, 'is_save': is_save})

def criticsResponse(request):
    return render(request, 'critics-response.html')

def criticsModify(request):
    return render(request, 'critics-modify.html')

def yourPosts(request):
    return render(request, 'your-posts.html')

def contact(request):
    return HttpResponse('<h2>Contact us</h2> <p>Contenu<p>')