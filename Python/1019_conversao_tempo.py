# -*- coding:utf-8 -*- 

qtd_segundos = int(input())

horas = qtd_segundos // 3600
qtd_segundos = qtd_segundos-horas*3600
minutos = qtd_segundos // 60
qtd_segundos = qtd_segundos-minutos*60
segundos = qtd_segundos

print(f"{horas}:{minutos}:{segundos}")

