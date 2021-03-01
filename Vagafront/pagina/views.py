from django.shortcuts import render
from django.http import HttpResponse

import requests
from urllib.request import urlopen
import json

def inicio (request):
    mensagem = ""
    return render(request,"inicio.html",{'msg': mensagem})


def cadastro (request):
    mensagem = ""
    status_msn = 1
    url = "http://api.teste.vallions.com.br:7000/api/user"
    name = request.POST.get('name')
    email = request.POST.get('email')
    senha = request.POST.get('password')
    conf = request.POST.get('passconfirm')
    telefone = request.POST.get('phone')
    cpf = request.POST.get('cpf')
    print(name,email,cpf)
    if name == None:
        name = ""
        status_msn -= 1
    else:
        if email == None:
            email = ""
            status_msn -= 1
        else:
            if senha == None:
                senha = ""
                status_msn -= 1
            else:
                if conf == None:
                    conf = ""
                    status_msn -= 1
                else:
                    if telefone == None:
                        telefone = ""
                        status_msn -= 1
                    else:
                        if cpf == None:
                            cpf = ""
                            status_msn -= 1
    if status_msn <= 0:
        mensagem = ""
        print("None")
        return render(request,"cadastro.html",{'msg': mensagem})
    else:
        if name == "":
            mensagem = "Erro no cadastro, Preencha o campo Nome!"
            print("Erro no cadastro, Preencha o campo Nome!")
            return render(request,"cadastro.html",{'msg': mensagem})
        else:
            if email == "":
                mensagem = "Erro no cadastro, Preencha o campo E-mail!"
                print("Erro no cadastro, Preencha o campo E-mail!!")
                return render(request,"cadastro.html",{'msg': mensagem})
            else:
                if cpf == "":
                    mensagem = "Erro no cadastro, Preencha o campo CPF!"
                    print("Erro no cadastro, Preencha o campo CPF!")
                    return render(request,"cadastro.html",{'msg': mensagem})
                else:
                    if telefone == "":
                        mensagem = "Erro no cadastro, Preencha o campo Telefone!"
                        print("Erro no cadastro, Preencha o campo Telefone!")
                        return render(request,"cadastro.html",{'msg': mensagem})
                    else:
                        if senha == "":
                            mensagem = "Erro no cadastro, Preencha o campo Senha!"
                            print("Erro no cadastro, Preencha o campo Senha!")
                            return render(request,"cadastro.html",{'msg': mensagem})
                        else:
                            if conf == "":
                                mensagem = "Erro no cadastro, Preencha o campo de confirmação de Senha!"
                                print("Erro no cadastro, Preencha o campo de confirmação de Senha!")
                                return render(request,"cadastro.html",{'msg': mensagem})
                            else:
                                if senha == conf:
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
                                    mensagem = "Cadastro Concluido!"
                                    print("Cadastro Concluido!")
                                    return render(request,"inicio.html",{'msg': mensagem})
                                else:
                                    mensagem = "Senhas não correspondem!"
                                    print("Senhas não correspondem!")
                                    return render(request,"usuarios.html",{'msg': mensagem})
    return render(request,"cadastro.html",{'msg': mensagem})


def usuarios (request):
    page = {}
    comp1 = []
    comp2 = []
    mensagem = ""
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

    return render(request,"usuarios.html",{"data":response, 'msg': mensagem})


