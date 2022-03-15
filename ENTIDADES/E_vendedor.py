from E_Humano import Persona

class vendedor (Persona):
    def __init__(self,vcodigo, vpaterno, vmaterno, vnombres, vedad, vsexo, vdni,vmodelo,vcantidad,vtotal):
        super().__init__(vcodigo, vpaterno, vmaterno, vnombres, vedad, vsexo, vdni)
        self.__modelo=vmodelo
        self.__cantidad=vcantidad
        self.__total=vtotal
    
    @property  
    def datamodelo(self):
        return self.__modelo

    @datamodelo.setter  
    def datamodelo(self,vmodelo):
        self._modelo=vmodelo
    
    @property  
    def datacantidad(self):
        return self.__cantidad

    @datacantidad.setter  
    def datacantidad(self,vcantidad):
        self._cantidad=vcantidad
    
    @property  
    def datatotal(self):
        return self.__total

    @datatotal.setter  
    def datatotal(self,vtotal):
        self._total=vtotal