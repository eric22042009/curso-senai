nome_arquivo = input('Nome do arquivo a limpar (ex: "diario.txt"): ')
 
  
with open(nome_arquivo, "w", encoding="utf-8"):
    pass
 
print(f"O arquivo {nome_arquivo} foi totalmente limpo e resetado!")