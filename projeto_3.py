# -*- coding: utf-8 -*-

#abrindo arquivo usuario, lendo linha 1, lendo linha 2, limpando e separando informacoes de usuario
entrada_usuario = open("usuario.csv","r")
entrada_usuario.readline()
entrada_informacoes = entrada_usuario.readline()
entrada_informacoes.strip()
info = entrada_informacoes.split(',')


nome = info[0]
sexo = info[3]
idade = int(info[1])
altura = float(info[4])
peso = float(info[2])
atividade = info[5]


IMC = peso/(altura**2)


if IMC < 17:
	imc_usuario = "muito abaixo do peso"
elif IMC > 17 and IMC < 18.49:
	imc_usuario = "abaixo do peso"
elif IMC >=18.5 and IMC < 24.99:
	imc_usuario = "no peso normal"
elif IMC >25 and IMC <29.99:
	imc_usuario = "acima do peso"
elif IMC >30 and IMC< 34.99:
	imc_usuario = "no nivel de obesidade 1"
elif IMC >35 and IMC <39.99:
	imc_usuario = "no nivel de obesidade 2"
elif IMC>40:
	imc_usuario = "com obesidade morbida"
print(imc_usuario)


arquivo_txt = open("newfile.txt","w")
arquivo_txt.write("O seu Indice de massa corporea é %s \n"%IMC)
arquivo_txt.write("voce esta %s \n"%imc_usuario)


diario = {}
entrada_usuario.readline()
linhasdiario = entrada_usuario.readlines() 
for line in linhasdiario:
    print(line)
    

"""
formula consumo de caloria ideal
if sexo == "m" or sexo =="M":
	HBh = (88.362 + (13.397 * peso) + (4.799 * altura) - (5.677 * idade)) * atividade
	
elif sexo == "f" or sexo == "F":
	HBm = (447.593 + (9.247 * peso) + (3.098 * altura) - (4.330 * idade)) * atividade	
"""	

entrada_alimentos = open("alimentos.csv","r")
linhas = entrada_alimentos.readlines()
linhas_limpas = []                            
for i in linhas:
    linhas_limpas.append(i.strip())
alimentos = dict()
for l in linhas_limpas[1:]:                        
    info2 = l.split(',')
"""     
info2[0] = "Alimento"
info2[1] = "Quantidade (g)"
info2[2] = "Calorias (kcal)"
info2[3] = "Proteínas (g)"
info2[4] = "Carboidratos (g)"
info2[5] = "Gorduras (g)"  
"""
alimentos[info2[0]] = list()
alimentos[info2[0]].append(float(info2[1]))
alimentos[info2[0]].append(float(info2[2])/float(info2[1]))
alimentos[info2[0]].append((float(info2[3])/float(info2[1])))
alimentos[info2[0]].append((float(info2[4])/float(info2[1])))
alimentos[info2[0]].append((float(info2[5])/float(info2[1])))

datas = []


