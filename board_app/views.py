from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse

from .models import *


# Create your views here.
def index(request):
    boards = {'boards': Board.objects.all()}
    return render(request, 'list.html', boards)


def post(request):
    if request.method == "POST":
        name = request.POST['name']
        phone = request.POST['phone']
        vdate = request.POST['vdate']
        gdate = request.POST['gdate']
        ap = request.POST['ap']
        walletype = request.POST['walletype']
        awAd = request.POST['awAd']
        bwAd= request.POST['bwAd']
        stakingW= request.POST['stakingW']
        stakingSD= request.POST['stakingSD']
        stakingDate= request.POST['stakingDate']
        stakingV = request.POST['stakingV']
        content= request.POST['content']
        board = Board(name=name, phone=phone, vdate=vdate, gdate=gdate, ap=ap, walletype=walletype, awAd=awAd, bwAd=bwAd, stakingW=stakingW, stakingSD=stakingSD, stakingDate=stakingDate, stakingV=stakingV, content=content )
        board.save()
        return HttpResponseRedirect(reverse('index'))
    else:
        return render(request, 'post.html')


def detail(request, no):
    try:
        board = Board.objects.get(pk=no)
    except Board.DoesNotExist:
        raise Http404("Does not exist!")
    return render(request, 'detail.html', {'board': board})
