#Importamos nuestro modulo matematica.py y ya podemos usar sus funciones
#Ambos archivos, tanto matematica.py que es nuestro modulo y
#calculo.py deben estar en la misma carpeta

import matematica #Esta es la manera mas simple de lograr la moudlaridad y
                  #requiere que ambos archivos, tanto matematica.py
                  #que es nuestro modulo y calculo.py esten en la misma carpeta

#para usar las funciones del modulo matematica.py es necesario
#anteponer el nombre del modulo seguido de la funcion que se va utilizar
#ejemplo: mi_modulo.mi_funcion()
#para evitar escribir el nombre completo del modulo en la importacion
#debemos escribir adicionalmente as mi_mod
#ejemplo: import matematica as mates
#se dice entonces que mates es un alias para el modulo matematica.py

print(matematica.sumar(5,3)) #salida: 8
print(matematica.restar(5,3)) #salida: 2

#al ejecutarse este programa dentro de la carpeta donde se almacenan
#ambos archivos se creara una carpeta __pycache__
