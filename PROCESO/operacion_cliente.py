import sys
sys.path.append('./ENTIDADES')
from E_Cliente import Cliente as objcliente
filaindicecliente=[]
listadatos_cliente=[]

def sizelista(listaindicecliente):
    indicecliente=0
    for i in range(0,len(listaindicecliente)):
        indicecliente=i
    return indicecliente                     

def grabardatos_cliente(vcodcliente,vpatc,vmatc,vnomc,vedad,vsexo,vdni,vdireccion,vdistrito):
    objcliente.datacodigo=vcodcliente
    objcliente.datapaterno=vpatc
    objcliente.datamaterno=vmatc
    objcliente.datanombres=vnomc
    objcliente.dataedad=vedad
    objcliente.datasexo=vsexo
    objcliente.datasexo=vdni
    objcliente.datadireccion=vdireccion
    objcliente.datadistrito=vdistrito

    listadatos_cliente.extend([objcliente.datacodigo,objcliente.datapaterno,objcliente.datamaterno,objcliente.datanombres,
                                objcliente.dataedad,objcliente.datasexo,objcliente.datadni,objcliente.datadireccion,objcliente.datadistrito])

    