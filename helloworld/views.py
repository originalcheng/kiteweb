# from django.http import HttpResponse
from django.shortcuts import render
# from django.views.generic import TemplateView, View

def index(request):
    # return HttpResponse("Hello, Saul.")
    return render(request, "index.html", {})
