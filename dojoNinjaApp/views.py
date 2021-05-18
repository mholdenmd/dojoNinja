from django.http.response import HttpResponse
from django.shortcuts import redirect, render, HttpResponse

from .models import *
# Create your views here.
def index(request):
    print("*******")
    print(Dojo.objects.all())
    print("*******")
    context = {
        "alldojos": Dojo.objects.all()
        
    }

    return render(request, "markfiles.html", context)

def createDojo(request):
    print("*******")
    print(request.POST)
    print("*******")
    Dojo.objects.create(name=request.POST["dojoname"], city=request.POST["City"], state=request.POST["State"])
    return redirect("/")

def createNinja(request):
    print("*******")
    print(request.POST)
    print("*******")
    Ninja.objects.create(fname=request.POST["first_name"], lname=request.POST["last_name"], dojo=Dojo.objects.get(id=request.POST["dojoTeam"]))
    return redirect("/")