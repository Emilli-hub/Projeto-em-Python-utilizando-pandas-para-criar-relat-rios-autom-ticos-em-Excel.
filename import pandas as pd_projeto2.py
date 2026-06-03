import pandas as pd
dados = {
    "NOME": ["Ana", "João", "Maria", "Carlos", "Julia"],
    "SALARIO": [2500, 4000, 3500, 6000, 8000],
    "SETOR": ["RH", "TI", "FINANCEIRO", "TI", "DIRETORIA"]
}
tabela = pd.DataFrame(dados)
status_cargo = []
for salario in tabela["SALARIO"]:
    if salario < 3000:
        status_cargo.append("JUNIOR")
    elif 3000 <= salario < 5000:
        status_cargo.append("PLENO")
    else:
        status_cargo.append("SENIOR")
tabela["STATUS"] = status_cargo
status_bonus = []
for setor in tabela["STATUS"]:
    if setor == "JUNIOR":
        status_bonus.append(0.05)
    elif setor == "PLENO":
        status_bonus.append(0.10)
    else:
        status_bonus.append(0.15)
tabela["BONUS"] = status_bonus
tabela["SALARIO_FINAL"] = tabela["SALARIO"] + (tabela["SALARIO"] * tabela["BONUS"])
print(tabela["SALARIO_FINAL"].max())
print(tabela["SALARIO_FINAL"].mean())
tabela.to_excel("tabela_funcionarios.xlsx", index=False)
print("Excel criado com sucesso!")
print(tabela)