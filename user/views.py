from django.shortcuts import render

def home(request):
    return render(request,'numismatics/home.html')
def coins(request):
    return render(request,'numismatics/coins.html')
def seals(request):
    return render(request, 'numismatics/seals.html')

def seal_issuer(request):
    return render(request, 'numismatics/seal_issuer.html')

def sources(request):
    return render(request, 'numismatics/sources.html')

def mints(request):
    return render(request, 'mints.html')

def all_datas(request):
    return render(request, 'numismatics/all_datas.html')
def start_page(request):
    return render(request, 'numismatics/start-page.html')
def emperor_page(request):
    return render(request, 'numismatics/emperor.html')
