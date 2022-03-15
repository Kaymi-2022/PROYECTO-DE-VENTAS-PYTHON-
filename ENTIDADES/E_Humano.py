class Persona(object):
    def __init__(self,vcodigo,vpaterno,vmaterno,vnombres,vedad,vsexo,vdni,vdireccion,vdistrito):
        self.__codigo=vcodigo
        self.__paterno=vpaterno
        self.__materno=vmaterno
        self.__nombres=vnombres
        self.__edad=vedad
        self.__sexo=vsexo
        self.__dni=vdni
        self.__direccion=vdireccion
        self.__distrito=vdistrito

    @property  
    def datacodigo(self):
        return self.__codigo   

    @datacodigo.setter  
    def datacodigo(self,vcodigo):
        self.__codigo=vcodigo  

    @property  
    def datapaterno(self):
        return self.__paterno

    @datapaterno.setter  
    def datapaterno(self,vpaterno):
        self.__paterno=vpaterno

    @property  
    def datamaterno(self):
        return self.__materno

    @datamaterno.setter  
    def datamaterno(self,vmaterno):
        self.__materno=vmaterno    

    @property  
    def datanombres(self):
        return self.__nombres

    @datanombres.setter  
    def datanombres(self,vnombres):
        self.__nombres=vnombres

    @property  
    def dataedad(self):
        return self.__edad

    @dataedad.setter  
    def dataedad(self,vedad):
        self.__edad=vedad         

    @property  
    def datasexo(self):
        return self.__sexo

    @datasexo.setter  
    def datasexo(self,vsexo):
        self.__sexo=vsexo

    @property  
    def datadni(self):
        return self.__dni

    @datasexo.setter  
    def datasexo(self,vsexo):
        self.__sexo=vsexo
        
    @property  
    def datadireccion(self):
        return self.__direccion

    @datadireccion.setter  
    def datadireccion(self,vdireccion):
        self.__direccion=vdireccion

    @property  
    def datadistrito(self):
        return self.__distrito

    @datadistrito.setter  
    def datadistrito(self,vdistrito):
        self.__distrito=vdistrito