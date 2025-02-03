class Conductor:
    def __init__(self, nombre, horario):
        self.nombre = nombre
        self.horario = horario

class Bus:
    def __init__(self, ruta):
        self.ruta = ruta
        self.horarios = []
        self.conductores_asignados = []

    def asignar_conductor(self, conductor):
        self.conductores_asignados.append(conductor)

    def agregar_horario(self, horario):
        self.horarios.append(horario)

class Admin:
    def __init__(self):
        self.buses = []
        self.conductores = []

    def agregar_bus(self, ruta):
        bus = Bus(ruta)
        self.buses.append(bus)
        return bus

    def agregar_ruta_a_bus(self, bus, ruta):
        bus.ruta = ruta

    def registrar_horario_a_bus(self, bus, horario):
        bus.agregar_horario(horario)

    def agregar_conductor(self, nombre, horario):
        for conductor in self.conductores:
            if conductor.horario == horario:
                print("Ya hay un conductor asignado en ese horario.")
                return None
        nuevo_conductor = Conductor(nombre, horario)
        self.conductores.append(nuevo_conductor)
        return nuevo_conductor

    def agregar_horario_a_conductor(self, conductor, horario):
        conductor.horario = horario

    def asignar_bus_a_conductor(self, bus, conductor):
        bus.asignar_conductor(conductor)

# Función para mostrar un menú interactivo
def menu():
    admin = Admin()
    while True:
        print("\n1. Agregar Bus")
        print("2. Agregar Ruta a Bus")
        print("3. Registrar Horario a Bus")
        print("4. Agregar Conductor")
        print("5. Agregar Horario a Conductor")
        print("6. Asignar Bus a Conductor")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            ruta = input("Ingrese la ruta del bus: ")
            admin.agregar_bus(ruta)
        elif opcion == "2":
            bus_idx = int(input("Ingrese el índice del bus al que desea agregar una ruta: "))
            ruta = input("Ingrese la ruta a agregar: ")
            admin.agregar_ruta_a_bus(admin.buses[bus_idx], ruta)
        elif opcion == "3":
            bus_idx = int(input("Ingrese el índice del bus al que desea registrar un horario: "))
            horario = input("Ingrese el horario a registrar: ")
            admin.registrar_horario_a_bus(admin.buses[bus_idx], horario)
        elif opcion == "4":
            nombre = input("Ingrese el nombre del conductor: ")
            horario = input("Ingrese el horario del conductor: ")
            admin.agregar_conductor(nombre, horario)
        elif opcion == "5":
            conductor_idx = int(input("Ingrese el índice del conductor al que desea agregar un horario: "))
            horario = input("Ingrese el nuevo horario a agregar: ")
            admin.agregar_horario_a_conductor(admin.conductores[conductor_idx], horario)
        elif opcion == "6":
            bus_idx = int(input("Ingrese el índice del bus: "))
            conductor_idx = int(input("Ingrese el índice del conductor: "))
            admin.asignar_bus_a_conductor(admin.buses[bus_idx], admin.conductores[conductor_idx])
        elif opcion == "7":
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

menu()