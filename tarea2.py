'''
Created on Apr 22, 2016

@author:
        Jean Paul Alexander Lacour
        Diego Daniel Pedroza Pérez
'''

import math

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
