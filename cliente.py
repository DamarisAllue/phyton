# cliente.py

class Cliente:
    def __init__(self, nombre, correo, direccion, saldo_inicial):
        self.nombre = nombre
        self.correo = correo
        self.direccion = direccion
        self.saldo = saldo_inicial

    def realizar_compra(self, monto):
        if monto > 0 and monto <= self.saldo:
            self.saldo -= monto
            print(f"Compra realizada por {self.nombre}. Saldo restante: {self.saldo}")
        else:
            print(f"No se puede realizar la compra por {self.nombre}. Saldo insuficiente.")

    def actualizar_direccion(self, nueva_direccion):
        self.direccion = nueva_direccion
        print(f"Dirección actualizada para {self.nombre}: {self.direccion}")

    def __str__(self):
        return f"Cliente: {self.nombre}, Correo: {self.correo}, Dirección: {self.direccion}, Saldo: {self.saldo}"