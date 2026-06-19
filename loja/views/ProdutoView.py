from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from ..models import Produto


def list_produto_view(request, id=None):
    # Mostra todos os produtos e imprime no terminal
    produtos = Produto.objects.all()
    print('Produtos no banco:', list(produtos.values('id', 'produto')))

    # Captura parâmetros GET
    params = {k: request.GET.get(k) for k in ['produto', 'destaque', 'promocao', 'categoria', 'fabricante']}
    print('GET params:', params)

    # Filtros simples (exemplos demonstrativos)
    qs = Produto.objects.all()
    if params.get('produto'):
        qs = qs.filter(produto__icontains=params['produto'])
    if params.get('promocao'):
        if params['promocao'].lower() in ['1', 'true', 'yes']:
            qs = qs.filter(promocao=True)
    if params.get('destaque'):
        if params['destaque'].lower() in ['1', 'true', 'yes']:
            qs = qs.filter(destaque=True)
    if params.get('categoria'):
        qs = qs.filter(categoria__categoria__iexact=params['categoria'])
    if params.get('fabricante'):
        qs = qs.filter(fabricante__fabricante__iexact=params['fabricante'])
    if id:
        qs = qs.filter(id=id)

    print('Resultado da consulta:', list(qs.values('id', 'produto')))

    return HttpResponse(f'Produtos encontrados: {qs.count()} — id recebido: {id}')
