# -*- coding:utf-8 -*- 

PI = 3.14159
val_a, val_b, val_c = input().split()
val_a = float(val_a)
val_b = float(val_b)
val_c = float(val_c)

resultado_triangulo = (val_a * val_c)/2
resultado_circulo =  PI * (val_c **2)
resultado_trapezio = ((val_a + val_b) * val_c) / 2
resultado_quadrado = (val_b * val_b)
resultado_retangulo = (val_a * val_b)

print(f"TRIANGULO: {resultado_triangulo:.3f}")
print(f"CIRCULO: {resultado_circulo:.3f}")
print(f"TRAPEZIO: {resultado_trapezio:.3f}")
print(f"QUADRADO: {resultado_quadrado:.3f}")
print(f"RETANGULO: {resultado_retangulo:.3f}")