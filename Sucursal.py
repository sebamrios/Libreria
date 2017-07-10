class Sucursales:
#------------------------------------------------------------------------------
#atributos
#    nroSucursal
#    nombreSucursal
#    domicilioSucursal
# S=[]    vector que almacena los datos de la sucursal
#------------------------------------------------------------------------------
#metodos
    def __init__(self):
        self.S=[]
        self.ListaS=[]

    def ingresarSucursal(self):
        print
        print
        self.nroSucursal=raw_input("Ingrese el nro de la Sucursal\n")
        self.nombreSucursal=raw_input("Ingrese el nombre de fantasia de la sucursal\n")
        self.domicilioSucursal=raw_input("Ingrese el domicilio\n")

    def cargarSucursal(self):
        self.S.append(self.nroSucursal)
        self.S.append(self.nombreSucursal)
        self.S.append(self.domicilioSucursal)

    def guardarSucursal(self):
        archivo=open("/sucursales.txt","a")
        archivo.write(self.S[0])
        archivo.write(",")
        archivo.write(self.S[1])
        archivo.write(",")
        archivo.write(self.S[2])
        archivo.write("\n")

    def mostrarSucursal(self):
        print('\t'*2+"Nro de Sucursal      :"+ str(self.S[0]))
        print('\t'*2+"Nombre de Fantasia   :"+ str(self.S[1]))
        print('\t'*2+"Domicilio de Sucursal:"+ str(self.S[2]))
        print
        print

    def listarSucursales(self):
        archivo=open("/sucursales.txt","r")
        for linea in archivo.readlines():
            print linea
            self.ListaS.append(linea)
        archivo.close()

    def devolverListaSucursales(self):
        return (self.ListaS)

    def limpiarSucursal(self):
        del self.S
        self.S=[]
