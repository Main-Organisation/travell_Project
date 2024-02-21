from django.shortcuts import render

def index(request):
    return render(request, 'travel/index.html')

def FirstPage(request):
    return render(request, 'travel/FirstPage.html')

def secondpage(request):
    return render(request, 'travel/secondpage.html')

def therdpage(request):
    return render(request, 'travel/therdpage.html')

def ForthPage(request):
    return render(request, 'travel/ForthPage.html')