__author__ = 'Diego J D Arias - diegojdarias@gmail.com'


class Sujeto:

    _observadores = []

    def agregar(self, obj):
        self._observadores.append(obj)

    def quitar(self, obj):
        pass

    def notificar(self, *args):
        for observador in self._observadores:
            observador.update(args)


class Observador:
    def update(self):
        raise NotImplementedError("Delegación de actualización")


class ObservadorConcretoA(Observador):
    def __init__(self, obj):
        self._observadoA = obj
        self._observadoA.agregar(self)

    def update(self, *args):
        print("Actualización dentro de ObservadorConcretoA")
        print("Los nuevos parámetros son los siguientes: ", args)
