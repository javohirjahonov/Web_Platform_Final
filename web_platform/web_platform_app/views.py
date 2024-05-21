from django.shortcuts import render, redirect
from .models import ServiceModel, OurTeamModel, CountersModel, ContactModel, PostModel


def home(request):
    services = ServiceModel.objects.all().order_by('-created_at')
    teams = OurTeamModel.objects.all()
    counters = CountersModel.objects.all()
    posts = PostModel.objects.all().order_by('-created_at')
    context = {
        'services': services,
        'teams': teams,
        'counters': counters,
        'posts': posts
    }
    return render(request, 'index.html', context)


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')
        ContactModel.objects.create(
            name=name,
            phone=phone,
            email=email,
            message=message
        )
        return redirect('home')
    return render(request, 'contact.html')


# def services(request):
#     services = ServiceModel.objects.all()
#     team = OurTeamModel.objects.all()
#     counters = CountersModel.objects.all()
#     context = {
#         'services': services,
#         'team': team,
#         'counters': counters
#     }
#     return render(request, 'testimonial.html', context)


def posts(request):
    services = ServiceModel.objects.all()
    team = OurTeamModel.objects.all()
    counters = CountersModel.objects.all()
    context = {
        'services': services,
        'team': team,
        'counters': counters
    }
    return render(request, 'testimonial.html', context)