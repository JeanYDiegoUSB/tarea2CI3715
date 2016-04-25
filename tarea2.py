'''
Created on Apr 22, 2016

@author:
        Jean Paul Alexander Lacour
        Diego Daniel Pedroza Pérez
'''

import math
from datetime import datetime 

'''
    Clase Tarifa
'''
class Tarifa(object) :
    #inicializacion
    def __init__(self,semana,fin) :
        self.semana = semana
        self.fin = fin

    #metodo para obtener el valor del campo semana
    def getSemana(self) :
        return self.semana
    
    #metodo para obtener el valor del campo fin
    def getFin(self) :
        return self.fin
'''
    Metodo para saber si un anio es bisiesto
'''
def bisiesto(year) :
    if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0) :  
        return True  
    else :  
        return False 

'''
    Metodo para saber el ultimo dia de un mes
    dado el mes y el anio
'''
def maxDay(month, year) :
    if month in [1,3,5,7,8,10,12] :
        return 31
    elif month in [4,6,9,11] :
        return 30
    else :
        if bisiesto(year) :
            return 29
        else :
            return 28

'''
    Metodo para calcular el monto a pagar por un trabajo
    dado un objeto Tarifa y un intervalo tiempoDeTrabajo
'''
def calcularPrecio(tarifa, tiempoDeTrabajo) :
    inicio,fin = tiempoDeTrabajo[0],tiempoDeTrabajo[1] # fechas de inicio y fin del trabajo

    #Si los anios, meses y dias son iguales
    if inicio.year == fin.year and inicio.month == fin.month and inicio.day == fin.day :
        #diferencia entre los horarios
        dif = fin.hour - inicio.hour
        if dif >= 0.25 :
            return tarifa.getSemana() * math.ceil(dif)
    #Si los anios y meses son iguales
    elif inicio.year == fin.year and inicio.month == fin.month :
        #diferencia entre los dias, se suma la hora en que termina el trabajo
        # y se resta la hora en que inicia
        dif = math.ceil(24 * (fin.day - inicio.day) - inicio.hour + fin.hour)
        #verificar que no se pasa del limite establecido
        if dif <= 168 :
            return tarifa.getSemana() * dif
    #Si los anios son iguales
    elif inicio.year == fin.year :
        #Si son meses seguidos
        if fin.month - inicio.month == 1 :
            #cantidad de dias entre las dos fechas
            dias = maxDay(inicio.month,inicio.year) + fin.day - inicio.day 
            #verificar que no se pasa del limite establecido
            if dias <= 7 :
                dif = math.ceil(24 * dias - inicio.hour + fin.hour)
                #verificar que no se pasa del limite establecido
                if dif <= 168 :
                    return tarifa.getSemana() * dif
    #Si los anios son diferentes
    elif inicio.year != fin.year :
        #Si el mes de inicio es diciembre y el mes de fin es enero
        if inicio.month == 12 and fin.month == 1 :
            #cantidad de dias entre las dos fechas
            dias = 31 + fin.day - inicio.day
            #verificar que no se pasa del limite establecido
            if dias <= 7 :
                dif = math.ceil(24 * dias - inicio.hour + fin.hour)
                #verificar que no se pasa del limite establecido
                if dif <= 168 :
                    return tarifa.getSemana() * dif
    #Si no trabaja lo suficiente o trabaja de más
    return 0

'''
    Funcion para saber cuantas horas son de tipo semana
    y cuantas son de tipo fin de semana. Recibe 
    un tiempoInicial y un tiempFinal de tipo datetime
    y devuelve un arreglo de enteros [horaSemana,horaFinSemana]
'''
def tipoHoraMesIgual(inicio,fin):
    arreglo = [0,0]            #Creando el arreglo [horaSemana,horaFinSemana]
    
    #Si los dias no son iguales
    if inicio.day!=fin.day :
        #Verifico que dia(si es fin de semana o no) y guardo la cantidad de horas en el espacio 
        #correspondiente
        x=inicio.weekday();
        if(x<=4):     
            arreglo[0]=24-math.ceil(inicio.hour+(inicio.minute)/100)
        else:
            arreglo[1]=24-math.ceil(inicio.hour+(inicio.minute)/100)

        #Veo que dia de la semana es dia siguiente del inicio
        if x == 6 :
            x = 0
        else:
            x +=1
        b=1
        totalDias = fin.day-inicio.day

        # Mientras no he revisado todos los dias que hay entre el dia
        #siguiente del inicio y el final, voy agregando las horas
        #de los días, teniendo en cuenta el tipo de día que es.   
        while(b < totalDias):
            if x<5 :
                arreglo[0]+=24
                x+=1
            else:
                arreglo[1]+=24
                if x==6 :
                    x=0
                else:
                    x+=1
            b+=1

        #Reviso el ultimo dia
        if(fin.weekday()<5):
            arreglo[0]+=math.ceil(fin.hour+(fin.minute/100))
        else:
            arreglo[1]+=math.ceil(fin.hour+(fin.minute/100))


    #Si los dias son iguales
    else:
        horasTotal=fin.hour-inicio.hour
        #Se cobra por hora completa
        if(fin.minute!=0 or inicio.minute!=0):
            if(inicio.minute!=0):
                horasTotal+=1
            if(fin.minute!=0):
                horasTotal+=1

        if(inicio.weekday()<5):
            arreglo[0]=horasTotal
        else:
            arreglo[1]=horasTotal


    return arreglo

'''
    Funcion para saber cuantas horas son de tipo semana
    y cuantas son de tipo fin de semana. Recibe 
    un tiempoInicial y un tiempFinal de tipo datetime
    y devuelve un arreglo de enteros [horaSemana,horaFinSemana]
'''
def tipoHoraMesDistintos(inicio,fin):
    arreglo = [0,0]            #Creando el arreglo [horaSemana,horaFinSemana]
    maxInit=maxDay(inicio.month,inicio.year)
    diaFin=maxInit+fin.day
    totalDias=diaFin-inicio.day
    #Verifico que dia(si es fin de semana o no) y guardo la cantidad de horas en el espacio 
    #correspondiente
    x=inicio.weekday();
    if(x<=4):     
        arreglo[0]=24-math.ceil(inicio.hour+(inicio.minute)/100)
    else:
        arreglo[1]=24-math.ceil(inicio.hour+(inicio.minute)/100)


    #Veo que dia de la semana es el dia siguiente del inicio
    if x<5:
        if x==6:
            x=0
        else:
            x+=1
    else:
        x+=1
    b=1;

    # Mientras no he revisado todos los dias que hay entre el dia
    #siguiente del inicio y el final, voy agregando las horas
    #de los días, teniendo en cuenta el tipo de día que es.   
    while(b < totalDias):
        if x<5 :
            arreglo[0]+=24
            x+=1
        else:
            arreglo[1]+=24
            if x==6 :
                x=0
            else:
                x+=1
        b+=1

    #Reviso el ultimo dia
    if(fin.weekday()<5):
            arreglo[0]+=math.ceil(fin.hour+(fin.minute/100))
        else:
            arreglo[1]+=math.ceil(fin.hour+(fin.minute/100))



    return arreglo



if __name__ == "__main__":
    sem = int(input("Introduzca tarifa de la semana: "))
    finSem = int(input("Introduzca tarifa del fin de semana: "))
    tiempInit= str(input(
        "Introduzca tiempoDeTrabajo Inicial\nSepare mediante comas\nyear,month,day,hour,minutes:  "
    ))
    tiempFin= str(input(
        "Introduzca tiempoDeTrabajo Final\nSepare mediante comas\nyear,month,day,hour,minutes:  "
    ))
    a= tiempInit.split(",")
    b =tiempFin.split(",")
    try:
        tiempoWorkInit=datetime(int(a[0]),int(a[1]),int(a[2]),int(a[3]), int(a[4]), 0, 0,None)
    except (TypeError,IndexError,ValueError):
        print("Error! de Tipo")
    try:
        tiempoWorkFin= datetime(int(b[0]),int(b[1]),int(b[2]),int(b[3]), int(b[4]), 0, 0,None)
    except (TypeError,IndexError,ValueError):
        print("Error! de Tipo")
    tarifa = Tarifa(sem,finSem);
    tiempoDeTrabajo=[tiempoWorkInit,tiempoWorkFin]
    
    c=tipoHoraMesDistintos(tiempoWorkInit,tiempoWorkFin)
    print("Horas_Sem: "+str(c[0])+" Horas Fin: "+str(c[1]))
   
    print("SALIENDO")
    

