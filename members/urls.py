from django.urls import path
from . import views

# create a list
urlpatterns = [
    path('members/', views.members, name = 'members'),
    
]