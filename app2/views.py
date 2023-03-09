from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def virat(request):
    return HttpResponse('<h1>Virat is the Best batsman</h1>')

def rahul(request):
    return HttpResponse('<h1> Rahul is the best allrounder')
