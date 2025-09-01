# -*- coding:utf-8 -*- 
import math 

def cadastra_pontos():
    contador = 0 
    qtd_iteracoes = 2
    pontos_informacoes = []
    while(contador < qtd_iteracoes):
        pontos_informacoes.append(list(map(float, input().split())))
        contador = contador + 1

    return pontos_informacoes

def calcula_distancia_pontos(pontos):
    distancia = math.sqrt((pontos[0][0] - pontos[1][0])**2 + (pontos[0][1] - pontos[1][1])**2)
    return distancia


info_pontos = cadastra_pontos()
resutado = calcula_distancia_pontos(info_pontos)
print(f"{resutado:.4f}")