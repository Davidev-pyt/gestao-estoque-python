print("=== O PROGRAMA INICIOU VALENDO ===")

from produto import Produto
from estoque import Estoque

# 1. Instancia o gerenciador de estoque
meu_estoque = Estoque()

# 2. Cria alguns produtos fictícios com ID, Nome, Preço e Quantidade
p1 = Produto(1, "iPhone 17 Pro Max", 11000.00, 10)
p2 = Produto(2, "MacBook M4 Pro", 18500.00, 5)

# 3. Adiciona os produtos ao estoque
meu_estoque.adicionar_produto(p1)
meu_estoque.adicionar_produto(p2)

# 4. Lista o estoque para ver se funcionou
meu_estoque.listar_produtos()

