#---------------IMPORTACIONES--------------- 
import sys
from PyQt5.uic import loadUi #PyQt5.uic --> Carga archivos .iu
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from baseDatosLogin import *  #Base de datos de login usuario
from baseDatosAlmacen import *
from PyQt5.QtGui import QPixmap




#-------------BIENVENIDA------------
class BienvenidaPantalla(QDialog): #Ventana BienvenidaLogin
    def __init__(self):
        super(BienvenidaPantalla, self).__init__()
        loadUi("bienvenida.ui", self) #Carga interfaz
        self.inicioBoton.clicked.connect(self.irInicioSesion) #Este codigo se refiere al hacer click en el boton, vamos a la funcion irInicioSesion 
        self.salirBoton.clicked.connect(self.funsalir)
        
     #Funciones para cambiar pantalla a inicio de sesion 
    def irInicioSesion(self):
        iniciaSesion = IniSesionPantalla()
        menuBien = BienvenidaPantalla()
        widget.addWidget(iniciaSesion) #Añadir Ventana
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.removeWidget(menuBien) #Remover Ventana
   
    #Cierra Ventana
    def funsalir(self):
        app.quit()


#---------INICIO SESION-------------  
class IniSesionPantalla(QDialog): 
    permisoUser = ""
    correoUser = ""
    def __init__(self):
        super(IniSesionPantalla, self).__init__()
        loadUi("login.ui", self, )  #Carga Interfaz 
        self.contra.setEchoMode(QtWidgets.QLineEdit.Password) #Forma para que la contraseña aparezca oculta al usuario
        self.loginBoton.clicked.connect(self.funcIniciaSesion) #Cuando hacemos click en el boton, vamos a la funcion iniciarSesion
        self.loginBD =  BaseDatosLogin() #Base de datos de login de usuario
        

    def funcIniciaSesion(self):
        #Extraemos la contraseña y el usuario y lo asignamos a variables
        correo = (self.correo.text())
        contra = (self.contra.text())
        
        #Realizamos una validación de ingreso
        if len(correo) == 0 or len(contra) == 0:
            self.error.setText("Todos los campos son obligatorios")

        #Verificamos la existencia del usuario en la base de datos
        elif correo not in self.loginBD.lista_correos():
            self.error.setText("Correo no encontrado. Vuelve a intentarlo.")

        #Cumpliendo todas las condiciones anteriores
        #Validamos la contraseña,segun los datos registrados en nuestra base de datos
        else:
            contraBD = self.loginBD.obtener_contrasena(correo)
            if contraBD == contra:
                print("Inicia sesion correcto.")
                self.error.setText("")

                #Se guarda en una variable global para poder utilizarlos en todas las clases
                global permisoUser 
                global correoUser

                permisoUser = self.loginBD.obtener_permiso(correo)
                correoUser = correo
                
                
                print(permisoUser) #-----------
                print(correoUser) #-------------
                self.loginBD.cerrar_conexion()
    
                menuPant = MenuPantalla()
                menuInic = IniSesionPantalla()
                
                widget.addWidget(menuPant)
                widget.setCurrentIndex(widget.currentIndex()+1)
                widget.removeWidget(menuInic)
              
            else:
                self.error.setText("Contraseña Invalida")


#---------------MENU----------------
class MenuPantalla(QDialog):
    def __init__(self):
        super(MenuPantalla, self).__init__()
        loadUi("menu.ui", self)
        self.almacenBoton.clicked.connect(self.funAlmacen)
        self.nuevaCntaBt.clicked.connect(self.irCrearCuenta)
        self.cerrarSesionBt.clicked.connect(self.irBienvenida)
        self.loginBD = BaseDatosLogin() #Base de datos de usuarios login
        
    def irCrearCuenta(self):
        global permisoUser
        global correoUser
        if permisoUser == "Administrador":
            crear = CrearCuentaPantalla()
            menu =MenuPantalla()
            widget.addWidget(crear)
            widget.setCurrentIndex(widget.currentIndex()+1)
            widget.removeWidget(menu)
        else:
            print(permisoUser)#-------------
            print("No tiene permisos para obtener el acceso")
            self.error.setText("No tiene permisos para obtener el acceso")

    def funAlmacen(self):
        global permisoUser
        global correoUser
        
        if permisoUser == "Administrador" or permisoUser == "Cajero":
            almacen = AlmacenMenuPant()
            widget.addWidget(almacen)
            widget.setCurrentIndex(widget.currentIndex()+1)
        else:
            print("No tiene permisos para obtener el acceso")
            self.error.setText("No tiene permisos para obtener el acceso")

    def irBienvenida(self):
        bienvenida = BienvenidaPantalla()
        widget.addWidget(bienvenida)
        widget.setCurrentIndex(widget.currentIndex()+1)

# -----------ALMACEN----------------
class AlmacenMenuPant(QDialog):   
    def __init__(self):
        super(AlmacenMenuPant, self).__init__()
        loadUi("prodMenu.ui", self) 
        self.inventarioBtn.clicked.connect(self.irInventario) 
        self.buscarBoton.clicked.connect(self.irBusquedad)
        self.agregarBoton.clicked.connect(self.irAgregar)
        self.borrarBoton.clicked.connect(self.irBorrar)
        self.atrasBoton.clicked.connect(self.irAtras)
        self.almacenBD = BaseDatosAlmacen()

    def irInventario(self):
        inv = InventarioProductoPant()
        menuAlmacen = AlmacenMenuPant()
        widget.addWidget(inv) 
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.removeWidget(menuAlmacen) 

    def irBusquedad(self):
        bus = BusquedadProductoPant()
        menuAlmacen = AlmacenMenuPant()
        widget.addWidget(bus) 
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.removeWidget(menuAlmacen) 

    def irAgregar(self):
        agr = AgregarProductoPant()
        menuAlmacen = AlmacenMenuPant()
        widget.addWidget(agr) 
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.removeWidget(menuAlmacen) 

    def irBorrar(self):
        bor = BorrarProductoPant()
        menuAlmacen = AlmacenMenuPant()
        widget.addWidget(bor) 
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.removeWidget(menuAlmacen)

    def irAtras(self):
        ventas = AlmacenMenuPant()
        menu = MenuPantalla()
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.removeWidget(ventas)


class InventarioProductoPant(QDialog): 
    def __init__(self):
        super(InventarioProductoPant, self).__init__()
        loadUi("prodInventario.ui", self)
        self.atrasBoton.clicked.connect(self.atras)
        self.reflescarBoton.clicked.connect(self.reflescar)
        self.tablaInventario.setColumnWidth(0, 180)
        self.tablaInventario.setColumnWidth(1, 180)
        self.tablaInventario.setColumnWidth(2, 180)
        self.tablaInventario.setColumnWidth(3, 380)
        self.tablaInventario.setColumnWidth(4, 130)
        self.tablaInventario.setColumnWidth(5, 130)
        self.tablaInventario.setColumnWidth(6, 130)
        self.tablaInventario.setColumnWidth(7, 130)
        self.almacenBD = BaseDatosAlmacen()

    def atras(self):
        menu = AlmacenMenuPant()
        pant = InventarioProductoPant()
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.removeWidget(pant)

    def reflescar(self):
        datos = self.almacenBD.lista_datos()
        i = len(datos)
        
        self.tablaInventario.setRowCount(i)
        tablerow = 0
        for row in datos: #row recorre la lista 
            self.tablaInventario.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[0]))
            self.tablaInventario.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[1]))
            self.tablaInventario.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[2]))
            self.tablaInventario.setItem(tablerow,3,QtWidgets.QTableWidgetItem(row[3]))
            self.tablaInventario.setItem(tablerow,4,QtWidgets.QTableWidgetItem(row[4]))
            self.tablaInventario.setItem(tablerow,5,QtWidgets.QTableWidgetItem(row[5]))
            self.tablaInventario.setItem(tablerow,6,QtWidgets.QTableWidgetItem(row[6]))
            self.tablaInventario.setItem(tablerow,7,QtWidgets.QTableWidgetItem(row[7]))
            tablerow +=1


class BusquedadProductoPant(QDialog): 
    def __init__(self):
        super(BusquedadProductoPant, self).__init__()
        loadUi("prodBuscar.ui", self)
        self.atrasBoton.clicked.connect(self.volver)
        self.buscarBtn.clicked.connect(self.buscarProducto)
        self.tablaBuscar.setColumnWidth(0, 180)
        self.tablaBuscar.setColumnWidth(1, 180)
        self.tablaBuscar.setColumnWidth(2, 180)
        self.tablaBuscar.setColumnWidth(3, 380)
        self.tablaBuscar.setColumnWidth(4, 90)
        self.tablaBuscar.setColumnWidth(5, 130)
        self.tablaBuscar.setColumnWidth(6, 130)
        self.almacenBD = BaseDatosAlmacen()

    def volver(self):
        menu = AlmacenMenuPant()
        pant = BusquedadProductoPant()
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.removeWidget(pant)

    def buscarProducto(self):
        codigo = self.codigo.text()

        if len(codigo)==0 :
            self.error.setText("Ingresa el codigo del producto")  
        else:
            
            resp = self.almacenBD.busca_producto(codigo)
            
            i = len(resp)
            
            self.tablaBuscar.setRowCount(i)
            tablerow = 0
            self.error.clear()
            for row in resp: #row recorre la lista 
                self.tablaBuscar.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[0]))
                self.tablaBuscar.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[1]))
                self.tablaBuscar.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[2]))
                self.tablaBuscar.setItem(tablerow,3,QtWidgets.QTableWidgetItem(row[3]))
                self.tablaBuscar.setItem(tablerow,4,QtWidgets.QTableWidgetItem(row[4]))
                self.tablaBuscar.setItem(tablerow,5,QtWidgets.QTableWidgetItem(row[5]))
                self.tablaBuscar.setItem(tablerow,6,QtWidgets.QTableWidgetItem(row[6]))
                self.tablaBuscar.setItem(tablerow,7,QtWidgets.QTableWidgetItem(row[7]))
                
                tablerow +=1

            if resp == None:
                self.error.setText("Producto no encontrado")
            elif resp == 0:
                self.error.setText("Producto no encontrado")


class AgregarProductoPant(QDialog):  
    def __init__(self):
        super(AgregarProductoPant, self).__init__()
        loadUi("prodAgregar.ui", self)
        self.atrasBoton.clicked.connect(self.atras)
        self.agregarBoton.clicked.connect(self.agregarProducto)
        self.limpiarBoton.clicked.connect(self.limpiar)
        self.check.clicked.connect(self.limpiarFechas)
        self.almacenBD = BaseDatosAlmacen()

    def atras(self):
        menu = AlmacenMenuPant()
        pant = AgregarProductoPant()
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.removeWidget(pant)

    def agregarProducto(self):
        codigo = self.codigo.text()
        producto = self.producto.text()
        descrip = self.descrip.text()
        stock = self.stock.text()
        proveedor = self.comboProv.currentText()
        precio = self.precio.text()
        fechaProduc = self.dateProduc.date()
        fechaVenci = self.dateVenci.date()     

        fecProdStr = fechaProduc.toString('dd-MM-yyyy')
        fecVencStr = fechaVenci.toString('dd-MM-yyyy')

        if len(codigo)==0 or len(producto)==0 or len(descrip)==0 or len(stock)==0 or len(precio)==0:
            self.error.setText("Todos los campos son obligatorios.")  

        elif codigo in self.almacenBD.lista_codigos():
            self.error.setText("Ha ingresado un producto con codigos duplicados, vuelva a intentarlo")

        else:
            if self.check.isChecked():
                fecProdStr = ""
                fecVencStr = ""
                self.almacenBD.inserta_producto(codigo, producto, proveedor, descrip, stock,precio, fecProdStr, fecVencStr)
                self.mensaje.setText("¡¡Producto registrado!!")
                self.error.clear()
                print("hola")
            else:
                self.almacenBD.inserta_producto(codigo, producto, proveedor, descrip, stock,precio, fecProdStr, fecVencStr)
                self.mensaje.setText("¡¡Producto registrado!!")
                self.error.clear()

    def limpiar(self):
        self.codigo.clear()
        self.producto.clear()
        self.descrip.clear()
        self.stock.clear()
        self.dateProduc.clear()
        self.dateVenci.clear()
        self.error.clear()
        self.mensaje.clear()
        self.precio.clear()

    def limpiarFechas(self):
        self.dateProduc.clear()
        self.dateVenci.clear()


class BorrarProductoPant(QDialog):  
    def __init__(self):
        super(BorrarProductoPant, self).__init__()
        loadUi("prodBorrar.ui", self)
        self.atrasBoton.clicked.connect(self.atras)
        self.borrarBtn.clicked.connect(self.eliminarProducto)
        self.tablaBorrar.setColumnWidth(0, 180)
        self.tablaBorrar.setColumnWidth(1, 180)
        self.tablaBorrar.setColumnWidth(2, 180)
        self.tablaBorrar.setColumnWidth(3, 380)
        self.tablaBorrar.setColumnWidth(4, 90)
        self.tablaBorrar.setColumnWidth(5, 130)
        self.tablaBorrar.setColumnWidth(6, 130)
        self.almacenBD = BaseDatosAlmacen() 

    def atras(self):
        menu = AlmacenMenuPant()
        pant = BorrarProductoPant()
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.removeWidget(pant)
		
    def eliminarProducto(self):
        codigo = self.codigo.text()
    
        if len(codigo)==0 :
            self.error.setText("Ingresa el codigo del producto")  

        else:
            resp = self.almacenBD.eliminar_productos(codigo)

            datos = self.almacenBD.lista_datos()
            i = len(datos)
            
            self.tablaBorrar.setRowCount(i)
            tablerow = 0
            for row in datos: #row recorre la lista 
                self.tablaBorrar.setItem(tablerow,0,QtWidgets.QTableWidgetItem(row[0]))
                self.tablaBorrar.setItem(tablerow,1,QtWidgets.QTableWidgetItem(row[1]))
                self.tablaBorrar.setItem(tablerow,2,QtWidgets.QTableWidgetItem(row[2]))
                self.tablaBorrar.setItem(tablerow,3,QtWidgets.QTableWidgetItem(row[3]))
                self.tablaBorrar.setItem(tablerow,4,QtWidgets.QTableWidgetItem(row[4]))
                self.tablaBorrar.setItem(tablerow,5,QtWidgets.QTableWidgetItem(row[5]))
                self.tablaBorrar.setItem(tablerow,6,QtWidgets.QTableWidgetItem(row[6]))
                self.tablaBorrar.setItem(tablerow,7,QtWidgets.QTableWidgetItem(row[7]))
                tablerow +=1
                
            if resp == None:
                self.error.setText("Producto no encontrado")
            elif resp == 0:
                self.error.setText("Producto no encontrado")
            else:
                self.error.setText("Producto eliminado")


#-----------CREAR CUENTA-----------

class CrearCuentaPantalla(QDialog):
    def __init__(self):
        super(CrearCuentaPantalla, self).__init__()
        loadUi("crearcuenta.ui",self)
        self.contra.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmarcontra.setEchoMode(QtWidgets.QLineEdit.Password)
        self.siguienteBoton.clicked.connect(self.funCrearCuenta)
        self.regresarBoton.clicked.connect(self.regresar)
        self.loginBD = BaseDatosLogin() # Base de datos de login usuarios
    
    def regresar(self):
        menu = MenuPantalla()
        crearCnta = CrearCuentaPantalla()
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.removeWidget(crearCnta)

    def funCrearCuenta(self):
        correo = self.correo.text()
        nombre = self.nombre.text()
        apellido = self.apellido.text()
        contrasena = self.contra.text()
        confirmaContra = self.confirmarcontra.text()

        if len(nombre)==0 or len(apellido)==0 or len(correo)==0 or len(contrasena)==0 or len(confirmaContra)==0:
            self.error.setText("Todos los campos son obligatorios.")  

        elif contrasena!=confirmaContra:
            self.error.setText("Las contraseñas no coinciden. Vuelve a intentarlo.")

        else:
            self.loginBD.crear_usuario(correo, nombre, apellido, contrasena)
            self.loginBD.cerrar_conexion()
            
            global correoUser
            correoUser = correo  # actualizando correo nuevo usuario
            print(correoUser)
            perfil = PerfilPantalla()
            crearCnta = CrearCuentaPantalla()

            widget.addWidget(perfil)
            widget.setCurrentIndex(widget.currentIndex()+1)
            widget.removeWidget(crearCnta)


class PerfilPantalla(QDialog):
    def __init__(self):
        super(PerfilPantalla, self).__init__()
        loadUi("perfil.ui",self)
        self.BasedeDatos = MenuPantalla()
        self.registroBoton.clicked.connect(self.funRegistrarPerfil)
        self.loginBD = BaseDatosLogin() #Base de datos de usuarios login
        

    def funRegistrarPerfil(self):
        celular = self.celular.text()
        fecha = self.dateEdit.date()
        permisos = self.comboPermisos.currentText()
        genero = self.comboGenero.currentText()

        fechaStr = fecha.toString('dd-MM-yyyy')

        if len(celular)==0 or len(fechaStr)==0:
            self.error.setText("Todos los campos son obligatorios.")  
        
        else:
            
            global correoUser
            self.loginBD.crear_perfil(celular, fechaStr, permisos, genero, correoUser)
            self.loginBD.cerrar_conexion()
            print("Usuario Creado")

            bienvenida = BienvenidaPantalla()
            perfil = PerfilPantalla()
            widget.addWidget(bienvenida)
            widget.setCurrentIndex(widget.currentIndex()+1)
            widget.removeWidget(perfil)   



#-------------MAIN-----------------
app = QApplication(sys.argv)
bienvenida = BienvenidaPantalla()

widget = QtWidgets.QStackedWidget()
#Widget apilado --> apilar tantas pantallas unas encimas de otras
#ejemplo: Para q al hacer clic en el boton iniciar , nos lleve a otra pantalla

widget.addWidget(bienvenida) #Agregamos bienvenido a la pila

#Establecemos la altura y ancho del widget
widget.setFixedHeight(800)
widget.setFixedWidth(1200)

widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Saliendo")


