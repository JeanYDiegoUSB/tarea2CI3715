'''
Created on Apr 22, 2016

@author:
        Jean Paul Alexander Lacour
        Diego Daniel Pedroza Pérez
'''

import math

class Tarifa(object) :
    def __init__(self,semana,fin) :
        self.semana = semana
        self.fin = fin
    
    def getSemana(self) :
        return self.semana

    def getFin(self) :
        return self.fin

def bisiesto(year) :
    if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0) :  
        return True  
    else :  
        return False 
    
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

def calcularPrecio(tarifa, tiempoDeTrabajo) :
    inicio,fin = tiempoDeTrabajo[0],tiempoDeTrabajo[1]
    if inicio.year == fin.year and inicio.month == fin.month and inicio.day == fin.day :
        dif = fin.hour - inicio.hour
        if dif >= 0.25 :
            return tarifa.getSemana() * math.ceil(dif)
    elif inicio.year == fin.year and inicio.month == fin.month :
        dif = math.ceil(24 * (fin.day - inicio.day) - inicio.hour + fin.hour)
        if dif <= 168 :
            return tarifa.getSemana() * dif
    elif inicio.year == fin.year :
        if fin.month - inicio.month == 1 :
            dias = maxDay(inicio.month,inicio.year) + fin.day - inicio.day 
            if dias <= 7 :
                dif = math.ceil(24 * dias - inicio.hour + fin.hour)
                if dif <= 168 :
                    return tarifa.getSemana() * dif
    elif inicio.year != fin.year :
        if inicio.month == 12 and fin.month == 1 :
            dias = 31 + fin.day - inicio.day
            if dias <= 7 :
                dif = math.ceil(24 * dias - inicio.hour + fin.hour)
                if dif <= 168 :
                    return tarifa.getSemana() * dif
    return 0
