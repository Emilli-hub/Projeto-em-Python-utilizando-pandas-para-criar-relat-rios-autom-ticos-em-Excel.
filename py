import pandas as pd
dados = {
    "NOME":["Ana", "João", "Maria"],
    "MEDIA":[8, 5, 9]
}
tabela = pd.DataFrame(dados)
status = []
for media in tabela["MEDIA"]:
    if media >= 7:
        status.append("APROVADO")
    else: 
        status.append("REPROVADO")
tabela ["STATUS"] = status
print(tabela)
