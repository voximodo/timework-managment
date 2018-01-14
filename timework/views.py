from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.views.generic import DetailView

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
        #response = response + "<li>" + str(worker.id) + "." + worker.first_name + " " + worker.second_name + "</li>"
        response = response + str(worker.id) + "-" + worker.first_name + " " + worker.second_name + "</br>"

    return HttpResponse(response)

def get_messages(request):
    if 'c' in request.GET:
        uid = request.GET['c']
        if Card.objects.filter(uid=uid).exists():
            card = Card.objects.get(uid=uid)
            worker = card.worker
            mess = Messages.objects.filter(worker=worker)
            response = "Wiadomosci:</br>"
            for m in mess:
                response = response + "<li>" + m.body + " - " + str(m.date) + " - " + str(m.read) + "</li>"

            return HttpResponse(response)

def get_l_messages(request):
    if 'c' in request.GET:
        uid = request.GET['c']
        if Card.objects.filter(uid=uid).exists():
            card = Card.objects.get(uid=uid)
            worker = card.worker
            mess = Messages.objects.filter(worker=worker)
            response = ""
            for m in mess:
                if m.read == 0:
                    response = response + "<li>" + m.body + " - " + str(m.date.strftime("%Y-%m-%d %H:%M:%S")) + "</li>"
                    m.read = 1
                    m.save()

            return HttpResponse(response)

def get_last_status(request):
    if 'c' in request.GET:
        uid = request.GET['c']
        if Card.objects.filter(uid=uid).exists():
            card = Card.objects.get(uid=uid)
            records = Record.objects.filter(card=card).order_by('-date')
            for r in records:
                if r.type == 'workin' or r.type == 'workout' or r.type == 'break':
                    return HttpResponse(card.worker.first_name + " " + card.worker.second_name + "-" + r.type)
        else:
            return HttpResponse("nocard")

        return HttpResponse(card.worker.first_name + " " + card.worker.second_name + "-workout")

    return HttpResponse("Blad.")

def main(request):

    users = Worker.objects.all()
    ur = dict()
    for u in users:
        dt = dict()
        dt["Wiadomości"] = Messages.objects.filter(worker=u).count()
        dt["Nieprzeczytane wiadomości:"] = Messages.objects.filter(worker=u, read=0).count()
        dt["Liczba kart"] = Card.objects.filter(worker=u).count()
        ur[u] = dt

    t = get_template('h_home.html')
    html = t.render({'ur': ur})


    return HttpResponse(html)

def user_detail(request):
    if 'w' in request.GET:
        id = int(request.GET['w'])
        worker = Worker.objects.get(id=id)
        cr = dict()
        cards = Card.objects.filter(worker=worker)
        for c in cards:
            cr[c] = Record.objects.filter(card=c).order_by('-date')[:10]

        m = Messages.objects.filter(worker=worker, read=0).order_by('-date')
        t = get_template('u_user.html')
        html = t.render({'cr': cr, 'us': worker, 'mess': m})
        return HttpResponse(html)


    t = get_template('h_home.html')
    html = t.render({})
    return HttpResponse(html)


def user_messages(request):
    if 'w' in request.GET:
        id = int(request.GET['w'])
        worker = Worker.objects.get(id=id)

        m = Messages.objects.filter(worker=worker).order_by('-date')
        t = get_template('m_mess.html')
        html = t.render({'us': worker, 'mess': m})
        return HttpResponse(html)


    t = get_template('h_home.html')
    html = t.render({})
    return HttpResponse(html)

def add_messages_f(request):
    us = Worker.objects.all()
    t = get_template('a_mess.html')
    html = t.render({'us': us})
    return HttpResponse(html)

def add_messages(request):
    if 'user' in request.GET:
        id = int(request.GET['user'])
        worker = Worker.objects.get(id=id)

        body = request.GET['body']
        m = Messages(worker=worker, body=body, read=0)
        m.save()

    t = get_template('a_mess_s.html')
    html = t.render()
    return HttpResponse(html)


