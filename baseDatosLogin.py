import pyodbc

class BaseDatosLogin:
    #Conexion con la base de datos SQL server "baseDatosProyecto" 
    def __init__(self, server="LAPTOP-USF80KCK",database="baseDatosProyecto",username="sa",password="1234"):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+self.server+';DATABASE='+self.database+';UID='+self.username+';PWD='+ self.password)

    #Aplicamos los cambios y cerramos la conexion del SQL server
    def cerrar_conexion(self):
        cursor = self.cnxn.cursor()
        cursor.close() 
        self.cnxn.commit() #Aplicamos los cambios
        self.cnxn.close() #Cerramos conexion con la base de datos

    #Obtiene la lista de todos los correos de SQL server y lo almacena en una lista
    def lista_correos(self):
        cursor = self.cnxn.cursor()
        cursor.execute("SELECT * FROM registroLogin")
        listaCorreos = [row[0] for row in cursor.fetchall()]
        listaStr = list(map(str, listaCorreos))#Convierte todos los datos de la lista en cadena de texto
        return listaStr

    #Obtiene las contraseña del usuario ingresado segun SQL server
    def obtener_contrasena(self,correo):
        cursor = self.cnxn.cursor()
        cursor.execute('SELECT contraseña FROM registroLogin WHERE correo =\''+correo+"\'")
        ct = cursor.fetchone()[0]
        contraConvertida =str(ct)
        return contraConvertida

    #Obtiene el permiso del usuario ingresado segun SQL server 
    def obtener_permiso(self,correo):
        cursor = self.cnxn.cursor()
        cursor.execute('SELECT permisos FROM registroLogin WHERE correo =\''+correo+"\'")
        ct = cursor.fetchone()[0]
        permiStr =str(ct)
        return permiStr

    #Creamos nuevo usuarios , y lo integramos a la base de datos SQL server
    def crear_usuario(self, cor, nom, ape, con):
        cursor = self.cnxn.cursor()
        cursor.execute("INSERT INTO registroLogin (correo, nombre, apellido, contraseña) VALUES (?, ?, ?, ?)", cor,nom, ape, con)
        return "Usuario Registrado"

    #Añadimos mas datos del usuario recien creado, a la base de datos SQL server  
    def crear_perfil(self, cel, nac, per, gen, correo ):
        cursor = self.cnxn.cursor()
        cursor.execute("UPDATE registroLogin SET celular = ?, nacimiento = ?, permisos = ?, genero = ? WHERE correo = ?", cel, nac, per, gen, correo)
        #AND nombre = ? AND apellido = ? AND contraseña = ?
        return "registrado"

    def obtener_ulti_user(self):
        cursor = self.cnxn.cursor()
        cursor.execute("SELECT * FROM registroLogin WHERE correo = (SELECT MAX(correo) FROM registroLogin)")
        lista_ultimo = cursor.fetchone()
        return lista_ultimo 
    
    def eliminar_usuario(self, nombre):
        cursor = self.cnxn.cursor()
        cursor.execute("DELETE FROM login WHERE nombres = ?", nombre)
        
    def ver_permisos(self, nombre):
        cursor = self.cnxn.cursor()
        cursor.execute("SELECT permisos FROM LoginPersonal WHERE nombre = ?", nombre)
        for row in cursor:
            print(row)
        





