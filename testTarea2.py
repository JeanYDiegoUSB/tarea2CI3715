'''
Created on Apr 22, 2016
@author:
        Jean Paul Alexander Lacour
        Diego Daniel Pedroza Perez
'''
import tarea2
from datetime import datetime
import unittest

class Tarea2Tester(unittest.TestCase):
    def testSieteDiasExactos(self):
        tarifa = tarea2.Tarifa(20,40)
        i,f=datetime(2016,4,28,0,0),datetime(2016,5,5,0,0)
        monto=tarea2.calcularPrecio(tarifa,[i,f])
        self.assertEqual(4320,monto)
    def testSieteDiasYUnaHora(self):
        tarifa = tarea2.Tarifa(20,40)
        i,f=datetime(2016,4,28,0,0),datetime(2016,5,5,1,0)
        monto=tarea2.calcularPrecio(tarifa,[i,f])
        self.assertEqual(0,monto)
    def testMesesDistintos(self):
        tarifa = tarea2.Tarifa(20,40)
        i,f=datetime(2007,8,28,4,0),datetime(2007,9,2,21,0)
        monto=tarea2.calcularPrecio(tarifa,[i,f])
        self.assertEqual(3640,monto)
    def testAniosDistintos(self):
        tarifa = tarea2.Tarifa(20,40)
        i,f=datetime(2007,12,28,3,0),datetime(2008,1,2,21,0)
        monto=tarea2.calcularPrecio(tarifa,[i,f])
        self.assertEqual(3720,monto)
    def testMenosDeQuinceMinutos(self):
        tarifa = tarea2.Tarifa(20,40)
        i,f=datetime(2016,5,5,0,0),datetime(2016,5,5,0,10)
        monto=tarea2.calcularPrecio(tarifa,[i,f])
        self.assertEqual(0,monto)
    def testSieteDiasYUnMinuto(self):
        tarifa = tarea2.Tarifa(20,40)
        i,f=datetime(2016,4,28,0,0),datetime(2016,5,5,0,1)
        monto=tarea2.calcularPrecio(tarifa,[i,f])
        self.assertEqual(0,monto)
    def testSeisDiasYUnMinuto(self):
        tarifa = tarea2.Tarifa(1,2)
        i,f=datetime(2016,4,28,0,0),datetime(2016,5,4,0,1)
        monto=tarea2.calcularPrecio(tarifa,[i,f])
        self.assertEqual(193,monto)
    def test24HorasBordesFinDe(self):
        tarifa = tarea2.Tarifa(1,2)
        i,f=datetime(2016,5,1,0,1),datetime(2016,5,1,23,59)
        monto=tarea2.calcularPrecio(tarifa,[i,f])
        self.assertEqual(48,monto)
    def test24HorasBordesSemana(self):
        tarifa = tarea2.Tarifa(1,2)
        i,f=datetime(2016,5,2,0,1),datetime(2016,5,2,23,59)
        monto=tarea2.calcularPrecio(tarifa,[i,f])
        self.assertEqual(24,monto)
    def testFaltan20ParaLasDoce(self):
        tarifa = tarea2.Tarifa(1,2)
        i,f=datetime(2015,12,31,23,40),datetime(2016,1,1,0,0)
        monto=tarea2.calcularPrecio(tarifa,[i,f])
        self.assertEqual(1,monto)





if __name__ == '__main__':
    unittest.main()