from produto import Produto
from estoque import Estoque
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

console = Console()
meu_estoque = Estoque()

def exibir_menu():
    opcoes = (
        "[bold cyan]1.[/bold cyan] Cadastrar Produto\n"
        "[bold cyan]2.[/bold cyan] Listar Estoque\n"
        "[bold cyan]3.[/bold cyan] Registrar Venda\n"
        "[bold cyan]4.[/bold cyan] Relatório de Vendas\n"
        "[bold cyan]5.[/bold cyan] Sair"
    )
    menu_painel = Panel(opcoes, title="[bold magenta]SISTEMA DE ESTOQUE[/bold magenta]", width=40)
    console.print(menu_painel)

def main():
    while True:
        exibir_menu()
        
        # Agora as escolhas válidas vão de 1 até 5
        opcao = Prompt.ask("Escolha uma opção", choices=["1", "2", "3", "4", "5"], default="2")

        if opcao == "1":
            console.print("\n[bold]--- NOVO CADASTRO ---[/bold]")
            try:
                id_prod = int(Prompt.ask("Digite o ID do produto"))
                nome = Prompt.ask("Nome do produto")
                preco = float(Prompt.ask("Preço do produto"))
                qtd = int(Prompt.ask("Quantidade em estoque"))
                
                novo_produto = Produto(id_prod, nome, preco, qtd)
                meu_estoque.adicionar_produto(novo_produto)
            except ValueError:
                console.print("[bold red]❌ Erro: Por favor, insira números válidos para ID, Preço e Quantidade.[/bold red]")
            console.print("")

        elif opcao == "2":
            console.print("")
            meu_estoque.listar_produtos()
            console.print("")

        elif opcao == "3":
            console.print("\n[bold]--- REGISTRAR VENDA ---[/bold]")
            try:
                id_prod = int(Prompt.ask("Digite o ID do produto vendido"))
                qtd_venda = int(Prompt.ask("Quantidade vendida"))
                
                meu_estoque.realizar_venda(id_prod, qtd_venda)
            except ValueError:
                console.print("[bold red]❌ Erro: Digite valores numéricos válidos.[/bold red]")
            console.print("")

        elif opcao == "4":
            console.print("")
            meu_estoque.exibir_relatorio_vendas()
            console.print("")

        elif opcao == "5":
            console.print("[bold green]👋 Saindo do sistema... Até logo![/bold green]")
            break

if __name__ == "__main__":
    main()
