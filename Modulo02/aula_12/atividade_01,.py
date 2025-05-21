import pandas as pd

livros = ["LT. Brasileira", "LT. Estrangeira", "Ciências", "Matemática", "História"]
qtd_estoque = [12, 9, 18, 14, 20]
qtd_borrow = [4, 2, 7, 5, 6]

#Series de livros com a quantidade total
estoque_total = pd.Series(qtd_estoque, index=livros)

estoque_total.loc["Filosofia"] = None

#Series de livros emprestados
estoque_borrow = pd.Series(qtd_borrow, index=livros)

#Series com calculo entre os estoques
estoque = estoque_total - estoque_borrow

print("\nA seguinte quantidade está disponivel: ")
print(estoque[estoque > 5])