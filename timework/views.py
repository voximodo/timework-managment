from django.shortcuts import render
from django.http import HttpResponse
from .models import Worker, Card

def reg_entrence(request):
    return HttpResponse("Hello world")

def reg_card(request):
    if 'w' in request.GET:
        id = int(request.GET['w'])
        worker = Worker.objects.get(id=id)
        if 'c' in request.GET:
            uid = request.GET['c']
            card = Card(worker=worker, uid=uid)
            card.save()
            return HttpResponse("Pomyślnie zarejestrowano kartę.")

def get_users(request):
    workers = Worker.objects.all()
    response = " "

    for worker in workers:
        response = response + "<li>" + str(worker.id) + "." + worker.first_name + " " + worker.second_name + "</li>"

    return HttpResponse(response)