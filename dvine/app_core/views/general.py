from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'app_core/pages/index.html', context)

def about(request):
    context = {}
    return render(request, 'app_core/pages/about.html', context)

def works(request):
    context = {}
    return render(request, 'app_core/pages/works.html', context)

def faq(request):
    context = {}
    return render(request, 'app_core/pages/faq.html', context)

def contact(request):
    context = {}
    return render(request, 'app_core/pages/contact.html', context)

def privacy(request):
    context = {}
    return render(request, 'app_core/pages/privacy.html', context)