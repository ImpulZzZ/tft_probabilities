from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render

# "Home page"
def home(request):
        return render(request, 'home.html')
        #return HttpResponse("Hello World. You're at the tft_prp index.")