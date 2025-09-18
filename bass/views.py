from django.shortcuts import render
from django.views import generic
from .models import Bass


class BassList(generic.ListView):
    queryset = Bass.objects.all()
    template_name = "bass/index.html"
    paginate_by = 3


def bass(request):
    """ renders the Bass page"""
    bass_list = Bass.objects.all().order_by('-dateTime')
    return render(
        request,
        "bass/bass.html",
        {"bass_list": bass_list},
    )