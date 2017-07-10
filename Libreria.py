#-------------------------------clases importadas------------------------------
from Libro import Libros
from Sucursal import Sucursales
from Venta import Ventas
from interface import Menues
#----------------Instancias de Clases y declaraciones de variables--------------
m=Menues()
v=Ventas()
s=Sucursales()
e=Libros()
respuesta=['s','S','si','SI','Si','n','N','no','No','NO']
respuestaSi=['s','S','si','SI','Si']
opciones=["1","2","3","4"]
bucle="s"
i="1"
ConjLibros=[] #conjunto de libros que hay en totalVentas
ConjSucursales=[]
ConjLibrosVendidos=[]


#------------------------------------INICIO-------------------------------------
while bucle in respuestaSi:
    m.menuGral()
    respMenuGral=respuestaSi[0]
    respMenuLibro=respuestaSi[0]
    respMenuSucursal=respuestaSi[0]
    respMenuVentas=respuestaSi[0]
    respCargaLibros=respuestaSi[0]
    o=""
    o=raw_input("Ingrese una de las opciones:\n")# opcion ingresada

    #while o in opciones:
    while not o in opciones:
        o=raw_input("Ingrese un valor valido,por favor\n")
    while o in opciones:
        if o=="1"  :#---------------------LIBROS------------------------------------
            m.menuLibro()
            while respMenuLibro in respuestaSi:
                e.ingresarLibro()
                e.cargarLibro()
                e.guardarLibro()
                e.mostrarLibro()
                ConjLibros.append(e.L)
                e.limpiarLibro()
                respMenuLibro=raw_input("\nDesea seguir cargando libros? s/n\n")
                while not respMenuLibro in respuesta:
                    respMenuLibro=raw_input("Ingrese un valor valido,por favor\n")
            break
        elif o=="2":#-------------------SUCURSALES----------------------------------
            m.menuSucursal()
            while respMenuSucursal in respuestaSi:
                s.ingresarSucursal()
                s.cargarSucursal()
                s.mostrarSucursal()
                s.guardarSucursal()
                ConjSucursales.append(s.S)
                s.limpiarSucursal()
                respMenuSucursal=raw_input("\nDesea seguir cargando sucursales? s/n\n")
                while not respMenuSucursal in respuesta:
                    respMenuSucursal=raw_input("Ingrese un valor valido,por favor\n")
            break
        elif o=="3":#--------------------VENTAS-------------------------------------
            m.menuVentas()
            while respMenuVentas in respuestaSi:
                k=""
                j=""
                respCargaLibros="s"
                del ConjLibrosVendidos
                ConjLibrosVendidos=[]
                m.msjVentasListaSucursales()
                s.listarSucursales()
                ConjSucursales=s.devolverListaSucursales()
                j=int(raw_input("\nIngrese la sucursal a eleccion,por favor\n"))
                j=ConjSucursales[j-1]

                while respCargaLibros in respuestaSi:
                    m.msjVentasListaLibros()
                    e.listarLibros()
                    ConjLibros=e.devolverListaLibros()
                    k=int(raw_input("\nIngrese un libro a comprar,por favor?\n"))
                    k=ConjLibros[k-1]
                    ConjLibrosVendidos.append(k)
                    respCargaLibros=raw_input("Desea seguir cargando mas libros en la compra? s/n\n")

                v.ingresarVenta(ConjLibrosVendidos,j)
                v.mostrarVenta()
                v.limpiarVenta()
                k=""
                respMenuVentas=raw_input("Desea seguir cargando Ventas? s/n\n")
                while not respMenuVentas in respuesta:
                    respMenuVentas=raw_input("Ingrese un valor valido,por favor\n")

            break
        elif o=="4":#--------------TOTAL DE VENTAS----------------------------------
            m.msjTotalVentas()
            break
    bucle=raw_input("Desea realizar una operacion mas? s/n\n")
    while not bucle in respuesta:
        bucle=raw_input("Ingrese un valor valido,por favor\n")
m.menuFin()
print("---------------------------------------------------------------")
