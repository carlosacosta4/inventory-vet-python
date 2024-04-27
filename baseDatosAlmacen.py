import pyodbc

class BaseDatosAlmacen:
   
    def __init__(self, server="LAPTOP-USF80KCK",database="baseDatosProyecto",username="sa",password="1234"):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+self.server+';DATABASE='+self.database+';UID='+self.username+';PWD='+ self.password)

    def inserta_producto(self,cod, prod, prov, descrip, stock, preUni, fecProd, fecVenc):
        cursor = self.cnxn.cursor()
        cursor.execute("INSERT INTO registroAlmacen (Codigo, Producto, Proveedor, Descripcion, Stock,PrecioUnitario, FechaProduccion, Fechavencimiento) VALUES (?, ?, ?, ?,?, ?, ?, ?)",cod, prod, prov, descrip, stock,preUni, fecProd, fecVenc)
        self.cnxn.commit() 
        cursor.close() 

    def lista_codigos(self):
        cursor = self.cnxn.cursor()
        cursor.execute("SELECT * FROM registroAlmacen")
        listaCodigos = [row[0] for row in cursor.fetchall()]
        listaStr = list(map(str, listaCodigos))
        cursor.close()
        return listaStr


    def eliminar_productos(self, codigo):
        cursor = self.cnxn.cursor()
        cursor.execute("DELETE FROM registroAlmacen WHERE codigo = ?", codigo)
        act = cursor.rowcount
        self.cnxn.commit() 
        cursor.close()
        return act  #devuelve el numero de datos eliminados 

    def lista_datos(self):
        cursor = self.cnxn.cursor()
        cursor.execute("SELECT * FROM registroAlmacen")
        listaDatos = cursor.fetchall()
        cursor.close()
        return listaDatos

    def busca_producto(self, codigo):
        cursor = self.cnxn.cursor()
        cursor.execute('SELECT * FROM registroAlmacen WHERE Codigo =\''+codigo+"\'")
        nombreBD = cursor.fetchall()  #lo asigna a una tupla
        cursor.close()
        return nombreBD

    def lista_codigos(self):
        cursor = self.cnxn.cursor()
        cursor.execute("SELECT * FROM registroAlmacen")
        listaCodigos = [row[0] for row in cursor.fetchall()]
        listaStr = list(map(str, listaCodigos))#Convierte todos los datos de la lista en cadena de texto
        cursor.close()
        return listaStr

    def obtener_stock(self,codigo):
        cursor = self.cnxn.cursor()
        cursor.execute('SELECT Stock FROM registroAlmacen WHERE Codigo =\''+codigo+"\'")
        ct = cursor.fetchone()[0]
        return ct

    def obtener_producto(self,codigo):
        cursor = self.cnxn.cursor()
        cursor.execute('SELECT Producto FROM registroAlmacen WHERE Codigo =\''+codigo+"\'")
        ct = cursor.fetchone()[0]
        return ct

    def obtener_precio(self,codigo):
        cursor = self.cnxn.cursor()
        cursor.execute('SELECT PrecioUnitario FROM registroAlmacen WHERE Codigo =\''+codigo+"\'")
        ct = cursor.fetchone()[0]
        return ct

