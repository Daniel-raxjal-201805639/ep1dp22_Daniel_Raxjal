from Publicos import Publicos

class Mixtos(Publicos):
    cantidad_hombres=0
    cantidad_mujeres=0

    def  VerDatosMixtos(self):
        super().VerDatosPublicos()
        print("cantidad de hombres:",self.cantidad_hombres,"cantidad de mujeres:",self.cantidad_mujeres)