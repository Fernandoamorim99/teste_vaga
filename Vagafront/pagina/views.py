from django.shortcuts import render
from django.http import HttpResponse

import requests
from urllib.request import urlopen
import json

def inicio (request):
    return render(request,"inicio.html")


def cadastro (request):
    return render(request,"cadastro.html")


def usuarios (request):
    url = "http://api.teste.vallions.com.br:7000/api/users"
    payload = {}
    headers= {}
    response = requests.request("GET", url, headers=headers, data = payload)

    return render(request,"usuarios.html")


def contato (request):
    return render(request,"contato.html")