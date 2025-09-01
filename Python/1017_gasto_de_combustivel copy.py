# -*- coding:utf-8 -*- 

CONSUMO_MEDIO = 12

qtd_hrs_viagem = int(input())
media_km_hora = int(input())

print(f"{(qtd_hrs_viagem *  media_km_hora)/CONSUMO_MEDIO:.3f}")

