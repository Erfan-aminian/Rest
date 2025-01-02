from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.http import HttpResponse
#rest_freamework
from rest_framework.decorators import api_view # for function base view
from rest_framework.response import Response
from rest_framework.views import APIView # for cbv

# Create your views here.

'''function base views code'''
#@api_view(['GET', 'POST', 'PUT'])
#def Home (request):
    #return Response({'name':'amir'})

''' Class base View '''
class Home(APIView):
    def get(self, request):
        return Response({'name': 'jack'})

    def post(self, request):
        name = request.data['name']
        return Response({'name': name})
