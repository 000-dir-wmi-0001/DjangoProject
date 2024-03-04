from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    peoples=[
        {'name':"jhon",'age':19},
        {'name':"james",'age':14},
        {'name':"bond",'age':18},
        {'name':"brandie",'age':15},
        {'name':"lincon",'age':20},
        {'name':"abraham",'age':17},
        {'name':"goslin",'age':22}

    ]
    return render(request,"index.html", context = {'peoples' : peoples})