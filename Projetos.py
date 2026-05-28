import pandas as pd
dados = {
    "NOME":["Ana", "João", "Maria"],
    "SALARIO":[2000, 3000, 4000]
}
tabela = pd.DataFrame(dados)
tabela["BONUS"] = tabela["SALARIO"] * 0.10
tabela["STATUS"] = ["BONUS NORMAL", "BONUS ALTO", "BONUS ALTO"]
print(tabela)