import pyodbc

class Registro_datos():


    def __init__(self):
        server= 'DESKTOP-CI404GT\MICHAELSQL'
        bd= 'PROYECTO2'
        user = 'Empresa'
        contrasena ='123456'

        try:
            self.conexion= pyodbc.connect('Driver={ODBC Driver 17 for SQL server};SERVER='+server+
                                    ';DATABASE='+bd+
                                    ';UID='+user+
                                    ';PWD='+contrasena)
            print("exitosa")

        except Exception as mensaje:
            print('ERROR DE CONEXION: ',mensaje)
        
    def mostrar_imagenes(self,modelo,camara,memoria,peso):
        cursor=self.conexion.cursor()
        cursor.execute(''' SELECT MODELO,CAMARA,MEMORIA,IMAGEN FROM EQUIPOS ''')

    def inserta_venta(self,codigo_c,paterno_c,materno_c,nombres_c,edad_c,sexos_c,dni_c,direccion_c,distrito_c,
        codigo_v,paterno_v,materno_v,nombres_v,edad_v,sexos_v,dni_v,modelo,cantidad,total):
        cursor=self.conexion.cursor()
        cursor.execute('{call LISTADO_VENTA (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)}',(codigo_c,paterno_c,materno_c,nombres_c,edad_c,sexos_c,dni_c,direccion_c,distrito_c,
        codigo_v,paterno_v,materno_v,nombres_v,edad_v,sexos_v,dni_v,modelo,cantidad,total))
        self.conexion.commit()    
        cursor.close()

    def mostrar_venta(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM VENTA" 
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro

    def busca_venta(self, pate_cliente):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM VENTA WHERE PATERNO = {}".format(pate_cliente)
        cursor.execute(sql)
        codigo_cliente = cursor.fetchall()
        cursor.close()     
        return codigo_cliente 

    def elimina_venta(self,pate_cliente):
        cursor = self.conexion.cursor()
        sql='''DELETE FROM VENTA WHERE PATERNO = {}'''.format(pate_cliente)
        cursor.execute(sql)
        valor = cursor.rowcount
        self.conexion.commit()    
        cursor.close()
        return valor

    def actualiza_venta(self, paterno_c,materno_c,nombres_c,edad_c,sexos_c,dni_c,direccion_c,distrito_c,
        codigo_v,paterno_v,materno_v,nombres_v,edad_v,sexos_v,dni_v,modelo,cantidad,total,codigo):
        cursor = self.conexion.cursor()
        cursor.execute('{call CAMBIO_VENTA (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)}',(paterno_c,materno_c,nombres_c,edad_c,sexos_c,dni_c,direccion_c,distrito_c,
        codigo_v,paterno_v,materno_v,nombres_v,edad_v,sexos_v,dni_v,modelo,cantidad,total,codigo))
        valor = cursor.rowcount
        self.conexion.commit()    
        cursor.close()
        return valor
    
    # actualiza_venta(145,"MASCCO","LUQUE","MICHAEL","33","MASCULINO","45090133","MZ J LT 5","LOS OLIVOS",500,
    # "RODRIGUEZ","MARON","RONALD","35","MASCULINO"   ,"42086144","HIRAOKA","15","3500")




