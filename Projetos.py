import pandas as pd
dados = {
    "PRODUTO":["Notebook", "Mouse", "Teclado", "Monitor"],
    "QUANTIDADE":[2, 5, 3, 1],
    "PRECO":[3000, 100, 150, 1200]
}
tabela = pd.DataFrame(dados)
tabela["TOTAL"] = tabela["QUANTIDADE"] * tabela["PRECO"]
desconto = []
for valor in tabela["TOTAL"]:
    if valor >= 1000:
       desconto.append(valor * 0.10)
    else:
       desconto.append(0)
tabela["DESCONTO"] = desconto
tabela["VALOR FINAL"] = tabela["TOTAL"] - tabela["DESCONTO"]
tabela.to_excel("controle_vendas.xlsx", index=False)
print("Excel criado com sucesso!")
print(tabela)