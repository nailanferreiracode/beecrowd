# -*- coding: utf-8 -*- 

peso_a = 3.5
peso_b = 7.5
soma_pesos = peso_a + peso_b

nota_a = float(input())
nota_b = float(input())

media = ((nota_a * peso_a) + (nota_b * peso_b)) / soma_pesos

print(f"MEDIA = {media:.5f}")