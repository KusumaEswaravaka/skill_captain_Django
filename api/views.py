from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.

def welcome(request):
    return JsonResponse({
        "message": "Welcome to the Movie Review API!"
    })