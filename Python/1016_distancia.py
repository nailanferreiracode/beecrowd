# -*- coding:utf-8 -*- 

VELOCIDADE_CARRO_01 = 60 
VELOCIDADE_CARRO_02 = 90 

DIFERENCA = abs(VELOCIDADE_CARRO_01 - VELOCIDADE_CARRO_02)
DIFERENCA_KM_HORA = DIFERENCA / 60

qtd_km_percorridos = int(input())


print(f"{qtd_km_percorridos //  DIFERENCA_KM_HORA:.0f} minutos")

