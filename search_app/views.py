from django.shortcuts import render
from board_app.models import Board
from django.db.models import Q

def search(request):
    if 'q' in request.GET:
        query = request.GET.get('q')
        querys = Board.objects.filter(Q(name__icontains=query) | Q(phone__icontains=query))
    
    return render(request, 'search.html', {'query':query, 'querys':querys})
