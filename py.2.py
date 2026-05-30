import pandas as pd
dados = {
    "PRODUTOS":["Notebook", "Mouse", "Teclado", "Monitor"],
    "QUANTIDADE":[10, 50, 20, 5],
    "PRECO":[3000, 100, 150, 1200]
}
tabela = pd.DataFrame(dados)
tabela["TOTAL"] = tabela["QUANTIDADE"] * tabela["PRECO"]
status_lista = []
tabela["QUANTIDADE"]
for quantidade in tabela["QUANTIDADE"]:
    if quantidade < 10:
        status_lista.append("ESTOQUE BAIXO")
    else:
        status_lista.append("ESTOQUE OK")
tabela["STATUS"] = status_lista
desconto = []
for total in tabela["TOTAL"]:
    if total >= 30000: 
      desconto.append(total * 0.10)
    else:
      desconto.append(0)
tabela["DESCONTO"] = desconto
tabela["VALOR_FINAL"] = tabela["TOTAL"] - tabela["DESCONTO"]
tabela.to_excel("vendas.xlsx", index=False)
print("Excel criado com sucesso!")