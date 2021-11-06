from django.http import HttpResponse
from django.utils.translation import gettext as _, get_language
from django.shortcuts import render
from random import randint

# Create your views here.
def main_view(request):
	s = _("Welcome\n")
	s += f"Current language: {get_language()}\n"
	return render(request, "main.html", {"s": s})


def random_view(request):
	r = randint(1000, 9999)
	s = _("Some number is: {0}.").format(r)
	return HttpResponse(f"<html><body><h1>{s}</h1></body></html>")
