#Variables primitivas
calificaciones = 3.5 #float
edad = 25 #int
nombre = "Johan" #String
hombre = True #boolean

concatenacion = str(calificaciones) + str(edad) + nombre + str(hombre)
print("Variables concatenadas:", concatenacion)

#Limites de los enteros:

# En Python 2, los enteros son de tamaño fijo y generalmente están limitados por la arquitectura de la 
# máquina. En la mayoría de los sistemas, los enteros suelen ser de 32 bits, lo que significa que el rango 
# va desde -2,147,483,648 hasta 2,147,483,647 en sistemas de 32 bits, y desde -9,223,372,036,854,775,808 
# hasta 9,223,372,036,854,775,807 en sistemas de 64 bits.

#En Python 3, los enteros son de tamaño variable y pueden ser muy grandes, limitados solo por la cantidad 
# de memoria disponible en la máquina. Esto significa que puedes trabajar con enteros mucho más grandes en 
# Python 3 sin preocuparte por los límites específicos de la arquitectura.

#Limites de los flotantes: 

#Python utiliza el estándar de punto flotante de doble precisión IEEE 754 para representar números de 
# punto flotante (floats) de 64 bits. Esto proporciona aproximadamente 15-17 dígitos de precisión decimal.

#El valor mínimo positivo no nulo que se puede representar en un float de 64 bits es del orden de 1e-308, 
# y el valor máximo es del orden de 1e308.

#Python también tiene constantes especiales para representar valores especiales de punto flotante, como 
#infinito positivo (float('inf')), infinito negativo (float('-inf')) y NaN (Not a Number).

numeros_pares = edad*(edad + 1)
print ("Primeros N Numeros Pares:", numeros_pares)