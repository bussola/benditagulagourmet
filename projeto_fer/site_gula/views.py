from django.shortcuts import render, redirect

def index(request):
    return render(request, 'site/index.html')

def graficos(request):
    return render(request, 'graficos.html')
