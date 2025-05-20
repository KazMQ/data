dic = {
    'nome': 'Notebook',
    'preco': 3500.00,
    'estoque': 15
}

del dic ['estoque']
dic.update({'preco': 4000.00})
print(f"{dic['nome']} custa R$ {dic['preco']}")