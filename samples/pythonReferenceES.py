# -*- coding: cp1252 -*-
## -*- coding: utf-8 -*-

# Esto es un comentario de una única línea
"""
Esto es un
comentario de
varias líneas
"""

print 'hello'
print 'Hello World desde España y olé' # Comprobando utf-8 :P
print "Bienvenido al \'resumen\' de Python"
print "Nueva línea: \n and y un pitido: \a"



# Definición de variables ###########
numero = 666
numeroNegativo = -42
numeroPI = 3.1415
nombre = "Pello"
otroNombre = "Pello Altadill"
letraA = 'a'
letraB = "b"
diosExiste = True
soyYo = False

# String de varias líneas
rezo = """Gods of war I call you,
my sword is by my side,
I seek a life of honor,
free from all false pride"""

# Asignación múltiple de variables
a = b = c = 0

# Podemos cambiar a otro tipo
a = True
c = 'Hola Python'

a = 10
b = -a
c = 42

# Podemos mostrar los valores
print numero
print c


# Operadores aritméticos
a = b + c
b = a - c
c = a * b
a = b / c # retorna valores con decimales
a = b // c # retorna resultado SIN decimales
modulo = a % c
potencia = a ** 3

# También está disponible este operador
a += b   # Equivale: a = a + b
b -= c   # Equivale: b = b - c
c *= a   # Equivale: c = c * a
a /= b   # Equivale: a = a / b
b %= 42  # Equivale: b = b % 42

# Operadores booleanos
laVerdad = diosExiste and soyYo
laVerdad = diosExiste or false
laVerdad = not diosExiste

# Operadored de comparación
sonIguales = a == b
noSonIguales = a!= b   # a <> b también sirve, pero está obsoleto
esMayor = a > b
esMenor = a < b
esMayorOIgual = a >= b
esMenorOIgual = a <= b

# Combinación de todos
superTrue = ( (a-1) > b) or (not(c == (b*4)))

# Concatenación de cadenas
# Usamos , en general para cualquier tipod e variables.
# Podemos usar + para cadenas
print "My name is " , nombre
print a , " - " , b , " - " , c

# Si queremos usar + con variables normales, debemos convertir a String
print str(a) + "," + str(b) + "," + str(c)
print rezo

# Otra manera
print "Un numero entero %d" % a
print "Un numero con decimales %f" % numeroPI
print "Una cadena o string %s" % nombre
#print "Un booleano %B" % diosExiste

# Para sacar múltiples variables
print ("a ver %d y otro %s y otro %d" % (a,nombre,c))

# Mediante del quitamos el valor a una variable
del rezo
# print rezo daría error!

# Condicionales #########################
# If único
if diosExiste:
	print "God is real unless declared integer"

## if de una única línea
if True:print 'Soy un if de una línea única'

cualquierCosa = '1'
if cualquierCosa:
	print "Sí, cualquier cosa distinta de 0 es True"

# 0, None, "", '', y las estructuras vacias (),[],{} son False
numeroCero = 0
if not numeroCero:
	print "0 es False"

# Podemos usar u omitar los paréntesis de la condición
if (a<b or b==c):
	print "a les menor que b o b es igual a c"


# if-else
if a > b:
	print "a es mayor que b"
else:
	print "a NO es mayor que b"

# elif
if a > b:
	print "a es mayor que b"
elif a < b:
	print "a es menor que b"
elif a == b:
	print "a y b son iguales"
elif a == 0:
	pass  # Esto es como decir que no hacemos nada
else:
	print "a y b son Alienígenas"

# NO EXISTE EL SWITCH CASE
# se puede simular con un if-elif

# Bucles ###########################
# while loop
c = 3
while c>0 :
	print "Un bucle while con c" , c
	c-=1

# for loop
# for i in range(inicio,fin), ojo NO llega a fin
# Y se va incrementando en 1
for x in range(0,5):
	print "Un bucle for con x " , x

# Con distinto tipo de incremento
# range(5) = [0, 1, 2, 3, 4]
# for (i in range(inicio,fin, incremento))
for x in range(0,10,2):
	print "for loop incremento en 2 con x " , x
for x in range(5,0,-1):
	print "for loop decremento en x " , x

# xrange(numero): desde 0 a numero
for x in xrange(5):  #  0..4
	print "probando xrange: " , x

nombre = 'Python mola'
for x in nombre:
	print "for loop con una cadena %x: " , x

# brea y continue nos sirven para alterar el funcionamiento de un bucle
# break: detiene la ejecucióin de un bucle y salimos fuera
buscarLaX = 'sdfXsaf'
for x in buscarLaX:
	if x == "X":
		print "Encontrada una X, salimos del bucle"
		break

# continue: dejamos de ejecutar la iteración o vuelta actual
# y pasamos a la siguiente vuelta del bucle, sin salir de él.
algunasVocales = '0a00i0e00u000a'
for x in algunasVocales:
	if x =='0':
		continue
	elif x =='a':
		print "a encontrada"
	elif x=='e':
		print "e encontrada"

# claúsula else
######
# Tras la ejecuxión de un for o un while, si todo ha ido normal y
# no ha habido interrupciones con break o excepciones o returns,
# se ejecutará lo que haya dentro del else
contador = 0
for x in algunasVocales:
	if x == 'a':
		contador += 1
else:
	print "Total de letras encontradas en " , algunasVocales , ": " , contador


# NO existe el do-while

# ESTRUCTURAS #############################
# Tuples = es una secuencia de elementos arbitrarios
# - IMMUTABLES una vez asignada un elemento no se puede cambiar
# - Están ordenados
algunosValores = (42, 15, 69)
otrosValores = ('Meaning', 42, True, -0.3)
nuevaTupla = tuple('aeiou') # this creates ('a','e','i','o','u')
tuplaVacia= ()

print "Primera: " , otrosValores[0]
print "Ultima: " , otrosValores[3]
print "Ultima, yendo atrás: " , otrosValores[-1]

# De este manera podemos agregar un elemento
otrosValores+= (34,56)
# ESTO NO SE PUEDE HACER, ya que una tupla ya es INMUTABLE
# otrosValores[0] = 'Satan'

# Se puede iterar o hacer un bucle con los valores de la Tupla
for v in otrosValores:
	print "Item de tupla: " , v

# Lists = Secuencia de items arbitrarios MUTABLE y ordenada
superLista = ['Python','Ruby','Go']
otraLista = ['God',666, True]
listaVacia = []

print "Primero: " , superLista[0]
print "Último: " , superLista[-1]

# De esta manera podemos agregar un elemento
superLista+= ['NodeJS']
# Y aquí SÍ lo podemos cambiar.
otraLista[0] = 'Satan'

for x in superLista:
	print "superLista : " , x

# Dictionaries = colección arbitraria de elementos, MUTABLES
# Son indexados por elementos arbitrarios (no siempre números)
# similares a hashtables, hash, maps, etc...
edades = {'Gandalf':1432, 'Aragorn':543, 'Bilbo':112}
diccionarioVacio = {}

# Podemos crearlos con una función dict
valoresTrig = dict(sin=34,cos=353.23,tan=34)
otrasEdades = dict([['Frodo',34],['Samwise',35]])

edades['Bilbo'] = 120
edades['Radagast'] = 1423

# iterating...
for clave in edades:
	print clave , " : " , edades[clave]

# Cortando secuencias
# Podemos acceder a una elemento con secuencia[indice]
# Para coger una parte de la secuencia podemos hacer:
#    sequence[inicio:longitud:salto]
# Ejemplos
puertos = [20, 21, 25, 80, 443, 110, 143];
puertosWeb = puertos[3:2] 		# [80, 443]
puertosFTP = puertos[:2]; 		# [20, 21]
algunosPuertos = puertos[1:6:2] 	# [21, 80, 110]

# Los Strings o cadenas son IMMUTABLES!!
# Por lo tanto hacer esto es ilegal.
# miNombre[0] = 'L'

# También se pueden cortar de la misma manera
miNombre = "Pello Xabier Altadill Izura"

print miNombre[0] , " name: " , miNombre[:5]

# Definición de funciones #################
def hola():
	print "hola"

def sumar(a,b):
	return a+b

def esPar(a):
	return (a%2==0)

def valoresPorDefecto(a, b=0, c=42):
	result = a + b - c
	print "Valores de parámetros: "
	print "a es " , a
	print "b es " , b
	print "c es " , c
	return result

# Llamando a funciones
hola
hola()
a = sumar(600,66)
print "Resultado de suma: " , sumar(a,b)
b = esPar(a)
print "Resultado es esPar para " , a , ": " , b

valoresPorDefecto(5)
valoresPorDefecto(15,-5)

