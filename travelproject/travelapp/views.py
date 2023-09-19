from django.http import HttpResponse
from django.shortcuts import render
from .models import place
from .models import teams


# Create your views here.

def index(request):
    obj = place.objects.all()
    obj2 = teams.objects.all()
    return render(request, "index.html", {'output': obj,'result':obj2})

from django.shortcuts import render

# Create your views here.
