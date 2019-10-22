from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, Clint and Ramsey and Baha and Deniz.")