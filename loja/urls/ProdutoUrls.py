from django.urls import path
from ..views import list_produto_view

urlpatterns = [
    path('produto/', list_produto_view, name='produto_list'),
    path('produto/<int:id>/', list_produto_view, name='produto_detail'),
]
