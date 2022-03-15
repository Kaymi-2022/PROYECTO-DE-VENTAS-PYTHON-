import sys
sys.path.append('./ENTIDADES')
from E_vendedor import vendedor as obvendedor
listadatos_vendedor=[]

def grabardatos_vendedor(vcodv,vpatv,vmatv,vnomv,vedad,vsexo,vdni,vmodelo,vcantidad,vtotal):
    obvendedor.datacodigo=vcodv
    obvendedor.datapaterno=vpatv
    obvendedor.datamaterno=vmatv
    obvendedor.datanombres=vnomv
    obvendedor.dataedad=vedad
    obvendedor.datasexo=vsexo
    obvendedor.datadni=vdni
    obvendedor.datamodelo=vmodelo
    obvendedor.datacantidad=vcantidad
    obvendedor.datatotal=vtotal

    listadatos_vendedor.extend([obvendedor.datacodigo,obvendedor.datapaterno,obvendedor.datamaterno,obvendedor.datanombres,
                                obvendedor.dataedad,obvendedor.datasexo,obvendedor.datadni,obvendedor.datamodelo,
                                obvendedor.datacantidad,obvendedor.datatotal])
