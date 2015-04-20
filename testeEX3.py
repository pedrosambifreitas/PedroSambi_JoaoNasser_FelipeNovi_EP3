# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt    #importa função para fazer gráficos
import datetime

doc_us = open('usuario.csv')           #abrindo o arquivo
doc_us.readline()                      #lê a primeira linha, que não será usada
linha_principal = doc_us.readline()    #lê a segunda linha, sendo ela a que contêm as informações a ser usadas
lp = linha_principal.strip()           #limpa o /n da linha principal
info = lp.split(',')                   #forma lista com as informações
doc_us.readline()
comeu = doc_us.readlines()
c = []
for i in comeu:
    c.append(i.strip())
    
for i in range(len(c)):
    c[i] = c[i].split(',')
    c[i][2] = float(c[i][2])
print(c)
print(info)

nome = info[0]
idade = float(info[1])
peso = float(info[2])
sexo = info[3]
altura = float(info[4])*100
fator = info[5]

print(nome,idade,peso,sexo,altura,fator)

if sexo == ('M' or 'masc' or 'masculino' or 'm' or 'Masculino' or 'Masc'):         #equação para homens
    TMB = 88.36 + (13.14*peso) + (4.8*altura) - (5.7*idade)
if sexo == ('F' or 'femin' or 'feminino' or 'f' or 'Feminino' or 'Femin' or 'fem' or 'Fem'): #equação para mulheres
    TMB = 447.6 + (9.2*peso) + (3.1*altura) - (4.3*idade)
    
if fator == ('minimo' or 'Minimo'):
    cal = TMB*1.2
if fator == ('baixo' or 'Baixo'):
    cal = TMB*1.375
if fator == ('médio' or 'Médio'):
    cal = TMB*1.55
if fator == ('alto' or 'Alto'):
    cal = TMB*1.725
if fator == ('muito alto' or 'Muito alto'):
    cal = TMB*1.9
    
print(cal)

doc_al = open('alimentos.csv','r+')
linhas = doc_al.readlines()

linhas_limpas = []                            #limpando linhas do arquivo dos alimentos
for i in linhas:
    linhas_limpas.append(i.strip())

alimentos = dict()

for l in linhas_limpas[1:]:                        #Dicionario com todos os alimentos
    p = l.split(',')
    """ 
    p[0] = 'nome'
    p[1] = 'quantidade'
    p[2] = 'calorias'
    p[3] = 'proteinas'
    p[4] = 'carboidratos'
    p[5] = 'gorduras'  
    z = 'calorias/quantidade'
    """
    alimentos[p[0]] = list()
    alimentos[p[0]].append(float(p[1]))
    alimentos[p[0]].append(float(p[2])/float(p[1]))
    alimentos[p[0]].append((float(p[3])/float(p[1])))
    alimentos[p[0]].append((float(p[4])/float(p[1])))
    alimentos[p[0]].append((float(p[5])/float(p[1])))

datas = []
    
for i in range(len(c)):
    datas.append(c[i][0])

print(datas)

for i in range(len(c)):
    if c[i][1] in alimentos.keys():
        calo = (alimentos[c[i][1]][1])
        gord = (alimentos[c[i][1]][4])
        prot = (alimentos[c[i][1]][2])
        carb = (alimentos[c[i][1]][3])
        
        cal_total = c[i][2]*calo
        gord_total = c[i][2]*gord
        prot_total = c[i][2]*prot
        carb_total = c[i][2]*carb
    
valores_diarios = {}

for m in datas:                        #Dicionario com as datas
    q = m.split(',')
    """ 
    q[0] = 'data'
    
    """
    valores_diarios[q[0]] = list()
        
print(valores_diarios)