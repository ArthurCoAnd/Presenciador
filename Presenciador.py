# 	PORTUGUESE
# "A LICENÇA BEER-WARE" ou "A LICENÇA DA CERVEJA" (Revisão 42):
# arthurcoand@gmail.com escreveu este arquivo.
# Enquanto você manter este comentário, você poderá fazer o que quiser com este arquivo.
# Caso nos encontremos algum dia e você ache que este arquivo vale,
# você poderá me comprar uma cerveja em retribuição, Arthur Cordeiro Andrade.

# Arthur Cordeiro Andrade
# Email - arthurcoand@gmail.com
# GitHub - https://github.com/ArthurCoAnd

import csv
import matplotlib.pyplot as pp
import numpy as np
import pandas as pd

# Pasta Com Arquivos CSV - NOME e EMAIL
nome_pasta = "Teste"

# Número De Dias/Arquivos CSV
n_arqs = 4

# Número de Dias/Aparições para Aprovação
n_aprovação = 3

# ===== PESSOAS =====

# Tableba Dados Pessoas
pessoas = []

# Pessoas Por Dia
ppd = [0] * n_arqs

# Cadastrar Pessoas Primeiro Dia
str_nome_arq = nome_pasta + "/Dia1.csv"
with open(str_nome_arq, encoding="utf-8") as arq_csv:
	leitor = csv.reader(arq_csv)
	for nome, email in leitor:
		# Verificar se a pessoa analisada é repetida
			chave = True
			for p in range (len(pessoas)):
				if(pessoas[p][0].lower()==nome.lower() or pessoas[p][1].lower()==email.lower()):
					chave = False
					break
			if(chave):
				pessoas.append([nome,email,1])
				ppd[0] += 1
print("Pessoas depois do Dia 1")
print(pd.DataFrame(pessoas, columns=["Nome","Email","Presenças"]))

# Cadastrar Pessoas Próximos Dias
for n_arq_atual in range (2,n_arqs+1):
	str_nome_arq = nome_pasta + "/Dia" + str(n_arq_atual) + ".csv"
	with open(str_nome_arq, encoding="utf-8") as arq_csv:
		leitor = csv.reader(arq_csv)
		verificador = [True] * len(pessoas)
		for nome, email in leitor:
			# Verificar se a pessoa analisada é repetida
			chave = True
			for p in range (len(pessoas)):
				if(pessoas[p][0].lower()==nome.lower() or pessoas[p][1].lower()==email.lower()):
					chave = False
					if(verificador[p]):
						pessoas[p][2] += 1
						ppd[n_arq_atual-1] += 1
						verificador[p] = False
						break
			if(chave):
				pessoas.append([nome,email,1])
				verificador.append(False)
				print(verificador)
				ppd[n_arq_atual-1] += 1
	print(f"Pessoas depois do Dia {n_arq_atual}")
	print(pd.DataFrame(pessoas, columns=["Nome","Email","Presenças"]))

# Print Pessoas
print("Pessoas")
print(pd.DataFrame(pessoas, columns=["Nome","Email","Presenças"]))

# Criar Arquivo CSV com pessoas
nome_arquivo_aprovados = nome_pasta + "Presentes.csv"
with open(nome_arquivo_aprovados, "w", newline="", encoding="utf-8") as arq_csv:
	escritor = csv.writer(arq_csv)
	escritor.writerows(pessoas)

# ===== APROVADOS =====

# Gerar Tabela Dados Pessoas Aprovadas
pessoas_aprovadas = []
for p in range (len(pessoas)):
	if(pessoas[p][2]>=n_aprovação):
		pessoas_aprovadas.append([pessoas[p][0],pessoas[p][1]])

# Print Pessoas Aprovadas
print("Pessoas APROVADAS")
print(pd.DataFrame(pessoas_aprovadas, columns=["Nome","Email"]))

# Criar Arquivo CSV com pessoas Aprovadas
nome_arquivo_aprovados = nome_pasta + "Aprovados.csv"
with open(nome_arquivo_aprovados, "w", newline="", encoding="utf-8") as arq_csv:
	escritor = csv.writer(arq_csv)
	escritor.writerows(pessoas_aprovadas)

# ===== GRÁFICOS =====

# Aprovados Por Pessoas
app = [0,0]
indexG = ["Sim","Não"]
cores = ["#15aa15","#aa1515"]
for p in range (len(pessoas)):
	if(pessoas[p][2]>=n_aprovação):
		app[0] += 1
	else:
		app[1] += 1
gAPP = pp.subplot(221)
gAPP.set_title("Aprovados")
gAPP.pie(app, labels=indexG, autopct="%1.1f%%", shadow=True, startangle=90, colors=cores)

# Pessoas Por Valor de Presença
ppvdp = [0] * n_arqs
indexD = []
for p in range (len(ppvdp)):
	indexD.append(str(p+1))
for p in range (len(pessoas)):
	for i in range (n_arqs):
		if((i+1)==pessoas[p][2]):
			ppvdp[i] += 1
gPPVDP = pp.subplot(222)
gPPVDP.set_title("Frequência")
gPPVDP.pie(ppvdp, labels=indexD, autopct="%1.1f%%", shadow=True, startangle=90)

# Pessoas Por Dia
indexG = []
for p in range (n_arqs):
	indexG.append(f"Dia {p+1}")
gPPD = pp.subplot(212)
gPPD.set_title("Pessoas/Dia")
gPPD.bar(indexD, ppd)
gPPD.grid()

# Gerar e Mostrar Gráfico
pp.show()