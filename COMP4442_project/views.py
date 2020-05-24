from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello World")

def form(request):
    context ={}
    return render(request, 'COMP4442_project/form.html', context)