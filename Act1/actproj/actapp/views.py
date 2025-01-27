from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')
def games(request):
    return render(request, "game.html")
def contacts(request):
    return render(request, 'contacts.html')
