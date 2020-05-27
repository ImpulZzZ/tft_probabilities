from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
        return render(request, 'index.html')
        #return HttpResponse("Hello World. You're at the tft_prp index.")