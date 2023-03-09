from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def dhoni(request):
    return HttpResponse('Dhoni is the best finisher')


def rohith(request):
    return HttpResponse('Rohith is the best batsman')