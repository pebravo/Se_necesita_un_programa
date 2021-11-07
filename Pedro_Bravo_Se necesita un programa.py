import math

#llamado por teclado para los numeros a calcular
primer_numero = int(input('ingrese un numero: '))
segundo_numero = int(input('ingrese un numero: '))

print('-----------------Suma-----------------')
print('el resultado de la suma entre:',primer_numero, 'y',segundo_numero, 'es:',primer_numero + segundo_numero)


print('-----------------Resta-----------------')
print('el resultado de la resta entre:',primer_numero, 'y',segundo_numero, 'es:',primer_numero - segundo_numero)


print('-----------------Multiplicacion-----------------')
print('el resultado de la multiplicacion entre:',primer_numero, 'y',segundo_numero, 'es:',primer_numero * segundo_numero)     


print('-----------------Division-----------------')
if(segundo_numero == 0):
    print('no se puede dividir por 0')
else:
    print('el resultado de la division entre:',primer_numero, 'y',segundo_numero, 'es:',primer_numero / segundo_numero)

print('-----------------Raiz Cuadrada-----------------')  
raiz1= math.sqrt (primer_numero)
raiz2= math.sqrt (segundo_numero)

print('la raiz cuadrada del primer numero',primer_numero,'es: ',raiz1)
print('la raiz cuadrada del segundo numero',segundo_numero, 'es: ',raiz2)

print('-----------------Potencias-----------------')
print(primer_numero, 'elevado a',segundo_numero, 'es:',primer_numero **segundo_numero)

print('-----------------Cuetionario-----------------')
nombre = input('¿Cual es su Nombre?: ')
nota= float(input('califice con una nota al programa: '))
descripcion= input('argumente la nota: ')

print('-----------------Respuesta cuestionario-----------------')
print('¿Nombre del usuario del programa?: ',nombre,)
print('Nota de calificación del programa: ',nota,)
print('Descripción de la calificación: ',descripcion)

















    
