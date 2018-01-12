from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template

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

    t = get_template('h_home.html')
    html = t.render({'users': users})
    return HttpResponse(html)

def user_detail(request):
    if 'w' in request.GET:
        id = int(request.GET['w'])
        worker = Worker.objects.get(id=id)
        cr = dict()
        cards = Card.objects.filter(worker=worker)
        for c in cards:
            cr[c] = Record.objects.filter(card=c).order_by('-date')[:10]

        m = Messages.objects.filter(worker=worker, read=0)
        t = get_template('u_user.html')
        html = t.render({'cr': cr, 'us': worker, 'mess': m})
        return HttpResponse(html)


    t = get_template('h_home.html')
    html = t.render({})
    return HttpResponse(html)
