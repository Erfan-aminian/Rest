from http.client import responses

from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.http import HttpResponse
#rest_freamework
from rest_framework.decorators import api_view # for function base view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView # for cbv
from .models import Person
from .serializers import PersonSerializer, QuestionSerializer, AnswerSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .models import Question, Answer
from rest_framework import status
from permissions import IsOwnerOrReadOnly
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


class QuestionListView(APIView):
    permission_classes = [IsAuthenticated,]


    def get(self, request):
        question = Question.objects.all()
        ser_data = QuestionSerializer(instance=question, many=True)
        return Response(ser_data.data, status=status.HTTP_200_OK)


class QuestionCreateView(APIView):
    def post(self,request):
        ser_data = QuestionSerializer(data=request.POST)
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data, status=status.HTTP_201_CREATED)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionUpdateView(APIView):
    permission_classes = [IsOwnerOrReadOnly,]

    def put(self, request, pk):
        question = Question.objects.get(pk=pk)
        self.check_object_permissions(request, question)
        ser_data = QuestionSerializer(instance=question, data=request.data, partial=True)
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data, status=status.HTTP_200_OK)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionDeleteView(APIView):
    permission_classes = [IsOwnerOrReadOnly,]

    def delete (self, request, pk):
        question = Question.objects.get(pk=pk)
        question.delete()
        return Response({'message':'question deleted'})


