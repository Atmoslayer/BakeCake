from django.http import HttpResponse


def index(request):
    return HttpResponse("База данных тортиков")