from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.http import HttpResponse
# Create your views here.
class HomeView(View):
    def get(self, request):
        return HttpResponse('hello world!')

