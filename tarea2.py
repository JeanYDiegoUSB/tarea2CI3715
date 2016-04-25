'''
Created on Apr 22, 2016
@author:
        Jean Paul Alexander Lacour
        Diego Daniel Pedroza Perez
'''
from datetime import datetime
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
    
    #metodo para ver que tarifa usar
    def cualTarifa(self, fecha) :
        if fecha.weekday() in [0,1,2,3,4] :
            return self.getSemana()
        elif fecha.weekday() in [5,6] :
            return self.getFin()
    
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
    monto = 0
    #Si los anios, meses y dias son iguales
    if inicio.year == fin.year and inicio.month == fin.month and inicio.day == fin.day :
        #diferencia entre los horarios
        dif = fin.hour - inicio.hour + (fin.minute - inicio.minute)/60
        if dif >= 0.25 :
            return tarifa.cualTarifa(inicio) * math.ceil(dif)
    #Si los anios y meses son iguales
    elif inicio.year == fin.year and inicio.month == fin.month :
        #diferencia entre los dias, se suma la hora en que termina el trabajo
        # y se resta la hora en que inicia
        dif = math.ceil(24 * (fin.day - inicio.day) - inicio.hour + fin.hour + (fin.minute - inicio.minute)/60)
        #verificar que no se pasa del limite establecido
        if dif <= 168 :
            monto += math.ceil(24 - inicio.hour - inicio.minute/60) * tarifa.cualTarifa(inicio)
            d = inicio.day + 1
            while d != fin.day :
                aux = datetime(inicio.year,inicio.month,d)
                monto += 24 * tarifa.cualTarifa(aux)
                d += 1
            monto += math.ceil(fin.hour + fin.minute/60) * tarifa.cualTarifa(fin)
            return monto
    #Si los anios son iguales
    elif inicio.year == fin.year :
        #Si son meses seguidos
        if fin.month - inicio.month == 1 :
            #cantidad de dias entre las dos fechas
            dias = maxDay(inicio.month,inicio.year) + fin.day - inicio.day 
            #verificar que no se pasa del limite establecido
            if dias <= 7 :
                dif = math.ceil(24 * dias - inicio.hour + fin.hour + (fin.minute - inicio.minute)/60)
                #verificar que no se pasa del limite establecido
                if dif <= 168 :
                    monto += math.ceil(24 - inicio.hour - inicio.minute/60) * tarifa.cualTarifa(inicio)
                    d = inicio.day + 1
                    m = inicio.month
                    while dias != 1 and d != fin.day :
                        aux = datetime(inicio.year,m,d)
                        monto += 24 * tarifa.cualTarifa(aux)
                        if d == maxDay(inicio.month, inicio.year) :
                            m = fin.month
                            d = 0
                        d += 1
                    monto += math.ceil(fin.hour + fin.minute/60) * tarifa.cualTarifa(fin)
                    return monto
    #Si los anios son diferentes
    elif inicio.year != fin.year :
        #Si el mes de inicio es diciembre y el mes de fin es enero
        if inicio.month == 12 and fin.month == 1 :
            #cantidad de dias entre las dos fechas
            dias = 31 + fin.day - inicio.day
            #verificar que no se pasa del limite establecido
            if dias <= 7 :
                dif = math.ceil(24 * dias - inicio.hour + fin.hour + (fin.minute - inicio.minute)/60)
                #verificar que no se pasa del limite establecido
                if dif <= 168 :
                    monto += math.ceil(24 - inicio.hour - inicio.minute/60) * tarifa.cualTarifa(inicio)
                    d = inicio.day
                    if d != maxDay(inicio.month, inicio.year) :
                        d +=1
                    m = inicio.month
                    while dias != 1 and d != fin.day :
                        aux = datetime(inicio.year,m,d)
                        monto += 24 * tarifa.cualTarifa(aux)
                        if d == maxDay(inicio.month, inicio.year) :
                            m = fin.month
                            d = 0
                        d += 1
                    monto += math.ceil(fin.hour + fin.minute/60) * tarifa.cualTarifa(fin)
                    return monto
    #Si no trabaja lo suficiente o trabaja de mas
    return 0