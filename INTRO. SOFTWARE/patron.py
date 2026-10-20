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

class FoodItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price


class MealOrder:
    def __init__(self, patron, food_item1, date, status,
                payment_method, delivery_location, delivery_time):
        self.patron = patron
        self.items = [food_item1]
        self.date = date
        self.status = status
        self.payment_method = payment_method
        self.delivery_location = delivery_location
        self.delivery_time = delivery_time

    def get_patron(self):
        return self.patron

    def get_items(self):
        return self.items

    def get_date(self):
        return self.date

    def get_status(self):
        return self.status

    def get_payment_method(self):
        return self.payment_method

    def get_delivery_location(self):
        return self.delivery_location

    def get_delivery_time(self):
        return self.delivery_time

    def add_item(self, item):
        self.items.append(item)

patron1 = Patron("Juan", "juan@example.com", "123-456-7890")
patron2 = Patron("Maria", "maria@example.com", "098-765-4321")

food_item1 = FoodItem("Vegetable soup", 45.0)
food_item2 = FoodItem("Chicken sandwich", 65.0)

order1 = MealOrder(patron1, food_item1,
 date="2026-10-12",
 status="Pending",
 payment_method="Card",
 delivery_location="Building A",
 delivery_time="13:00")

order1.add_item(food_item2)

print("Your selected items are:")
for item in order1.get_items():
    print("- " + item.get_name() + ": $" + str(item.get_price()))

print("OBJETO PATRON 1")
print("Nombre: " + patron1.get_name())
print("Correo electrónico: " + patron1.get_email())
print("Teléfono: " + patron1.get_phone())

#NOMBRE, CORREO ELECTRÓNICO Y TELÉFONO ACTUALIZADOS
patron1.set_name ("Diego")
print("Nombre actualizado: " + patron1.get_name())
patron1.set_email("diego@example.com")
print("Correo electrónico actualizado: " + patron1.get_email())
patron1.set_phone("555-555-5555")
print("Teléfono actualizado: " + patron1.get_phone())

print("OBJETO PATRON 2")
print("Nombre: " + patron2.get_name())
print("Correo electrónico: " + patron2.get_email())
print("Teléfono: " + patron2.get_phone())

#NOMBRE, CORREO ELECTRÓNICO Y TELÉFONO ACTUALIZADOS
patron2.set_name("Ana")
print("Nombre actualizado: " + patron2.get_name())
patron2.set_email("ana@example.com")
print("Correo electrónico actualizado: " + patron2.get_email())
patron2.set_phone("666-666-6666")
print("Teléfono actualizado: " + patron2.get_phone())


print("OBJETO FOOD ITEM 1")
print("El primer producto es " + food_item1.get_name())
print("El precio del primer producto es " + str(food_item1.get_price()))

print("OBJETO FOOD ITEM 2")
print("El segundo producto es " + food_item2.get_name())
print("El precio del segundo producto es " + str(food_item2.get_price()))

print("OBJETO ORDER 1")
order_patron = order1.get_patron()
print(order_patron.get_name())

order_items = order1.get_items()
food_item1 = order_items[0]
print(food_item1.get_name())
print(food_item1.get_price())

order_patron = order1.get_patron()

print("OBJETO ORDER 1")
print("Patron:", order_patron.get_name())
print("Date:", order1.get_date())
print("Status:", order1.get_status())
print("Payment:", order1.get_payment_method())
print("Location:", order1.get_delivery_location())
print("Time:", order1.get_delivery_time())

order_items = order1.get_items()

first_item = order_items[0]

print("First item:", first_item.get_name())
print("Number of items:", len(order_items))