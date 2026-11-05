from django.shortcuts import render

def index(request):
    return render(request, 'library_app/index.html')

def about(request):
    return render(request, 'library_app/about.html')

def contacts(request):
    return render(request, 'library_app/contacts.html')

def how_to_find(request):
    return render(request, 'library_app/how_to_find.html')

def catalog(request):
    return render(request, 'library_app/catalog.html')

def readers(request):
    return render(request, 'library_app/readers.html')