from E_Humano import Persona

class Cliente(Persona):

    def __init__(self, vcodigo, vpaterno, vmaterno, vnombres, vedad,vdni, vsexo, vdireccion, vdistrito):
        super().__init__(vcodigo, vpaterno, vmaterno, vnombres, vedad, vsexo,vdni,vdireccion, vdistrito)

