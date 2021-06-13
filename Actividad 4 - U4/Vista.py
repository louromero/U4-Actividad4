from tkinter import *
from tkinter import ttk
from functools import partial
from Fraccion import Fraccion
class Calculadora:
    __ventana= None
    __operador= None
    __panel= None
    __operadorAux= None
    __primerOperando= None
    __segundoOperando= None
    __bandera= False
    def __init__(self):
        self.__ventana= Tk()
        self.__ventana.title('Tk-Calculadora')
        mainframe= ttk.Frame(self.__ventana, padding="3 10 3 10")
        mainframe.grid(column=0,row=0,sticky=(N,W,E,S))
        mainframe.columnconfigure(0,weight=1)
        mainframe['borderwidth']= 2
        mainframe['relief']= 'sunken'
        self.__panel= StringVar()
        self.__operador= StringVar()
        self.__operadorAux= None
        operatorEntry= ttk.Entry(mainframe,width= 10,textvariable= self.__operador,justify='center',state='disabled')
        operatorEntry.grid(column=1,row=1,columnspan=1,sticky=(W,E))
        panelEntry= ttk.Entry(mainframe,width=20,textvariable=self.__panel,justify='right',state='disabled')
        panelEntry.grid(column=2,row=1,columnspan=2,sticky=(W,E))
        ttk.Button(mainframe, text='1', command=partial(self.ponerNUMERO, '1')).grid(column=1, row=3, sticky=W)
        ttk.Button(mainframe, text='2', command=partial(self.ponerNUMERO,'2')).grid(column=2, row=3, sticky=W)
        ttk.Button(mainframe, text='3', command=partial(self.ponerNUMERO,'3')).grid(column=3, row=3, sticky=W)
        ttk.Button(mainframe, text='4', command=partial(self.ponerNUMERO,'4')).grid(column=1, row=4, sticky=W)
        ttk.Button(mainframe, text='5', command=partial(self.ponerNUMERO,'5')).grid(column=2, row=4, sticky=W)
        ttk.Button(mainframe, text='6', command=partial(self.ponerNUMERO,'6')).grid(column=3, row=4, sticky=W)
        ttk.Button(mainframe, text='7', command=partial(self.ponerNUMERO,'7')).grid(column=1, row=5, sticky=W)
        ttk.Button(mainframe, text='8', command=partial(self.ponerNUMERO,'8')).grid(column=2, row=5, sticky=W)
        ttk.Button(mainframe, text='9', command=partial(self.ponerNUMERO,'9')).grid(column=3, row=5, sticky=W)
        ttk.Button(mainframe, text='0', command=partial(self.ponerNUMERO, '0')).grid(column=1, row=6, sticky=W)
        ttk.Button(mainframe, text='+', command=partial(self.ponerOPERADOR, '+')).grid(column=2, row=6, sticky=W)
        ttk.Button(mainframe, text='-', command=partial(self.ponerOPERADOR, '-')).grid(column=3, row=6, sticky=W)
        ttk.Button(mainframe, text='*', command=partial(self.ponerOPERADOR, '*')).grid(column=1, row=7, sticky=W)
        ttk.Button(mainframe, text='%', command=partial(self.ponerOPERADOR, '%')).grid(column=3,row=7, sticky=W)
        ttk.Button(mainframe, text='/', command=self.crearFraccion).grid(column=2, row=7, sticky=W)
        ttk.Button(mainframe, text='=', command=partial(self.ponerOPERADOR, '=')).grid(column=1,row=8,columnspan=3,sticky=(E,W))
        self.__panel.set(0)
        panelEntry.focus()
        self.__ventana.mainloop()
    def crearFraccion(self):
        cadena= self.__panel.get()
        if cadena.find("/") == -1:
            self.__panel.set(cadena + "/")
    def ponerNUMERO(self,numero):
        if self.__panel.get()== '0':
            self.__panel.set('')
        if self.__bandera == True:
            self.__panel.set('')
            self.__bandera = False
        if self.__operadorAux==None:
            valor= self.__panel.get()
            self.__panel.set(valor+numero)
        else:
            self.__operadorAux= None
            valor= self.__panel.get()
            self.__primerOperando= valor
            self.__panel.set(numero)
    def borrarPanel(self):
        self.__panel.set('0')
    def resolverOperacion(self,operando1,operacion,operando2):
        resultado= 0
        if str(operando1).find('/') != -1:
            numerador= operando1[0:operando1.find("/")]
            denominador= operando1[operando1.find("/") + 1:]
            if int(denominador) == 0:
                raise Exception('ERROR, fraccion con denominador 0, operacion invalida')
            operando1= Fraccion(int(numerador),int(denominador))
        else:
            operando1= int(operando1)
        if str(operando2).find('/') != -1:
            numerador= operando2[0:operando2.find("/")]
            denominador= operando2[operando2.find("/") + 1:]
            if int(denominador) == 0:
                raise Exception('ERROR, fraccion con denominador 0, operacion invalida')
            operando2= Fraccion(int(numerador),int(denominador))
        else:
            operando2= int(operando2)
        if operacion=='+':
            resultado=operando1+operando2
        else:
            if operacion == '-':
                resultado= operando1-operando2
            else:
                if operacion == '*':
                    resultado= operando1*operando2
                else:
                    if operacion=='%':
                        try:
                            resultado=operando1/operando2
                        except ZeroDivisionError:
                            print("ERROR, division por 0, operacion invalida")
        self.__panel.set(str(resultado))
    def ponerOPERADOR(self,op):
        if op == '=':
            operacion= self.__operador.get()
            self.__segundoOperando=self.__panel.get()
            self.resolverOperacion(self.__primerOperando,operacion,self.__segundoOperando)
            self.__operador.set('')
            self.__operadorAux= None
            self.__bandera= True
        else:
            if self.__operador.get()=='':
                self.__operador.set(op)
                self.__operadorAux= op
            else:
                operacion= self.__operador.get()
                self.__segundoOperando=int(self.__panel.get())
                self.resolverOperacion(self.__primerOperando,operacion,self.__segundoOperando)
                self.__operador.set(op)
                self.__operadorAux= op
