from django.http import HttpResponse


def home_view(request):
    return HttpResponse('Bem-vindo à loja — view home funcionando')
