from django.urls import path,include
from . import *
from . import views
from rest_framework.compat import path


urlpatterns = [
    path('ticket/api/', views.ticketApi.as_view(), name='ticket'),
    path('tutorial/api/all_massage/', views.getallticket.as_view() , name = 'all_ticket'),
]
