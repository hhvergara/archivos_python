#!/usr/bin/env python
'''
Archivos [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para que practiquen los conocimietos
adquiridos durante la semana
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"


import csv
import re

# InoveTip: El nombre de la funcion no me termina de decir a que convierte
# el time, porque lo convierte a ¿¿time??, sugerencias
# strtime_to_time
# time_to_seconds
def time_to_time(time="00:00:00"):
    """
    Recibe el horario en formato string 00:00:00 (horas:minutos:segundos)
    y lo devuelve en formato int en segundos
    """
    
    #int_time = 0
    if time == "":
        return 0
    else:
        
        time_list = list(time.split(":"))
        map(int(), time_list)
        return int(time_list[0]) * 3600 + int(time_list[1]) * 60 + int(time_list[2])
        '''
        int_time = (int (time [7])) + (int(time [6]) * 10) 
        int_time += (int (time [4]) + (int (time [3]) * 10)) * 60
        int_time += (int (time [1]) + (int (time [0]) * 10)) * 3600
        return int_time
        '''
            # InoveTip: En este caso en vez de sumar los caracteres por separados es más
    # práctico y seguro usar split(':') y obtener así la hora, minuto, segundos
    # ya armados como string para pasar a numero. Es más seguro por si te llega a venir
    # en un caso hipotetico 6:30:15 en vez de 06:30:15

# InoveTip: A modo sintazis lo ideal seria:
# def dataset_get_time(dataset="", column="Division", category="MPRO", activity="Swim"):
# Se que es engorroso pero cada tanto copiate el código en "pep8online" para chequear estas cosas
# porque muchos "recluters" lo primero que hacen es correr tu código en un unittest de pep8,
# no te digo que de 100% bien la sintaxis pero al menos lo esperable si, quiero decir con esto
# que podes tener alguna linea de código de más de 79 caracteres pero no estos casos que visualmente
# se notan a la legua


def dataset_get_time(dataset="", column="Division", category="MPRO", activity="Swim"):
    """
    La función busca dentro el csv la columna deseada, filtra por categoría de esta columna
    y devuelve los valores de max, min y promedio de tiempo en segundos con formato int. del campo deseado.
    """
    posicion = 0
    promedio = 0
    tiempo_int = 0
    acumulador = 0
    hit_row=[]
    registro_de_tiempos = []
    times = []
    # Lectura de archivo CSV con diccionario
    with open(dataset) as csvfile:
        data = list(csv.DictReader(csvfile))
        
    for i in range(len(data)):
        row = data[i]
        division = str(row.get(column))
        if division == category:
            tiempo_int = time_to_time(str(row.get(activity)))
            if tiempo_int != 0:
                # InoveTip
                # -----------------------------------------------
                registro_de_tiempos.insert(posicion,tiempo_int)
                hit_row.insert(posicion,i)
                posicion += 1
                # Veo que no hay un suo posterior de "posicion" y solo se
                # usa para colocar los elementos en las listas,
                # y por otro lado veo que siempre es incremental.
                # En este caso donde "posicion" no se le está dando
                # otro uso y siempre es incremental utilizar directamnete
                # el método append
                # -----------------------------------------------
                acumulador += tiempo_int
                # Veo que se está calculando el promedio en cada vuelta de loop
                # pero finalmente le promedio se usa el salir del loop,
                # lo más eficiente es diretamente realizar el promedio
                # fuera del loop
                promedio= acumulador / len(hit_row) # Ojo con ese signo igual (sintaxis) :)
    times.insert(0,min(registro_de_tiempos))
    times.insert(0,max(registro_de_tiempos))
    times.insert(2,promedio)
    csvfile.close()
    return times

def ej1():
    print("Cuenta caracteres")
    cantidad_letras = 0

    '''
    Realizar un prorgrama que cuenta la cantidad de caracteres
    (todo tipo de caracter, los espacios cuentan) de un archivo.
    Abra el archivo "text.txt" en modo "lectura", lea linea a
    linea el archivo, y cuente la cantidad de caracteres de cada línea.
    Debe realizar la sumatoria total de la cantidad de caracteres de todas
    las líneas para obtener el total del archivo e imprimirlo en pantalla
    '''

    fi = open('texto.txt', 'r')
    line = fi.readline()

    with open('texto.txt') as fi:
        for line in fi:
            cantidad_letras += len(line)
        print('cantidad de letras:', cantidad_letras)
    fi.close()

def ej2():
    print("Transcribir!")
    cantidad_letras = 0
    entrada_texto = ""
    '''
    Deberá abrir un archivo txt para escritura (un archivo nuevo)
    Luego mediante un bucle deberá pedir por consola que
    se ingrese texto. Todo el texto ingresado por consola
    debe escribirse en el archivo txt, cada entrada de texto
    deberá ser una línea en el archivo.
    El programa termina cuando por consola no se ingresa
    nada (texto vacio). En ese momento se termina el bucle
    y se cierra el archivo.
    Durante la realización del bucle y el ingreso de texto por
    consola, se debe ir contanto cuandos caracteres se ingresaron
    por consola, al fin de al terminar el bucle saber cuantos
    caracteres se copiaron al archivo.
    NOTA: Recuerde agregar el salto de línea "\n" a cada entrada
    de texto de la consola antes de copiar la archivo.
    '''
    fo = open('nuevo.txt', 'w')
    while (1):
        entrada_texto = str (input("ingrese texto:\n"))
        cantidad_letras += len (entrada_texto)
        if entrada_texto != "":
            
            fo.write(entrada_texto + "\n")
        else:
            break
    print("la cantidad de caracteres ingresados es de:",cantidad_letras)
    fo = fo.close()

def ej3():
    print("Escrutinio de los alquileres de Capital Federal")
    cantidad_ambientes = 2
    hint_row = []
    promedio = 0
    lista_de_precios = []



    '''
    Realizar un prorgrama que solicite la cantidad de
    ambientes de los alquileres que se desean analizar.
    Abra el archivo "propiedades.csv" y mediante un bucle analizar:
    1) Contar cuantos alquileres en "pesos" hay disponibles
    en la cantidad de ambientes deseados.
    2) Obtener el promedio del valor de los alquileres en "pesos"
    de la cantidad de ambientes deseados.
    3) Obtener el máximo valor de alquiler en "pesos"
    de la cantidad de ambientes deseados.
    4) Obtener el mínimo valor de alquiler en "pesos"
    de la cantidad de ambientes deseados.
    '''

    promedio = 0
    # Lectura de archivo CSV con diccionario
    with open('propiedades.csv') as csvfile:
        data = list(csv.DictReader(csvfile))
    
    #Obtenemos la posición de las filas en pesos y con cantidad de ambientes deseados:
    posicion = 0
    for i in range(len(data)):
        row = data[i]
        moneda = str(row.get('moneda'))
        ambientes = str(row.get('ambientes'))
        precio = float(row.get("precio"))


        if moneda == "ARS" and ambientes == str(cantidad_ambientes):
            hint_row.insert (posicion,i)
            lista_de_precios.insert(posicion,precio)
            posicion += 1   # InoveTip:  Mismo tip de append (ver comentario más arriba)
            # InoveTip:  No me puse a hacer la equivalencia, pero este promedio por sumas sucesivas
            # en donde el "len" va variando, es equivalente al promedio real??
            promedio += precio
            promedio/= len(hint_row)
    # 1.
    print("la cantidad de alquileres en pesos es:",len(hint_row))
    # 2.
    print("El promedio es de AR$",promedio)
    # 3.
    print("El precio minimo es de AR$:",min(lista_de_precios))
    # 4.
    print("El precio máximo es de AR$:",max(lista_de_precios))

def ej4():
    print("Ahora sí! buena suerte :)")
    
    '''
    Para poder realizar este ejercicio deberán descargarse el
    dataset "2019 Ironman world championship results" del siguiente
    link:
    https://www.kaggle.com/andyesi/2019-ironman-world-championship-results/data#

    Una vez tengan descargado el archivo CSV lo pueden observar un poco.
    En principio le daremos importancia a las siguientes columnas:

    Division: Esta columna marca la divisón del corredor por experiencia o edad.
    Swim: Tiempo nadando
    Bike: Tiempo en bicicleta
    Run: Tiempo corriendo

    Queremos investigar las siguientes divisiones o categorias:
    - MPRO
    - M45-49
    - M25-29
    - M18-24

    De cada una de estas categorías de corredores deseamos que analices
    por separado el tiempo de Swim, Bike y Run. En cada caso (para los 3)
    se desea obtener
    1) El tiempo máximo realizado por un corredor en dicha categoria
    2) El tiempo mínimo realizado por un corredor en dicha categoria
    3) El tiempo promedio de dicha categoria

    Es decir, por ejemplo voy a investigar la categoria M45-49 en "Run"
    - Debo buscar de todos los M45-49 cual fue el mayor tiempo en Run
    - Debo buscar de todos los M45-49 cual fue el menor tiempo en Run
    - Debo buscar de todos los M45-49 el tiempo Run y calcular el promedio

    Para poder realizar este ejercicio necesitará muchas variables para almacenar
    los datos, puede organizarse como mejor prefiera, en listas, con diccionarios,
    lo que se sienta más comodo.

    Es valido recorrer todo el archivo para extrer la información ordenada
    y almacenarlas en listas según el criterio que escojan.

    NOTA:
    Recomendamos empezar de a poco, los primeros ensayos realizarlo
    con una sola categoría de edad en solo una sección (Bike, Run, Swim)
    de la carrera. Sería igual al ej4 la información recolectada y calculada.

    NOTA IMPORTANTE:
    En este ejercicio se pide calcular el promedio, el máximo y mínimo tiempo
    que realizaron los corredores en distintas etapas de la carrera.
    La dificultad radica en que el dato que el archivo nos provee está
    en el siguiente formado:

    hora:minutos:segundos, 0:47:27 --> (0 horas, 47 minutos, 27 segundos).

    No pueden utilizar este valor para calcular el promedio, el máximo
    y mínimo ya que está en formato texto, no está en formato numérico.
    Para poder realizar cálculos matemáticos sobre este dato deben primero
    llevarlo a un formato que les permita realizar cálculos.

    Normalmente en estos casos lo que se realiza es llevar este dato
    0:47:27 a segundos, es decir, calcular cuantos segundos le llevó
    al corredor completar esa etapa, ya que segundos es la unidad mínima
    presentada (horas, minutos, segundos).

    Para poder calcular la cantidad de segundos totales deberían operar
    de la siguiente forma:

    segundos_totales = horas * 3600 + minutos * 60 + segundos

    De esta forma están pasando de un formato texto horas:minutos:segundos a
    un número "segundos_totales" el cual pueden calcular
    promedio, máximo y mínimo
    
    Queda en sus manos pensar como extraer las "horas" "minutos" y "segundos"
    del formato "horas:minutos:segundos", 
    pueden realizar operaciones de texto ahí, o usar algún módulo externo
    de Python que resuelva este problema.

    '''
    dataset = "datasets_575912_1042673_2019 Ironman World Championship Results.csv"
    actividad = ["Swim","Bike","Run"] # InoveTip: si es una lista mejor poner el nombre en plural
    categoria = ["MPRO","M45-49","M25-29","M18-24"] # InoveTip: si es una lista mejor poner el nombre en plural


    for i in range(len(categoria)):
        print("----------------------------------\n")
        # InoveTip: Veo que el loop va de 0 a 2, y solo se usa ese "iterador" para acceder a las actividades,
        # en ese caso donde solo se usa para acceder a las actividades, queda totalmente explicito y más legible
        # realizar el bucle con:
        # for actividad in actividades:
        #     time = dataset_get_time(dataset,"Division",categoria[i],actividad)
        # Mismo comentario apra categoria --> for categoria in categorias:
        for k in range(len(actividad)):
            time = dataset_get_time(dataset,"Division",categoria[i],actividad[k])
            print("Categoría:",categoria[i],"Actividad:",actividad[k],"\nTiempo [minutos]:")
            #print("maximo:",time[0]/60,", mínimo:",time[1]/60,", promedio:",time[2]/60)
            print("maximo:{0:.2f}, mínimo:{1:.2f}, promedio:{2:.2f}".format((time[0]/60),(time[1]/60),(time[2]/60)))


if __name__ == '__main__':
    print("Ejercicios de práctica")
    #ej1()
    #ej2()
    #ej3()
    ej4()
