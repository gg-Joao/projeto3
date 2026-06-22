from django.urls import path
from ..views import list_produto_view, create_produto_view, edit_produto_view, edit_produto_postback

urlpatterns = [
    path('produto/', list_produto_view, name='produto_list'),
    path('produto/create/', create_produto_view, name='create_produto'),
    path('produto/<int:id>/', list_produto_view, name='produto_detail'),
    path('produto/<int:id>/edit/', edit_produto_view, name='produto_edit'),
    path('produto/<int:id>/edit/post/', edit_produto_postback, name='produto_edit_post'),
    path('produto/<int:id>/delete/', list_produto_view, name='produto_delete'),
]
