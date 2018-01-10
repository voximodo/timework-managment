from django.shortcuts import render
from django.http import HttpResponse
from .models import Worker, Card, Messages, Reader, Record

def reg_entrence(request):
    if 'c' in request.GET:

        uid = request.GET['c']
        card = Card.objects.get(uid=uid)

        id = int(request.GET['id'])
        reader = Reader.objects.get(id=id)

        type = request.GET['type']

        entrance = Record(card=card, reader=reader, type=type)
        entrance.save()

        return HttpResponse("Pomyslnie zarejestrowano.")

    return HttpResponse("Błąd!")

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

def get_messages(request):
    if 'w' in request.GET:
        id = int(request.GET['w'])
        worker = Worker.objects.get(id=id)
        mess = Messages.objects.filter(worker=worker)
        response = "Wiadomosci:</br>"
        for m in mess:
            response = response + "<li>" + m.body + " - " + str(m.date) + " - " + str(m.read) + "</li>"

        return HttpResponse(response)

def get_last_status(request):
    if 'c' in request.GET:
        uid = request.GET['c']
        card = Card.objects.get(uid=uid)
        records = Record.objects.filter(card=card).order_by('-date')
        for r in records:
            if r.type == 'workin' or r.type == 'workout' or r.type == 'break':
                return HttpResponse(r.type)

        return HttpResponse("workout")

    return HttpResponse("Blad.")