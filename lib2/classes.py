class nodo():
    def __init__(self, valor):
        self.valor=valor
        self.Izq=None
        self.Der=None
        pass

    def __str__(self):
        return f"valor: {self.valor}, Izq: {self.Izq}, Der: {self.Der}"



pass