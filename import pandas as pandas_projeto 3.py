import pandas as pandas
dados = {
    "PRODUTO": ["Notebook", "Mouse", "Teclado", "Monitor", "Impressora"],
    "QUANTIDADE": [5, 30, 15, 8, 3],
    "PRECO": [3000, 100, 150, 1200, 800]
}
tabela = pandas.DataFrame(dados)
tabela["FATURAMENTO"] = tabela["QUANTIDADE"] * tabela["PRECO"]
status_lista = []
tabela["COMISSAO"] = tabela["FATURAMENTO"]
for comissao in tabela["FATURAMENTO"]:
    if comissao >= 10000:
        status_lista.append(0.08)
    else:
        status_lista.append(0.03)
tabela["COMISSAO"] = status_lista
tabela["VALOR_COMISSAO"] = tabela["FATURAMENTO"] * tabela["COMISSAO"]
categoria_lista = []
print(categoria_lista)
for categoria in tabela["FATURAMENTO"]:
    if categoria >= 15000:
        categoria_lista.append("TOP VENDAS")
    elif categoria >= 5000:
        categoria_lista.append("BOA VENDAS")
    else:
        categoria_lista.append("VENDAS BAIXAS")
tabela["CATEGORIA"] = categoria_lista
print(tabela["FATURAMENTO"].max())
print(tabela)