import pandas as pd
dados = {
    "PRODUTO":["Notebook", "Mouse", "Teclado", "Monitor", "Impressora"],
    "QUANTIDADE":[10, 50, 20, 5, 3],
    "PRECO":[3000, 100, 150, 1200, 800]
}
tabela = pd.DataFrame(dados)
tabela["FATURAMENTO"] = tabela["QUANTIDADE"] * tabela["PRECO"]
status_faturamento = []
for faturamento in tabela["FATURAMENTO"]:
    if faturamento >= 10000:
        status_faturamento.append("ALTA VENDA")
    else:
        status_faturamento.append("BAIXA VENDA")
status_lista = []
for status in status_faturamento:
    if status == "ALTA VENDA":
        status_lista.append(0.10)
    else:
        status_lista.append(0)
tabela["DESCONTO"] = status_lista
tabela["VALOE_FINAL"] = tabela["FATURAMENTO"] - tabela["DESCONTO"]
tabela.to_excel("tabela_relatorio_vendas.xlsx", index=False)
print("Excel criado com sucesso!")
print(tabela)