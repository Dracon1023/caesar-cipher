from django.urls import path
from .views import grettings

urllpatterns = {
    path('', grettings)    
}