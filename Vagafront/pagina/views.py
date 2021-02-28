from django.shortcuts import render
from django.http import HttpResponse

import requests
from urllib.request import urlopen
import json

def inicio (request):
    return render(request,"inicio.html")


def cadastro (request):
    url = "http://api.teste.vallions.com.br:7000/api/user"
    name = request.POST.get('name')
    email = request.POST.get('email')
    senha = request.POST.get('password')
    telefone = request.POST.get('phone')
    cpf = request.POST.get('cpf')
    if name or email or senha or telefone or cpf == None:
        mensagem = "Revise as informações e tente novamente!"
        return render(request,"cadastro.html",{'msg': mensagem})
    else:
        payload = {
        'name': str(name),
        'email':str(email),
        'password':str(senha),
        'phone':str(telefone),
        'cpf':str(cpf),
        }
        headers= {}

        response = requests.post(url, headers=headers, data = payload)

        response.text.encode('utf8')
        print(response)
        if response == "<Response [200]>":
            mensagem = "Cadastro concluido!"
            return render(request,"inicio.html",{'msg': mensagem})
        else:
            mensagem = "Erro no cadastro, Tente novamente mais Tarde!"
            return render(request,"cadastro.html",{'msg': mensagem})
    return render(request,"cadastro.html")


def usuarios (request):
    page = {}
    comp1 = []
    comp2 = []
    url = "http://api.teste.vallions.com.br:7000/api/users"
    payload = {}
    headers= {}
    response = requests.request("GET", url, headers=headers, data = payload)
    response = response.text.encode('utf8')
    response = json.loads(response)
    for cont1 in range(0,len(response)):
        for cont2 in range(0,len(response)):
            try:
                comparacao1 = (response[cont1])
            except:
                break
            comparacao2 = (response[cont2])
            comp1.append(str(comparacao1['name']))
            comp1.append(str(comparacao1['email']))
            comp1.append(str(comparacao1['phone']))
            comp2.append(str(comparacao2['name']))
            comp2.append(str(comparacao2['email']))
            comp2.append(str(comparacao2['phone']))
            cont2 = cont2
            if "None" in comp1:
                del(response[cont1])
                comp1 = []
                comp2 = []
                break
            elif "None" in comp2:
                del(response[cont2])
                comp1 = []
                comp2 = []
                break

            if cont1 != cont2:
                if comp2 == comp1:
                    del(response[cont2])
                    comp1 = []
                    comp2 = []
                    break
            else:
                comp1 = []
                comp2 = []

    return render(request,"usuarios.html",{"data":response})


def contato (request):
    return render(request,"contato.html")