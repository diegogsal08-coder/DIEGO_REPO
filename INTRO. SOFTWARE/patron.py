# Welcome to your Python project!
class Patron:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
    def get_name(self):
        return self.name
        
    def set_name(self, name):
        self.name = name

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def get_phone(self):
        return self.phone

    def set_phone(self, phone):
        self.phone = phone

patron1 = Patron("Juan", "juan@example.com", "123-456-7890")
patron2 = Patron("Maria", "maria@example.com", "098-765-4321")

print("Objeto Patron 1" )
print("Nombre: " + patron1.get_name())
patron1.set_name(input("Ingrese un nuevo nombre para el patron 1: "))
print("Nombre actualizado: " + patron1.get_name())
patron1.set_email(input("Ingrese un nuevo correo electrónico para el patron 1: "))
print("Correo electrónico actualizado: " + patron1.get_email())
patron1.set_phone(input("Ingrese un nuevo número de teléfono para el patron 1: "))
print("Teléfono actualizado: " + patron1.get_phone())

print("Objeto Patron 2")
print("Nombre: " + patron2.get_name())