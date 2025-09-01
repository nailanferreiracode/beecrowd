# -*- coding:utf-8 -*- 

qtd_segundos = int(input())

horas, qtd_segundos = divmod(qtd_segundos, 3600)
minutos, qtd_segundos = divmod(qtd_segundos, 60)
segundos = qtd_segundos

print(f"{horas}:{minutos}:{segundos}")

