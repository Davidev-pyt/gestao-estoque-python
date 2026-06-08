from produto import Produto
import json
import os
#Componetes visuais do rich
from rich.console import Console
from rich.table import Table
console = Console()
class Estoque:

    def __init__(self):
        #Lista para armazenar os produtos no estoque
        self.produtos = []
        self.historico_vendas = [] # Lista para guardar as vendas realizadas
        self.caminho_arquivo = "estoque.json"
        self.caminho_venda = "vendas.json" # Arquivo para salvar o historico 
        self.carregar_dados = () 

    def adicionar_produto(self, produto: Produto):
        """Adiciona um novo produto ao estoque."""
        self.produtos.append(produto)
        console.print(f'[bold green] ✅ Produto "{produto.nome}" adicionado com sucesso![/bold green]')
        self.salvar_dados()
    
    def listar_produtos(self):
        """Lista de todos os produtos no estoque."""
        if not self.produtos:
            console.print(f"[bold yellow]⚠️ O estoque está vazio.[/bold yellow]")
            
        #Cria a estrutura da tabela usando a biblioteca rich para exibir os produtos de forma organizada.
        tabela = Table(title = "📦 Produtos em estoque", show_header = True, header_style = "bold magenta" )
        tabela.add_column("ID", style="dim", width = 6, justify = "center")
        tabela.add_column("Nome do produto", min_width = 20)
        tabela.add_column("Preço unidade", justify = "right", style = "green")
        tabela.add_column("Quantidade", justify = "center")

        # Alimenta a tabela com os dados do estoque
        for prod in self.produtos:
        #Regra visual se os estoque estiver baixo (menos de 4 itens), exibe em vermelho
            qtd_estilizada = f"[bold red] {prod.quantidade}[/bold red]" if prod.quantidade < 4 else str(prod.quantidade) 

            tabela.add_row(
                str(prod.id),
                prod.nome, 
                f"{prod.preco:.2f}",
                qtd_estilizada
            )
            # Imprime a tabela renderizada na tela
            console.print(tabela)
    def realizar_venda (self, id_produto, quantidade_venda):
            """ busca o produto pelo id e reduz a quantidade se houver estoque suficiente"""
            for prod in self.produtos:
                if prod.id == id_produto:
                    if prod.quantidade >= quantidade_venda:
                        prod.quantidade -= quantidade_venda
                        
                        # Calcula o valor total da venda
                        valor_total = prod.preco * quantidade_venda

                        # Registra a venda em um dicionario
                        nova_venda = {
                            "produto":prod.nome, 
                            "quantidade":quantidade_venda,
                            "total":valor_total
                        }
                        self.historico_vendas.append(nova_venda)
                        console.print(f"[bold blue]🛍️ Venda realizada:[/bold blue] {quantidade_venda} unidade(s) de '{prod.nome}' (Total: R$ {valor_total:.2f})")

                        # Salva ambos os arquivos de dados
                        self.salvar_dados()
                        return True
                    else:
                         console.print(f"[bold red]❌ Erro:[/bold red] Estoque insuficiente para '{prod.nome}'. Disponível: {prod.quantidade}")
                         return False
                    
            console.print(f"[bold yellow]⚠️ Erro:[/bold yellow] Produto com ID {id_produto} não encontrado.")
            return False
    def exibir_relatorio_vendas (self):
        """Exibe uma tabela com todas as vendas feitas e seu faturamento"""
        if not self.historico_vendas:
            console.print("[bold yellow]⚠️ Nenhuma venda registrada ainda.[/bold yellow]")
            return
        tabela = Table(title ="📈 Relatorio de vendas", show_header = True, header_style = "bold cyan")
        tabela.add_column("Produto", min_width=20)
        tabela.add_column("Qtd Vendida", justify="center")
        tabela.add_column("Total Faturado", justify="right", style="green")
        
        faturamento_total = 0.0
        for venda in self.historico_vendas:
              tabela.add_row(
                venda["produto"],
                str(venda["quantidade"]),
                f"R$ {venda['total']:.2f}"
            )
              faturamento_total += venda['total']
              console.print(tabela)
              console.print(f"[bold green]💰 FATURAMENTO TOTAL ACUMULADO: R$ {faturamento_total:.2f}[/bold green]\n")

    def salvar_dados(self):
         """Salva os produtos e o historico de venda em um arquivo json separados."""
         # Salva produtos 
         lista_dicionarios = []
         for prod in self.produtos:
              dados_prod = {"id": prod.id, "nome": prod.nome, "preco": prod.preco, "quantidade": prod.quantidade}
              lista_dicionarios.append(dados_prod)
         with open(self.caminho_arquivo, "w", encoding="utf-8") as arquivo:
            json.dump(lista_dicionarios, arquivo, indent=4, ensure_ascii=False)
            
        # Salva Vendas
         with open(self.caminho_venda, "w", encoding="utf-8") as arquivo:
            json.dump(self.historico_vendas, arquivo, indent=4, ensure_ascii=False)
    def carregar_dados(self):
        """Carrega produto do historico de vendas do arquivo json"""
        #carrega produtos 
        if os.path.exists(self.caminho_arquivo):
            try:
                  with open(self.caminho_arquivo, "r", encoding="utf-8") as arquivo:
                    lista_dicionarios = json.load(arquivo)
                    self.produtos = []
                    for dados in lista_dicionarios:
                        self.produtos.append(Produto(dados["id"], dados["nome"], dados["preco"], dados["quantidade"]))
            except Exception as e:
                console.print(f"[bold red]❌ Erro ao carregar produtos: {e}[/bold red]")

    #carrega vendas
        if os.path.exists(self.caminho_venda):
            try:
                with open(self.caminho_venda, "r", encoding="utf-8") as arquivo:
                    self.historico_vendas = json.load(arquivo)
            except Exception as e:
                console.print(f"[bold red]❌ Erro ao carregar vendas: {e}[/bold red]")
