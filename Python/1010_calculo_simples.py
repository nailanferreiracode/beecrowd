# -*- coding:utf-8 -*- 

QTD_VENDAS= 2
total_carrinho = 0
contador = 1

while(contador <= QTD_VENDAS):
    codigo, quantidade_pecas, valor_unitario = input().split()
    codigo = int(codigo)
    quantidade_pecas = int(quantidade_pecas)
    valor_unitario = float(valor_unitario)

    total_carrinho += quantidade_pecas * valor_unitario

    contador += 1

print(f"VALOR A PAGAR: R$ {total_carrinho:.2f}")
