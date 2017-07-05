class Sucursales:
#------------------------------------------------------------------------------
#atributos
#    nroSucursal
#    nombreSucursal
#    domicilioSucursal
#   S=[]    vector que almacena los datos de la sucursal
#------------------------------------------------------------------------------
#metodos
    def __init__(self):
        self.S=[]
        return

    def ingresarSucursal(self):
        print
        print
        self.nroSucursal=raw_input("Ingrese el nro de la Sucursal\n")
        self.nombreSucursal=raw_input("Ingrese el nombre de fantasia de la sucursal\n")
        self.domicilioSucursal=raw_input("Ingrese el domicilio\n")
        return

    def cargarSucursal(self):
        self.S.append(self.nroSucursal)
        self.S.append(self.nombreSucursal)
        self.S.append(self.domicilioSucursal)
        return

    def mostrarSucursal(self):
        print('\t'*2+"Nro de Sucursal      :"+ str(self.S[0]))
        print('\t'*2+"Nombre de Fantasia   :"+ str(self.S[1]))
        print('\t'*2+"Domicilio de Sucursal:"+ str(self.S[2]))
        print
        print
        return

    def limpiarSucursal(self):
        del self.S
        self.S=[]
        return
