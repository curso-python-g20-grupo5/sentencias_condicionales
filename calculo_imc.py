"""
En busca de mejorar la salud nutricional de los pacientes, se le solicita a usted como
programador el hecho de diseñar una herramienta que permita determinar el estado
nutricional de una persona utilizando el cálculo del IMC, para ello, la 
Organización Mundial de la Salud (OMS) ha determinado una clasificación así
para distintos rangos de valores.
"""

#ingreso de variables
peso = float(input('Ingresa tu peso en kilogramos: '))
altura = int(input('Ingresa tu altura en centímetros: '))

#transformación de altura, de cm a mt
altura_mt = altura/100

#cálculo del IMC e impresión por consola del resultado
imc = peso / (altura_mt ** 2)
print("--------------------------------------------------------------------")
print(f"------Tu Índice de Masa Corporal (IMC) es: {imc:.2f}------")

#categorización del IMC e impresión por consola del resultado

if imc < 18.5:
    print( "------Su clasificación sgún la OMS es Bajo Peso------")
elif 18.5 <= imc and imc <25:
    print( "------Su clasificación sgún la OMS es Adecuado-------")
elif 25 <= imc and imc <30:
    print( "------Su clasificación sgún la OMS es Sobrepeso------")
elif 30 <= imc and imc < 35:
    print( "------Su clasificación sgún la OMS es Obesidad grado I------")
elif 35 <= imc and imc < 40:
    print( "------Su clasificación sgún la OMS es Obesidad grado II------")
else:
    print( "------Su clasificación sgún la OMS es Obesidad grado III------")

print("--------------------------------------------------------------------")