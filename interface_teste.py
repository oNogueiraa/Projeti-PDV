import tkinter as tk
from tkinter import messagebox

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f'{self.nome} - R$ {self.preco:.2f}'

class PilhaProdutos:
    def __init__(self):
        self.pilha = []

    def adicionar_produto(self, produto):
        self.pilha.append(produto)
        return f'Produto {produto.nome} adicionado com sucesso!'

    def listar_produtos(self):
        if not self.pilha:
            return ["Nenhum produto cadastrado."]
        return [str(produto) for produto in self.pilha]

class FilaCustos:
    def __init__(self):
        self.fila = []

    def adicionar_custo(self, custo):
        self.fila.append(custo)
        return f'Custo R$ {custo:.2f} adicionado à fila.'

    def calcular_media_custos(self):
        if not self.fila:
            return 0
        return sum(self.fila) / len(self.fila)

class PilhaVendas:
    def __init__(self):
        self.pilha = []

    def registrar_venda(self, produto):
        self.pilha.append(produto)
        return f'Venda registrada: {produto.nome}'

    def listar_vendas(self):
        if not self.pilha:
            return ["Nenhuma venda registrada."]
        return [str(venda) for venda in self.pilha]

class PDVApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDV de Açaí")

        # Instâncias das pilhas e filas
        self.pilha_produtos = PilhaProdutos()
        self.fila_custos = FilaCustos()
        self.pilha_vendas = PilhaVendas()

        # Menu principal
        self.menu_frame = tk.Frame(root)
        self.menu_frame.pack(pady=20)

        tk.Button(self.menu_frame, text="Cadastrar Produto", command=self.cadastrar_produto).pack(fill="x")
        tk.Button(self.menu_frame, text="Listar Produtos", command=self.listar_produtos).pack(fill="x")
        tk.Button(self.menu_frame, text="Adicionar Custo", command=self.adicionar_custo).pack(fill="x")
        tk.Button(self.menu_frame, text="Calcular Média de Custos", command=self.calcular_media_custos).pack(fill="x")
        tk.Button(self.menu_frame, text="Registrar Venda", command=self.registrar_venda).pack(fill="x")
        tk.Button(self.menu_frame, text="Listar Vendas", command=self.listar_vendas).pack(fill="x")

    def cadastrar_produto(self):
        def adicionar():
            nome = entry_nome.get()
            preco = float(entry_preco.get())
            msg = self.pilha_produtos.adicionar_produto(Produto(nome, preco))
            messagebox.showinfo("Sucesso", msg)
            cadastro_window.destroy()

        cadastro_window = tk.Toplevel(self.root)
        cadastro_window.title("Cadastrar Produto")

        tk.Label(cadastro_window, text="Nome do Produto:").pack()
        entry_nome = tk.Entry(cadastro_window)
        entry_nome.pack()

        tk.Label(cadastro_window, text="Preço do Produto:").pack()
        entry_preco = tk.Entry(cadastro_window)
        entry_preco.pack()

        tk.Button(cadastro_window, text="Adicionar", command=adicionar).pack(pady=10)

    def listar_produtos(self):
        produtos = self.pilha_produtos.listar_produtos()
        messagebox.showinfo("Produtos Cadastrados", "\n".join(produtos))

    def adicionar_custo(self):
        def adicionar():
            custo = float(entry_custo.get())
            msg = self.fila_custos.adicionar_custo(custo)
            messagebox.showinfo("Sucesso", msg)
            custo_window.destroy()

        custo_window = tk.Toplevel(self.root)
        custo_window.title("Adicionar Custo")

        tk.Label(custo_window, text="Novo Custo:").pack()
        entry_custo = tk.Entry(custo_window)
        entry_custo.pack()

        tk.Button(custo_window, text="Adicionar", command=adicionar).pack(pady=10)

    def calcular_media_custos(self):
        media = self.fila_custos.calcular_media_custos()
        messagebox.showinfo("Média de Custos", f"Média de custos: R$ {media:.2f}")

    def registrar_venda(self):
        def registrar():
            nome_venda = entry_nome_venda.get()
            for produto in self.pilha_produtos.pilha:
                if produto.nome.lower() == nome_venda.lower():
                    msg = self.pilha_vendas.registrar_venda(produto)
                    messagebox.showinfo("Sucesso", msg)
                    venda_window.destroy()
                    return
            messagebox.showerror("Erro", "Produto não encontrado.")

        venda_window = tk.Toplevel(self.root)
        venda_window.title("Registrar Venda")

        tk.Label(venda_window, text="Nome do Produto Vendido:").pack()
        entry_nome_venda = tk.Entry(venda_window)
        entry_nome_venda.pack()

        tk.Button(venda_window, text="Registrar", command=registrar).pack(pady=10)

    def listar_vendas(self):
        vendas = self.pilha_vendas.listar_vendas()
        messagebox.showinfo("Vendas Registradas", "\n".join(vendas))

if __name__ == "__main__":
    root = tk.Tk()
    app = PDVApp(root)
    root.mainloop()
