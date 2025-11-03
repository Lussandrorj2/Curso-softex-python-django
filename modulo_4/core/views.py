from django.shortcuts import render
from django.http import HttpResponse 
# Uma 'view' é uma função que recebe um 'request' e retorna uma 'response' 
def home(request): 
# Vamos retornar a resposta HTTP mais simples: um texto HTML 
    return HttpResponse("<h1>Olá, Mundo! Esta é minha primeira página Django!</h1>") 
# Create your views here.

def saudacao(request):
    return HttpResponse("<h1> Segunda linha do código <h1>")
