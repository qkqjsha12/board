from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from .models import *
from .forms import BoardForm
from django.contrib import messages
from django.db.models import Q

# Create your views here.

def index(request):
    boards = {'boards': Board.objects.all()}
    return render(request, 'list.html', boards)


def post(request):
    # if request.method == "POST":
    #     form = BoardForm(request.POST)
    #     if form.is_valid():
    #         board = form.save(commit=False)
    #         board.save()
    #         messages.success(request, "등록되었습니다.")
    #         return HttpResponseRedirect(reverse('index'))
    #     else:
    #         return HttpResponseRedirect(reverse('index'))
    # else:
    #     form = BoardForm()
    #     return render(request, 'post.html', {'from': form})

 #과거판
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
        messages.success(request, "등록되었습니다.")
        return HttpResponseRedirect(reverse('index'))
    else:
        return render(request, 'post.html')

def detail(request, no):
    try:
        board = Board.objects.get(pk=no)
    except Board.DoesNotExist:
        raise Http404("Does not exist!")
    return render(request, 'detail.html', {'board': board})

def delete(request, no):
    board = Board.objects.get(pk=no)
    board.delete()
    messages.success(request, "삭제되었습니다.")
    return HttpResponseRedirect(reverse('index'))


def update(request, no):
     
    board = get_object_or_404(Board, pk=no)
    
    if request.method == "POST":
        form = BoardForm(request.POST, instance=board)
        board = form.save(commit=False)

        board.save()
        messages.success(request, "수정되었습니다.")
        return redirect('/detail/' + str(board.no))
    else:
        form = BoardForm(instance=board)

        return render(request, 'update.html', {'form': form})
       

  

