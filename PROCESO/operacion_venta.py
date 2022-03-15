import sys
sys.path.append('./ENTIDADES')
from E_Cliente import Cliente as objcliente
from E_vendedor import vendedor as obvendedor
listadatos_venta=[]

def sizelista(listaindicecliente):
    indicecliente=0
    for i in range(0,len(listaindicecliente)):
        indicecliente=i
    return indicecliente

def grabardatos_venta(vcodcliente,vpatc,vmatc,vnomc,vedad,vsexo,vdni,vdireccion,
                    vdistrito,vcodv,vpatv,vmatv,vnomv,vedadv,vsexov,vdniv,vmodelo,vcantidad,vtotal):
    objcliente.datacodigo=vcodcliente
    objcliente.datapaterno=vpatc
    objcliente.datamaterno=vmatc
    objcliente.datanombres=vnomc
    objcliente.dataedad=vedad
    objcliente.datasexo=vsexo
    objcliente.datasexo=vdni
    objcliente.datadireccion=vdireccion
    objcliente.datadistrito=vdistrito
    obvendedor.datacodigo=vcodv
    obvendedor.datapaterno=vpatv
    obvendedor.datamaterno=vmatv
    obvendedor.datanombres=vnomv
    obvendedor.dataedad=vedadv
    obvendedor.datasexo=vsexov
    obvendedor.datadni=vdniv
    obvendedor.datamodelo=vmodelo
    obvendedor.datacantidad=vcantidad
    obvendedor.datatotal=vtotal

    listadatos_venta.extend([objcliente.datacodigo,objcliente.datapaterno,objcliente.datamaterno,objcliente.datanombres,
                            objcliente.dataedad,objcliente.datasexo,objcliente.datadni,objcliente.datadireccion,objcliente.datadistrito,
                            obvendedor.datacodigo,obvendedor.datapaterno,obvendedor.datamaterno,obvendedor.datanombres,
                            obvendedor.dataedad,obvendedor.datasexo,obvendedor.datadni,obvendedor.datamodelo,
                            obvendedor.datacantidad,obvendedor.datatotal])
