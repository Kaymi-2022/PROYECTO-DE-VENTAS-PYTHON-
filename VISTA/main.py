from ast import Lambda
from optparse import Values
from sqlite3 import Cursor
import sys
from typing_extensions import Self

from numpy import insert
sys.path.append('./CONEXION')
sys.path.append('./PROCESO')
from turtle import clone
from PyQt6.QtWidgets import *
from PyQt6.QtWidgets import QApplication, QMainWindow, QGraphicsDropShadowEffect
from PyQt6.QtCore import QPropertyAnimation, Qt
from PyQt6.QtGui import *
from PyQt6 import QtWidgets,QtGui
from menu import Ui_MainWindow
from conexion import Registro_datos
from configTabla import configuracionTabla as  config
import operacion_venta as obventa


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.initUi()
        self.datosTotal = Registro_datos()
        
    def initUi(self):
        self.show()
        # eliminar barra y de titulo - opacidad
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)        

        #SizeGrip
        # proporciona un controlador de cambio de tamaño para cambiar el tamaño de las ventanas de nivel superior.
        self.gripSize = 10
        self.grip = QtWidgets.QSizeGrip(self)
        self.grip.resize(self.gripSize, self.gripSize)

        # LLENAR COMBO BOX
        self.ui.comboBox_cliente.addItem("SEXO...........")
        self.ui.comboBox_cliente.addItem("MASCULINO")
        self.ui.comboBox_cliente.addItem("FEMEMNINO")
        self.ui.combo_sexov.addItem("SEXO...........")
        self.ui.combo_sexov.addItem("MASCULINO")
        self.ui.combo_sexov.addItem("FEMEMNINO")

        modelo=["ELIGA EL MODELO.......","SAMSUNG GALAXY S22 ULTRA","MOTOROLA G20",
                "SAMSUNG GALAXY A22"]
        self.ui.combo_modelo.addItem(modelo[0])
        self.ui.combo_modelo.addItem(modelo[1])
        self.ui.combo_modelo.addItem(modelo[2])
        self.ui.combo_modelo.addItem(modelo[3])

        
        # botones de control para mover los menus del JFrame
        self.ui.b_menu.clicked.connect(self.mover_menu)
        self.ui.b_minimizar.clicked.connect(self.control_minimizar)
        self.ui.b_restaurar.clicked.connect(self.control_normal)
        self.ui.b_maximizar.clicked.connect(self.control_maximizar)
        self.ui.b_cerrar.clicked.connect(self.salir)
        self.ui.b_restaurar.hide()
        self.ui.b_cacular.clicked.connect(self.calcular)
        self.ui.b_resumen.clicked.connect(self.m_ventas)
        self.ui.b_resumen2.clicked.connect(self.m_ventas2)
        self.ui.b_resumen3.clicked.connect(self.m_ventas3)
        self.ui.b_grabar.clicked.connect(self.grabar)
        self.ui.b_buscar.clicked.connect(self.buscar_cliente)
        self.ui.b_borrar.clicked.connect(self.eliminar_cliente)
        self.ui.b_actualizar.clicked.connect(self.modificar_ventas)


        # ACCESO A LAS PAGINAS DE STACK
        self.ui.b_cliente.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_1))	
        self.ui.b_vendedor.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))	
        self.ui.b_venta.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_3))	
        self.ui.b_producto.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_4))	
        self.ui.b_reporte.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page))	

        # CONECTAR AL COMBO BOX
        self.ui.combo_modelo.activated.connect(self.seleccion_producto)
        
        #ANCHO DE FILA
        config.tabla1(self)
        config.tabla2(self)
        config.tabla3(self)

        #utilizamos estilos sombra en los widgets
        self.sombra_frame(self.ui.stackedWidget)
        self.sombra_frame(self.ui.stackedWidget_2)
        self.sombra_frame(self.ui.tableWidget)
        self.sombra_frame(self.ui.tableWidget_2)
        self.sombra_frame(self.ui.tableWidget_6)
        self.sombra_frame(self.ui.b_actualizar)
        self.sombra_frame(self.ui.b_borrar)
        self.sombra_frame(self.ui.b_buscar)
        self.sombra_frame(self.ui.b_cacular)
        self.sombra_frame(self.ui.b_cacular_2)
        self.sombra_frame(self.ui.b_cerrar)
        self.sombra_frame(self.ui.b_cliente)
        self.sombra_frame(self.ui.b_contado)
        self.sombra_frame(self.ui.b_efectivo)
        self.sombra_frame(self.ui.b_grabar)
        self.sombra_frame(self.ui.b_restaurar)
        self.sombra_frame(self.ui.b_reporte)
        self.sombra_frame(self.ui.b_resumen)
        self.sombra_frame(self.ui.b_resumen2)
        self.sombra_frame(self.ui.b_resumen3)

    def sombra_frame(self, frame):
        sombra = QGraphicsDropShadowEffect(self)
        sombra.setBlurRadius(10)
        sombra.setXOffset(10)
        sombra.setYOffset(10)
        sombra.setColor(QColor(228, 216, 240, 94))   #setColor(#999999) 
        frame.setGraphicsEffect(sombra)

    def seleccion_producto(self):    
        indice=self.ui.combo_modelo.currentIndex()
        imagen=["",".\\VISTA/IMAGENES/S22.png",
        ".\\VISTA/IMAGENES/Moto-G20-EE.png",
        ".\\VISTA/IMAGENES/A22.png"]
        CAM=["","CAMARA FRONTAL DE 48 MP F1.8 OIS","CAMARA FRONTAL DE 13 MP",
            "CAMARA FRONTAL DE 8 MP"]
        MEMO=["","64GB Y 128 GB EXPANDIBLE HASTA 1TB","64GB EXPANDIBLE HASTA 1TB",
                "64/128 GB Memoria SD de hasta 1 TB"]
        PES=["","163,3 x 77,9 x 8,9 milímetros 227 gramos","165.22 x 75.73 x 9.14 mm 200 gr.",
                "167,2 x 76,4 x 9 mm 203 gramos"]
        COST=[0,5399.00,949.00,1389.00]
        imagen_url=imagen[indice]
        camara=CAM[indice]
        memoria=MEMO[indice]
        peso=PES[indice]
        costo=COST[indice]
        self.ui.lb_imagen.setPixmap(QtGui.QPixmap(imagen_url))
        self.ui.lb_camara.setText(camara)
        self.ui.lb_memoria.setText(memoria)
        self.ui.lb_peso.setText(peso)
        self.ui.lb_precio.setText(str(costo))

        
    def mover_menu(self):
        if True:
            width = self.ui.frame.width()
            normal= 0
            if width == 0:
                extender =300
                self.ui.b_menu.show()
            else:
                self.ui.b_menu.show()
                extender = normal
            self.animacion = QPropertyAnimation((self.ui.frame), b"maximumWidth")
            self.animacion.setStartValue(width)
            self.animacion.setEndValue(extender)
            self.animacion.setDuration(100)
            self.animacion.start()

    def control_minimizar(self):
        self.showMinimized()        

    def  control_normal(self): 
        self.showNormal()       
        self.ui.b_restaurar.hide()
        self.ui.b_maximizar.show()

    def  control_maximizar(self): 
        self.showMaximized()
        self.ui.b_maximizar.hide()
        self.ui.b_restaurar.show()
    
    def salir(self):
        opcion=QMessageBox.question(self,"SALIR","ESTA SEGURO DE SALIR DEL SISTEMA?",
                    QMessageBox.StandardButton.Yes|QMessageBox.StandardButton.No)
        if opcion==QMessageBox.StandardButton.Yes:
            self.close()
    
    def calcular(self):
        valor_spinbox=int(self.ui.spinBox_cantidad.text())
        precio=float(self.ui.lb_precio.text())
        monto_total=valor_spinbox*precio
        igv=monto_total*0.18
        total=monto_total-igv
        self.ui.lb_igv.setText(str(round(igv,2)))
        self.ui.lb_precio_2.setText(str(round(total,2)))
        self.ui.lb_total.setText(str(round(monto_total,2)))
    
    def nuevo (self):
        self.ui.lb_imagen.setText("")
        self.ui.lb_camara.setText("")
        self.ui.lb_memoria.setText("")
        self.ui.lb_peso.setText("")
        self.ui.lb_precio.setText("")
        self.ui.lb_precio_2.setText("")
        self.ui.lb_igv.setText("")
        self.ui.lb_total.setText("")
        self.ui.combo_modelo.setCurrentIndex(0)
        self.ui.spinBox_cantidad.setValue(0)
        self.ui.tableWidget.clearContents()

    
    def grabar (self):
        codigo_c=self.ui.ln_codigoc.text()
        paterno_c=self.ui.ln_paternoc.text().upper()
        materno_c=self.ui.ln_maternoc.text().upper()
        nombres_c=self.ui.ln_nombrec.text().upper()
        edad_c=str(self.ui.spinBox_cliente.value())
        sexos_c=self.ui.comboBox_cliente.itemText(self.ui.comboBox_cliente.currentIndex())
        dni_c=self.ui.ln_dnic.text()
        codigo_v=(self.ui.ln_codigov.text())
        paterno_v=self.ui.ln_paternov.text().upper()
        materno_v=self.ui.ln_maternov.text().upper()
        nombres_v=self.ui.ln_nombrev.text().upper()
        edad_v=str(self.ui.spinBox_v.value())
        sexos_v=self.ui.combo_sexov.itemText(self.ui.comboBox_cliente.currentIndex())
        dni_v=self.ui.ln_dniv.text()
        modelo=self.ui.combo_modelo.itemText(self.ui.combo_modelo.currentIndex())
        cantidad=str(self.ui.spinBox_cantidad.value())
        total=str(self.ui.lb_total.text())
        direccion_c=self.ui.ln_direccionc.text().upper()
        distrito_c=self.ui.ln_distritoc.text().upper()
        self.datosTotal.inserta_venta(codigo_c,paterno_c,materno_c,nombres_c,edad_c,sexos_c,dni_c,direccion_c,distrito_c,
        codigo_v,paterno_v,materno_v,nombres_v,edad_v,sexos_v,dni_v,modelo,cantidad,total)
        self.ui.ln_codigoc.clear()
        self.ui.ln_paternoc.clear()
        self.ui.ln_maternoc.clear()
        self.ui.spinBox_cliente.clear()
        self.ui.comboBox_cliente.setCurrentIndex(0)
        self.ui.ln_dnic.clear()
        self.ui.ln_codigov.clear()
        self.ui.ln_paternov.clear()
        self.ui.ln_maternov.clear()
        self.ui.ln_nombrev.clear()
        self.ui.spinBox_v.clear()
        self.ui.combo_sexov.setCurrentIndex(0)
        self.ui.ln_dniv.clear()
        self.ui.combo_modelo.setCurrentIndex(0)
        self.ui.spinBox_cantidad.clear()
        self.ui.lb_total.clear()
        self.ui.ln_direccionc.clear()
        self.ui.ln_distritoc.clear()
        QMessageBox.information(self,"REGISTRO","DATOS DEL CLIENTE REGISTRADO")

    def m_ventas(self):
        datos = self.datosTotal.mostrar_venta()
        i = len(datos)

        self.ui.tableWidget.setRowCount(i)
        indicefila = 0
        for data in datos:
            self.ui.tableWidget.setItem(indicefila,0,QtWidgets.QTableWidgetItem(str(data[0])))
            self.ui.tableWidget.setItem(indicefila,1,QtWidgets.QTableWidgetItem(data[1]))
            self.ui.tableWidget.setItem(indicefila,2,QtWidgets.QTableWidgetItem(data[2]))
            self.ui.tableWidget.setItem(indicefila,3,QtWidgets.QTableWidgetItem(data[3]))
            self.ui.tableWidget.setItem(indicefila,4,QtWidgets.QTableWidgetItem(str(data[4])))
            self.ui.tableWidget.setItem(indicefila,5,QtWidgets.QTableWidgetItem(data[5]))
            self.ui.tableWidget.setItem(indicefila,6,QtWidgets.QTableWidgetItem(data[6]))
            self.ui.tableWidget.setItem(indicefila,7,QtWidgets.QTableWidgetItem(data[7]))
            self.ui.tableWidget.setItem(indicefila,8,QtWidgets.QTableWidgetItem(data[8]))
            self.ui.tableWidget.setItem(indicefila,9,QtWidgets.QTableWidgetItem(str(data[9])))
            self.ui.tableWidget.setItem(indicefila,10,QtWidgets.QTableWidgetItem(data[10]))
            self.ui.tableWidget.setItem(indicefila,11,QtWidgets.QTableWidgetItem(data[11]))
            self.ui.tableWidget.setItem(indicefila,12,QtWidgets.QTableWidgetItem(data[12]))
            self.ui.tableWidget.setItem(indicefila,13,QtWidgets.QTableWidgetItem(str(data[13])))
            self.ui.tableWidget.setItem(indicefila,14,QtWidgets.QTableWidgetItem(data[14]))
            self.ui.tableWidget.setItem(indicefila,15,QtWidgets.QTableWidgetItem(data[15]))
            self.ui.tableWidget.setItem(indicefila,16,QtWidgets.QTableWidgetItem(data[16]))
            self.ui.tableWidget.setItem(indicefila,17,QtWidgets.QTableWidgetItem(data[17]))
            self.ui.tableWidget.setItem(indicefila,18,QtWidgets.QTableWidgetItem(data[18]))
            indicefila+=1

    def m_ventas2(self):
        datos = self.datosTotal.mostrar_venta()
        i = len(datos)

        self.ui.tableWidget_6.setRowCount(i)
        indicefila = 0
        for data in datos:
            self.ui.tableWidget_6.setItem(indicefila,0,QtWidgets.QTableWidgetItem(str(data[0])))
            self.ui.tableWidget_6.setItem(indicefila,1,QtWidgets.QTableWidgetItem(data[1]))
            self.ui.tableWidget_6.setItem(indicefila,2,QtWidgets.QTableWidgetItem(data[2]))
            self.ui.tableWidget_6.setItem(indicefila,3,QtWidgets.QTableWidgetItem(data[3]))
            self.ui.tableWidget_6.setItem(indicefila,4,QtWidgets.QTableWidgetItem(str(data[4])))
            self.ui.tableWidget_6.setItem(indicefila,5,QtWidgets.QTableWidgetItem(data[5]))
            self.ui.tableWidget_6.setItem(indicefila,6,QtWidgets.QTableWidgetItem(data[6]))
            self.ui.tableWidget_6.setItem(indicefila,7,QtWidgets.QTableWidgetItem(data[7]))
            self.ui.tableWidget_6.setItem(indicefila,8,QtWidgets.QTableWidgetItem(data[8]))
            self.ui.tableWidget_6.setItem(indicefila,9,QtWidgets.QTableWidgetItem(str(data[9])))
            self.ui.tableWidget_6.setItem(indicefila,10,QtWidgets.QTableWidgetItem(data[10]))
            self.ui.tableWidget_6.setItem(indicefila,11,QtWidgets.QTableWidgetItem(data[11]))
            self.ui.tableWidget_6.setItem(indicefila,12,QtWidgets.QTableWidgetItem(data[12]))
            self.ui.tableWidget_6.setItem(indicefila,13,QtWidgets.QTableWidgetItem(str(data[13])))
            self.ui.tableWidget_6.setItem(indicefila,14,QtWidgets.QTableWidgetItem(data[14]))
            self.ui.tableWidget_6.setItem(indicefila,15,QtWidgets.QTableWidgetItem(data[15]))
            self.ui.tableWidget_6.setItem(indicefila,16,QtWidgets.QTableWidgetItem(data[16]))
            self.ui.tableWidget_6.setItem(indicefila,17,QtWidgets.QTableWidgetItem(data[17]))
            self.ui.tableWidget_6.setItem(indicefila,18,QtWidgets.QTableWidgetItem(data[18]))
            indicefila+=1

    def m_ventas3(self):
        datos = self.datosTotal.mostrar_venta()
        i = len(datos)

        self.ui.tableWidget_2.setRowCount(i)
        indicefila = 0
        for data in datos:
            self.ui.tableWidget_2.setItem(indicefila,0,QtWidgets.QTableWidgetItem(str(data[0])))
            self.ui.tableWidget_2.setItem(indicefila,1,QtWidgets.QTableWidgetItem(data[1]))
            self.ui.tableWidget_2.setItem(indicefila,2,QtWidgets.QTableWidgetItem(data[2]))
            self.ui.tableWidget_2.setItem(indicefila,3,QtWidgets.QTableWidgetItem(data[3]))
            self.ui.tableWidget_2.setItem(indicefila,4,QtWidgets.QTableWidgetItem(str(data[4])))
            self.ui.tableWidget_2.setItem(indicefila,5,QtWidgets.QTableWidgetItem(data[5]))
            self.ui.tableWidget_2.setItem(indicefila,6,QtWidgets.QTableWidgetItem(data[6]))
            self.ui.tableWidget_2.setItem(indicefila,7,QtWidgets.QTableWidgetItem(data[7]))
            self.ui.tableWidget_2.setItem(indicefila,8,QtWidgets.QTableWidgetItem(data[8]))
            self.ui.tableWidget_2.setItem(indicefila,9,QtWidgets.QTableWidgetItem(str(data[9])))
            self.ui.tableWidget_2.setItem(indicefila,10,QtWidgets.QTableWidgetItem(data[10]))
            self.ui.tableWidget_2.setItem(indicefila,11,QtWidgets.QTableWidgetItem(data[11]))
            self.ui.tableWidget_2.setItem(indicefila,12,QtWidgets.QTableWidgetItem(data[12]))
            self.ui.tableWidget_2.setItem(indicefila,13,QtWidgets.QTableWidgetItem(str(data[13])))
            self.ui.tableWidget_2.setItem(indicefila,14,QtWidgets.QTableWidgetItem(data[14]))
            self.ui.tableWidget_2.setItem(indicefila,15,QtWidgets.QTableWidgetItem(data[15]))
            self.ui.tableWidget_2.setItem(indicefila,16,QtWidgets.QTableWidgetItem(data[16]))
            self.ui.tableWidget_2.setItem(indicefila,17,QtWidgets.QTableWidgetItem(data[17]))
            self.ui.tableWidget_2.setItem(indicefila,18,QtWidgets.QTableWidgetItem(data[18]))
            indicefila+=1

    def buscar_cliente(self):
        d=self.ui.lineEdit.text()
        d="'"+d+"'"
        self.ui.lineEdit.clear()
        self.ui.lineEdit.setFocus()
        datos = self.datosTotal.busca_venta(d)
        i = len(datos)

        self.ui.tableWidget.setRowCount(i)
        indicefila = 0
        for data in datos:
            self.ui.tableWidget.setItem(indicefila,0,QtWidgets.QTableWidgetItem(str(data[0])))
            self.ui.tableWidget.setItem(indicefila,1,QtWidgets.QTableWidgetItem(data[1]))
            self.ui.tableWidget.setItem(indicefila,2,QtWidgets.QTableWidgetItem(data[2]))
            self.ui.tableWidget.setItem(indicefila,3,QtWidgets.QTableWidgetItem(data[3]))
            self.ui.tableWidget.setItem(indicefila,4,QtWidgets.QTableWidgetItem(str(data[4])))
            self.ui.tableWidget.setItem(indicefila,5,QtWidgets.QTableWidgetItem(data[5]))
            self.ui.tableWidget.setItem(indicefila,6,QtWidgets.QTableWidgetItem(data[6]))
            self.ui.tableWidget.setItem(indicefila,7,QtWidgets.QTableWidgetItem(data[7]))
            self.ui.tableWidget.setItem(indicefila,8,QtWidgets.QTableWidgetItem(data[8]))
            self.ui.tableWidget.setItem(indicefila,9,QtWidgets.QTableWidgetItem(str(data[9])))
            self.ui.tableWidget.setItem(indicefila,10,QtWidgets.QTableWidgetItem(data[10]))
            self.ui.tableWidget.setItem(indicefila,11,QtWidgets.QTableWidgetItem(data[11]))
            self.ui.tableWidget.setItem(indicefila,12,QtWidgets.QTableWidgetItem(data[12]))
            self.ui.tableWidget.setItem(indicefila,13,QtWidgets.QTableWidgetItem(str(data[13])))
            self.ui.tableWidget.setItem(indicefila,14,QtWidgets.QTableWidgetItem(data[14]))
            self.ui.tableWidget.setItem(indicefila,15,QtWidgets.QTableWidgetItem(data[15]))
            self.ui.tableWidget.setItem(indicefila,16,QtWidgets.QTableWidgetItem(data[16]))
            self.ui.tableWidget.setItem(indicefila,17,QtWidgets.QTableWidgetItem(data[17]))
            self.ui.tableWidget.setItem(indicefila,18,QtWidgets.QTableWidgetItem(data[18]))
            indicefila+=1

    def eliminar_cliente(self):
        paterno=self.ui.codigo_eliminar.text()
        paterno="'"+paterno+"'"
        num_eliminados=self.datosTotal.elimina_venta(paterno)
        datos = self.datosTotal.mostrar_venta()
        i = len(datos)
        if num_eliminados>0:
            QMessageBox.information(self,"CANTIDAD DE DATOS ELIMINADOS","SE ELIMINO "+str(num_eliminados)+" DATOS")
        else:
            QMessageBox.information(self,"CANTIDAD DE DATOS ELIMINADOS","NO HAY DATOS CON ESE CODIGO")

        self.ui.tableWidget_6.setRowCount(i)
        indicefila = 0
        for data in datos:
            self.ui.tableWidget_6.setItem(indicefila,0,QtWidgets.QTableWidgetItem(str(data[0])))
            self.ui.tableWidget_6.setItem(indicefila,1,QtWidgets.QTableWidgetItem(data[1]))
            self.ui.tableWidget_6.setItem(indicefila,2,QtWidgets.QTableWidgetItem(data[2]))
            self.ui.tableWidget_6.setItem(indicefila,3,QtWidgets.QTableWidgetItem(data[3]))
            self.ui.tableWidget_6.setItem(indicefila,4,QtWidgets.QTableWidgetItem(str(data[4])))
            self.ui.tableWidget_6.setItem(indicefila,5,QtWidgets.QTableWidgetItem(data[5]))
            self.ui.tableWidget_6.setItem(indicefila,6,QtWidgets.QTableWidgetItem(data[6]))
            self.ui.tableWidget_6.setItem(indicefila,7,QtWidgets.QTableWidgetItem(data[7]))
            self.ui.tableWidget_6.setItem(indicefila,8,QtWidgets.QTableWidgetItem(data[8]))
            self.ui.tableWidget_6.setItem(indicefila,9,QtWidgets.QTableWidgetItem(str(data[9])))
            self.ui.tableWidget_6.setItem(indicefila,10,QtWidgets.QTableWidgetItem(data[10]))
            self.ui.tableWidget_6.setItem(indicefila,11,QtWidgets.QTableWidgetItem(data[11]))
            self.ui.tableWidget_6.setItem(indicefila,12,QtWidgets.QTableWidgetItem(data[12]))
            self.ui.tableWidget_6.setItem(indicefila,13,QtWidgets.QTableWidgetItem(str(data[13])))
            self.ui.tableWidget_6.setItem(indicefila,14,QtWidgets.QTableWidgetItem(data[14]))
            self.ui.tableWidget_6.setItem(indicefila,15,QtWidgets.QTableWidgetItem(data[15]))
            self.ui.tableWidget_6.setItem(indicefila,16,QtWidgets.QTableWidgetItem(data[16]))
            self.ui.tableWidget_6.setItem(indicefila,17,QtWidgets.QTableWidgetItem(data[17]))
            self.ui.tableWidget_6.setItem(indicefila,18,QtWidgets.QTableWidgetItem(data[18]))
            indicefila+=1
            
    def modificar_ventas (self):
        d=self.ui.a_codigov_2.text()
        d="'"+d+"'"
        confirmar=self.datosTotal.busca_venta(d)

        if confirmar!=0:
            codigo_c=self.ui.a_codigov_2.text()
            paterno_c=self.ui.a_paternoc.text().upper()
            materno_c=self.ui.a_maternoc.text().upper()
            nombres_c=self.ui.a_nombresc.text().upper()
            edad_c=str(self.ui.a_edadc.text())
            sexos_c=self.ui.a_sexoc.text().upper()
            direccion_c=self.ui.a_direccionc.text().upper()
            distrito_c=self.ui.a_distritoc.text().upper()
            dni_c=str(self.ui.a_dnic.text())
            codigo_v=self.ui.a_codigov.text().upper()
            paterno_v=self.ui.a_paternov.text().upper()
            materno_v=self.ui.a_maternov.text().upper()
            nombres_v=self.ui.a_nombresv.text().upper()
            edad_v=str(self.ui.a_edadv.text())
            sexos_v=self.ui.a_sexov.text().upper()
            dni_v=str(self.ui.a_dniv.text())
            modelo=self.ui.a_modelo.text().upper()
            cantidad=str(self.ui.a_cantidad.text())
            total=str(self.ui.a_pago.text().upper())
            conf=self.datosTotal.actualiza_venta(int(codigo_c),paterno_c,materno_c,nombres_c,int(edad_c),sexos_c,dni_c,direccion_c,distrito_c,
            int(codigo_v),paterno_v,materno_v,nombres_v,int(edad_v),sexos_v,dni_v,modelo,cantidad,total)

            if conf==1:
                QMessageBox.information(self,"ACTUALIZACION","CONFIRMADA")
                datos = self.datosTotal.mostrar_venta()
                i = len(datos)

                self.ui.tableWidget_2.setRowCount(i)
                indicefila = 0
                for data in datos:
                    self.ui.tableWidget_2.setItem(indicefila,1,QtWidgets.QTableWidgetItem(str(data[0])))
                    self.ui.tableWidget_2.setItem(indicefila,1,QtWidgets.QTableWidgetItem(data[1]))
                    self.ui.tableWidget_2.setItem(indicefila,2,QtWidgets.QTableWidgetItem(data[2]))
                    self.ui.tableWidget_2.setItem(indicefila,3,QtWidgets.QTableWidgetItem(data[3]))
                    self.ui.tableWidget_2.setItem(indicefila,4,QtWidgets.QTableWidgetItem(str(data[4])))
                    self.ui.tableWidget_2.setItem(indicefila,5,QtWidgets.QTableWidgetItem(data[5]))
                    self.ui.tableWidget_2.setItem(indicefila,6,QtWidgets.QTableWidgetItem(data[6]))
                    self.ui.tableWidget_2.setItem(indicefila,7,QtWidgets.QTableWidgetItem(data[7]))
                    self.ui.tableWidget_2.setItem(indicefila,8,QtWidgets.QTableWidgetItem(data[8]))
                    self.ui.tableWidget_2.setItem(indicefila,9,QtWidgets.QTableWidgetItem(str(data[9])))
                    self.ui.tableWidget_2.setItem(indicefila,10,QtWidgets.QTableWidgetItem(data[10]))
                    self.ui.tableWidget_2.setItem(indicefila,11,QtWidgets.QTableWidgetItem(data[11]))
                    self.ui.tableWidget_2.setItem(indicefila,12,QtWidgets.QTableWidgetItem(data[12]))
                    self.ui.tableWidget_2.setItem(indicefila,13,QtWidgets.QTableWidgetItem(str(data[13])))
                    self.ui.tableWidget_2.setItem(indicefila,14,QtWidgets.QTableWidgetItem(data[14]))
                    self.ui.tableWidget_2.setItem(indicefila,15,QtWidgets.QTableWidgetItem(data[15]))
                    self.ui.tableWidget_2.setItem(indicefila,16,QtWidgets.QTableWidgetItem(data[16]))
                    self.ui.tableWidget_2.setItem(indicefila,17,QtWidgets.QTableWidgetItem(data[17]))
                    self.ui.tableWidget_2.setItem(indicefila,18,QtWidgets.QTableWidgetItem(data[18]))
                    indicefila+=1
                self.ui.a_codigov_2.clear()
                self.ui.a_paternoc.clear()
                self.ui.a_maternoc.clear()
                self.ui.a_nombresc.clear()
                self.ui.a_edadc.clear()
                self.ui.a_sexoc.clear()
                self.ui.a_direccionc.clear()
                self.ui.a_distritoc.clear()
                self.ui.a_dnic.clear()
                self.ui.a_codigov.clear()
                self.ui.a_paternov.clear()
                self.ui.a_maternov.clear()
                self.ui.a_nombresv.clear()
                self.ui.a_edadv.clear()
                self.ui.a_sexov.clear()
                self.ui.a_dniv.clear()
                self.ui.a_modelo.clear()
                self.ui.a_cantidad.clear()
                self.ui.a_pago.clear()
                self.ui.a_codigov_2.setFocus()
            elif conf==0:
                QMessageBox.information(self,"ACTUALIZACION","ERROR")
            else:
                QMessageBox.information(self,"ACTUALIZACION","INCORRECTO")

if __name__=='__main__':
    app=QApplication(sys.argv)
    mi_app=VentanaPrincipal()
    mi_app.show()
    sys.exit(app.exec())