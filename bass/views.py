from django.shortcuts import render
from .models import Bass

def bass(request):
    """ renders the Bass page"""
    bass = Bass.objects.all().order_by('-dateTime').first()

    return render(
        request,
        "bass/bass.html",
        {"bass" : bass},
)