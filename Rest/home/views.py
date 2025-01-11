from http.client import responses

from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.http import HttpResponse
#rest_freamework
from rest_framework.decorators import api_view # for function base view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView # for cbv
from .models import Person
from .serializers import PersonSerializer, QuestionSerializer, AnswerSerializer
from rest_framework.permissions import IsAdminUser
from .models import Question, Answer
from rest_framework import status
# Create your views here.

'''function base views code'''
#@api_view(['GET', 'POST', 'PUT'])
#def Home (request):
    #return Response({'name':'amir'})

''' Class base View '''
class Home(APIView):
    permission_classes = [IsAdminUser,]

    def get(self, request):
        persons = Person.objects.all()
        ser_data = PersonSerializer(instance=persons, many=True)
        return Response(data=ser_data.data)

    def post(self, request):
        pass


class QuestionView(APIView):

    def get(self, request):
        question = Question.objects.all()
        ser_data = QuestionSerializer(instance=question, many=True)
        return Response(ser_data.data, status=HTTP_200_OK)

