from django.shortcuts import render

def landing(request):
    """render the landing page"""
    return render(request, "bouncer/index.html")

