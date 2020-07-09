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
            serializer = serializers.TutorialSerilizer(all_ticket , many = True)
            return CustomResponse(self, status_code=200, errors=[], message="", data =serializer.data, status=status.HTTP_200_OK)
        except Exception as e :
            trace_back = traceback.format_exc()
            message = str(e) + ' ' + str(trace_back)
            return CustomResponse(self, status_code=500, errors=message, message="", data="", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class ticketApi(APIView):
    permission_classes = (IsAuthenticated,)
    def get (self, request) :
        try :
            Ticket_id = request.GET['tutorial_id']
            if Tutorial.objects.all().filter(id = tutorial_id ).exists():
                temp_tutoril = Tutorial.objects.get(id = tutorial_id)
                serializer = serializers.TutorialSerilizer(temp_tutoril)
                return CustomResponse( self , status_code=200, errors=[], message="", data =serializer.data, status=status.HTTP_200_OK)
            else :
                return CustomResponse(self, status_code=406, errors=["اموزش مورد نظر وجود ندارد!"], message="", data ="", status=status.HTTP_200_OK)
        except  Exception as e :
            trace_back = traceback.format_exc()
            message = str(e) + ' ' + str(trace_back)
            return CustomResponse(self, status_code=500, errors=message, message="", data="", status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def post(self,requset) :
        try :
            serializer = serializers.TicketSerilizer(data = requset.data )
            if  serializer.is_valid() :
                serializer.save()
                return CustomResponse(self, status_code=200, errors=[], message =("", data="", status=status.HTTP_200_OK)
            else :
                massage = serializer.errors
                return CustomResponse(self, status_code=406, errors = massage, message="", data="", status=status.HTTP_200_OK)
        except  Exception as  e:
                trace_back = traceback.format_exc()
                message = str(e) + ' ' + str(trace_back)
                return CustomResponse(self, status_code=500, errors=message, message="", data="", status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def delete(self , request):
        try:
            id = request.GET['tutorial_id']
            if Tutorial.objects.all().filter(id = id).exists():
                temp_tutorial  = Tutorial.objects.get(id = id)
                temp_tutorial.delete()
                return CustomResponse(self, status_code=200, errors="", message="اموزش با موفقیت حذف شد", data=[], status=status.HTTP_200_OK)
            else:
                return CustomResponse(self, status_code=406,message = ["اموزش با این ایدی موجود نیست !"] , errors = "", data="", status=status.HTTP_406_NOT_ACCEPTABLE)
        except Exception as e:
            trace_back = traceback.format_exc()
            message = str(e) + ' ' + str(trace_back)
            return CustomResponse(self, status_code=500, errors=message, message="", data="", status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put (self, request) :
            try :
                id = request.GET['tutorial_id']
                if Tutorial.objects.all().filter(id = id).exists():
                    temp_tutorial = Tutorial.objects.get(id = id)
                else:
                    return CustomResponse(self, status_code=406, errors=["اموزش با این ایدی موجود نیست"], message="", data="", status=status.HTTP_406_NOT_ACCEPTABLE)
                serializer = serializers.TutorialSerilizer(temp_tutorial,data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return CustomResponse(self, status_code=200, errors="", message="اموزش با موفقیت اپدیت شد", data="", status=status.HTTP_200_OK)
                else:
                    message = serializer.errors
                    return CustomResponse(self, status_code=406, errors =message, message="", data="", status=status.HTTP_200_OK)
            except Exception as e :
                trace_back = traceback.format_exc()
                message = str(e) + ' ' + str(trace_back)
                return CustomResponse(self, status_code=500, errors=message, message="", data="", status=status.HTTP_500_INTERNAL_SERVER_ERROR)