from django.urls import path
from .views import home, contact

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    # path('services/', services, name='services'),
    # path('posts/', posts, name='posts'),
]
