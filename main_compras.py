# main_compras.py
from cliente import Cliente

# Crear instancias de la clase Cliente
cliente1 = Cliente("Juan Perez", "juan@gmail.com", "Calle 123", 1000)
cliente2 = Cliente("Maria Lopez", "maria@gmail.com", "Avenida XYZ", 1500)

# Mostrar información utilizando el método __str__()
print(cliente1)
print(cliente2)

# Realizar compras
cliente1.realizar_compra(500)
cliente2.realizar_compra(2000)

# Actualizar direcciones
cliente1.actualizar_direccion("Calle Nueva 456")
cliente2.actualizar_direccion("Avenida Principal")

# Mostrar información actualizada
print(cliente1)
print(cliente2)

# Gestionar usuarios
miDato = {}
registro_login(miDato)
guardar_datos(miDato)
leer_datos(miDato)