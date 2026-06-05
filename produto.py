class Produto:

    def __init__(self, id_produto: int, nome: str, preco: float, quantidade: int):
        self.id = id_produto
        self.nome = nome
        self.preco = float(preco)  # Garante que o preço seja um número decimal
        self.quantidade = int(quantidade)  # Garante que a quantidade seja um número inteiro

    def __str__(self):
        # O :.2f só funciona perfeitamente aqui porque self.preco é um float puro
        return f"[{self.id}] {self.nome} - R$ {self.preco:.2f} (Qtd: {self.quantidade})"

    
