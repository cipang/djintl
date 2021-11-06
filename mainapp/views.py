from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.utils.translation import gettext as _, get_language
from django.shortcuts import render
from random import randint
from mainapp.utils import page_info


def main_view(request):
	s = _("Welcome\n")
	s += f"Current language: {get_language()}\n"
	return render(request, "main.html", {"s": s})


def random_view(request):
	r = randint(1000, 9999)
	s = _("Some number is: {0}.").format(r)
	return HttpResponse(f"<html><body><h1>{s}</h1></body></html>")


@page_info(page_id="p1", page_title="Page 1 Title")
def page1_view(request):
	print(f"{request.page_info=}")
	return render(request, "framework.html", {"content": "This is page 1."})
