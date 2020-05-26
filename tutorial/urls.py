from django.urls import path,include
from . import *
from . import views
from rest_framework.compat import path


urlpatterns = [
    path('tutorial/api/', views.tutorialApi.as_view(), name='tutorial'),
    
]
# fix shod . hasdy ? ye react bedew
