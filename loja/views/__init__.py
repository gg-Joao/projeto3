from .HomeView import home_view
from .ProdutoView import (
	list_produto_view,
	create_produto_view,
	edit_produto_view,
	edit_produto_postback,
	produto_detail_view,
	produto_delete_view,
)

__all__ = [
	'home_view',
	'list_produto_view',
	'create_produto_view',
	'edit_produto_view',
	'edit_produto_postback',
	'produto_detail_view',
	'produto_delete_view',
]
