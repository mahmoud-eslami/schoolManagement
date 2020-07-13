from django.shortcuts import render
from django.contrib.auth.models import User
from Users.models import MyUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from school.methods import *
from rest_framework import status
from .models import *
import traceback
from . import serializers
from rest_framework.parsers import FileUploadParser


class getallticket(APIView):
    permission_classes=(IsAuthenticated,)
    def get (self , request):
        try:
            all_ticket = Ticket.objects.all()
            serializer = serializers.TicketSerilizer(all_ticket , many = True)
            return CustomResponse(self, status_code=200, errors=[], message="", data =serializer.data, status=status.HTTP_200_OK)
        except Exception as e :
            trace_back = traceback.format_exc()
            message = str(e) + ' ' + str(trace_back)
            return CustomResponse(self, status_code=500, errors=message, message="", data="", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ticketApi(APIView):
    permission_classes = (IsAuthenticated,)
    def get (self, request) :
 