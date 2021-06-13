import math
class Fraccion:
    __numerador= 0
    __denominador= 0
    def __init__(self,numerador,denominador):
        self.__numerador= numerador
        self.__denominador= denominador
    def __str__(self):
        return '{}/{}'.format(self.__numerador,self.__denominador)
    def mcd(self,denominador1,denominador2):
        return math.gcd(denominador1,denominador2)
    def simplificar(self,numerador,denominador):
        aux= self.mcd(numerador,denominador)
        if aux != 1:
            numerador /=aux
            denominador /=aux
        return Fraccion(int(numerador),int(denominador))
    def getNumerador(self):
        return self.__numerador
    def getDenominador(self):
        return self.__denominador
    def __add__(self,otro):
        if type(otro) == int:
            otro= Fraccion(otro,1)
        if self.__denominador == otro.getDenominador():
            denominador= self.__denominador
            numerador= self.__numerador + otro.getNumerador()
        else:
            denominador= math.lcm(self.__denominador,otro.getDenominador())
            numerador= int(((denominador / self.__denominador)* self.__numerador)+((denominador / otro.getDenominador())*otro.getNumerador()))
        resultado= self.simplificar(numerador,denominador)
        return resultado
    def __radd__(self,otro):
        if type(otro) == int:
            otro= Fraccion(otro,1)
        if self.__denominador == otro.getDenominador():
            denominador= self.__denominador
            numerador= self.__numerador + otro.getNumerador()
        else:
            denominador= math.lcm(self.__denominador,otro.getDenominador())
            numerador= int(((denominador / self.__denominador)* self.__numerador)+((denominador / otro.getDenominador())*otro.getNumerador()))
        resultado= self.simplificar(numerador,denominador)
        return resultado
    def __sub__(self,otro):
        if type(otro) == int:
            otro= Fraccion(otro,1)
        if self.__denominador == otro.getDenominador():
            denominador= self.__denominador
            numerador= self.__numerador - otro.getNumerador()
        else:
            denominador= math.lcm(self.__denominador,otro.getDenominador())
            numerador= int(((denominador / self.__denominador)* self.__numerador)-((denominador / otro.getDenominador())*otro.getNumerador()))
        resultado= self.simplificar(numerador,denominador)
        return resultado
    def __rsub__(self,otro):
        if type(otro) == int:
            otro= Fraccion(otro,1)
        if self.__denominador == otro.getDenominador():
            denominador= self.__denominador
            numerador= otro.getNumerador() - self.__numerador
        else:
            denominador= math.lcm(self.__denominador,otro.getDenominador())
            numerador= int(((denominador / otro.getDenominador())* otro.getNumerador())-((denominador / self.__denominador)*self.__numerador))
        resultado= self.simplificar(numerador,denominador)
        return resultado
    def __mul__(self,otro):
        if type(otro) == int:
            otro= Fraccion(otro,1)
        numerador= self.__numerador * otro.getNumerador()
        denominador= self.__denominador * otro.getDenominador()
        resultado= self.simplificar(numerador,denominador)
        return resultado
    def __rmul__(self,otro):
        if type(otro) == int:
            otro= Fraccion(otro,1)
        numerador= self.__numerador * otro.getNumerador()
        denominador= self.__denominador * otro.getDenominador()
        resultado= self.simplificar(numerador,denominador)
        return resultado
    def __truediv__(self,otro):
        if type(otro) == int:
            otro= Fraccion(otro,1)
        numerador= self.__numerador * otro.getDenominador()
        denominador= self.__denominador * otro.getNumerador()
        resultado= self.simplificar(numerador,denominador)
        return resultado
    def __rtruediv__(self, otro):
        if type(otro) == int:
            otro= Fraccion(otro,1)
        numerador= otro.getNumerador() * self.__denominador
        denominador= otro.getDenominador() * self.__numerador
        resultado= self.simplificar(numerador,denominador)
        return resultado






