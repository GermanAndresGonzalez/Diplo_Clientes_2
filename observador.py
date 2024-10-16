class Sujeto:
    observers = []

    def agregar(self, obj):
        self.observers.append(obj)

    def notificar(self, *args):
        for observador in self.observers:
            observador.update(*args)


class ObservadorPrincipal:
    def update(self):
        raise NotImplementedError("Delegación de actualización")


class Observer(ObservadorPrincipal):
    def __init__(self, obj):
        self.observed = obj
        self.observed.agregar(self)
        print(self.observed.observers)

    def update(self, *args):
        print("\n", "Actualización del observador", "\n")
        print("Estado = ", args, "\n")
