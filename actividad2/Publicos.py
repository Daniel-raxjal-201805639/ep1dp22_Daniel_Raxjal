from Centros import Centros

class Publicos(Centros):
    fecha_creacion=0
    tipo=""
    descripcion=""

    def VerDatosPublicos(self):
        super().VerDatosCentros()
        print("fecha creacion:",self.fecha_creacion,"tipo:",self.tipo,"descripcion:",self.descripcion)