from django.shortcuts import render
from django.http import HttpResponse
from .models import Worker

def reg_entrence(request):
    return HttpResponse("Hello world")

def get_users(request):
    workers = Worker.objects.all()
    response = " "

    for worker in workers:
        response = response + "<li>" + worker.first_name + " " + worker.second_name + "</li>"

    return HttpResponse(response)