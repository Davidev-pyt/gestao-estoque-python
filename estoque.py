from produto import Produto

class Estoque:

    def __init__(self):
        #Lista para armazenar os produtos no estoque
        self.produtos = []

    def adicionar_produto(self, produto: Produto):
        """Adiciona um novo produto ao estoque."""
        self.produtos.append(produto)
        return f" :white_check_mark:Produto '{produto.nome}' adicionado ao estoque."
    
    def listar_produtos(self):
        """Lista de todos os produtos no estoque."""
        if not self.produtos:
            return " :warning:O estoque está vazio."
        
        print("\n --- Produtos no Estoque ---")
        for prod in self.produtos:
            print(prod) #Prod é o objeto do tipo produto que vai ser chamado o método __str__ para exibir as informações do porduto de forma formatada.
            print("-" * 30)