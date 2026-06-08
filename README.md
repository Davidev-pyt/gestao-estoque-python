# 📦 Sistema de Gestão de Estoque e Vendas

Um sistema de gerenciamento de estoque e fluxo de caixa automatizado via terminal, desenvolvido em Python. O projeto aplica conceitos fundamentais de Engenharia de Software, como Programação Orientada a Objetos (POO), arquitetura de software limpa e persistência de dados.

## 🚀 Funcionalidades

- **Cadastro de Produtos:** Registro com validação de ID único, nome, preço e quantidade.
- **Tabela de Estoque Dinâmica:** Listagem visual estilizada que alerta automaticamente (em vermelho) quando um produto atinge nível crítico de estoque (menos de 4 unidades).
- **Módulo de Vendas:** Abatimento automático de itens no estoque com validação de segurança (impede vendas sem saldo disponível).
- **Relatório de Faturamento:** Histórico detalhado de vendas com cálculo automatizado do faturamento bruto acumulado da empresa.
- **Persistência de Dados (Banco NoSQL em JSON):** Os dados de produtos e vendas são salvos em arquivos locais, garantindo que as informações não sejam perdidas ao fechar o sistema.

## 🛠️ Tecnologias e Conceitos Utilizados

- **Linguagem:** Python 3
- **Biblioteca Visual:** [Rich](https://readthedocs.io) (para renderização de tabelas, painéis e menus interativos no terminal)
- **Paradigma:** Programação Orientada a Objetos (POO) com *Type Hinting* (indicação de tipos)
- **Persistência:** Manipulação de arquivos com o módulo nativo `json` e tratamento robusto de exceções (`try/except`)

## 📁 Estrutura de Pastas do Projeto

```text
gestao-estoque-python/
│
├── src/                  # Código-fonte isolado da aplicação
│   ├── __init__.py       # Inicializador do pacote Python
│   ├── produto.py        # Modelagem da classe Produto
│   └── estoque.py        # Classe controladora e regras de negócio
│
├── main.py               # Ponto de entrada (Interface e Loop do Menu)
├── requirements.txt      # Dependências externas do projeto
├── .gitignore            # Filtro para não subir arquivos desnecessários
└── README.md             # Documentação do projeto
```

## 🔧 Como Executar o Projeto

### Pré-requisitos
Certifique-se de ter o Python instalado na sua máquina.

1. **Clone o repositório:**
   ```bash
   git clone https://github.com
   cd gestao-estoque-python
   ```

2. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Execute o sistema:**
   ```bash
   python main.py
   ```

---
*Projeto desenvolvido como marco de evolução prática para o 3º semestre da faculdade de Engenharia de Software.*
