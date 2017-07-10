class Libros:
#------------------------------------------------------------------------------
#atributos
#    titulo
#    autor
#    color
#    anio
#    precio
#    L=[]  vector que almacena los datos del libro ingresado
#------------------------------------------------------------------------------
#metodos
    def __init__(self):
        self.L=[]
        self.ListaL=[]

    def ingresarLibro(self):
        print
        print
        self.titulo=raw_input("Ingrese el nombre del libro:\n")
        self.autor=raw_input("Ingrese el autor del libro:\n")
        self.precio=raw_input("Ingrese el precio:\n")
        self.color=raw_input("Ingrese el color:\n")
        self.anio=raw_input("Ingrese el anio:\n")

    def cargarLibro(self):
        self.L.append(self.titulo)
        self.L.append(self.autor)
        self.L.append(self.color)
        self.L.append(self.precio)
        self.L.append(self.anio)

    def guardarLibro(self):
        archivo=open("/libros.txt","a")
        archivo.write(self.L[0])
        archivo.write(",")
        archivo.write(self.L[1])
        archivo.write(",")
        archivo.write(self.L[2])
        archivo.write(",")
        archivo.write(self.L[3])
        archivo.write("\n")

    def listarLibros(self):
        archivo=open("/Libros.txt","r")
        for linea in archivo.readlines():
            print linea
            self.ListaL.append(linea)
        archivo.close()

    def devolverListaLibros(self):
        return (self.ListaL)

    def mostrarLibro(self):
        print('\t'*2 + "Titulo: " + str(self.L[0]))
        print('\t'*2 + "Autor:  " + str(self.L[1]))
        print('\t'*2 + "color:  " + str(self.L[2]))
        print('\t'*2 + "precio: " + str(self.L[3]))
        print('\t'*2 + "precio: " + str(self.L[4]))
        print
        print

    def limpiarLibro(self):
        del self.L
        self.L=[]
