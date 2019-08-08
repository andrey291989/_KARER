from django.shortcuts import render
from .models import Samosval
# Create your views here.

#def index(request):
#    """Домашняя страница приложения Learning Log"""
#    return render(request, 'polls/index.html')

def index(request):
    topics = Samosval.objects.all()
    context = {'topics': topics}
    return render(request, 'polls/index.html', context)