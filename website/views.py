from django.shortcuts import render, redirect

def home_view(request):
    return render(request, "home.html")

def index(request):
    return redirect('home/')

def about(request):
    return render(request, "about.html")

def complaints(request):
    return render(request, "complaints.html")

def in_progress(request):
    return render(request, "in-progress.html")