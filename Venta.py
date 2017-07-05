import time
from Libro import Libros
from Sucursal import Sucursales
#------------------------------------------------------------------------------
class Ventas():
#------------------------------------------------------------------------------
#atributos
#    fecha
#    hora
#    totalVentas
#    V=[]   vector que contiene los datos de la venta realizada
#------------------------------------------------------------------------------
#metodos
    def __init__(self):
        self.V=[]
        #self.VecLibros=[]
        #self.VecSucursales=[]

    def ingresarVenta(self, libro,sucursal):
        self.fecha=time.strftime("%d/%m/%y")
        self.hora=time.strftime("%X")
        self.V.append(self.fecha)
        self.V.append(self.hora)
        self.V.append(sucursal)
        self.V.append(libro)

    def mostrarVenta(self):
        print('\t'*2 + "Fecha:       "+ str(self.V[0]))
        print('\t'*2 + "Hora:        "+ str(self.V[1]))
        print('\t'*2 + "Sucursal Nro:"+ str(self.V[2]))

        print('\t'*2 + "Libro:")
        for i in range(len(self.V[3])):
            print('\t'*3 + str(self.V[3][i]))

    def limpiarVenta(self):
        del self.V
        self.V=[]

    #def cargarVenta(venta):
    #    self.VecVentas.append(self.fecha)
    #    self.VecVentas.append(self.hora)
    #    self.VecVentas.append(sucursal)
        #self.V.append(L)

    def mostrarTotal():
        print("El precio total de las ventas es:")
        print("$"+str(totalVentas))
