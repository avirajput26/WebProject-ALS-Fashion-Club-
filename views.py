from django.shortcuts import render
from django.http import HttpResponse



def index(request):
    return render(request, 'index.html')
def women(request):
    return render(request, 'women.html')

# Create your views here.
