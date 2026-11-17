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

    def set_name(self, name):
        self.name = name

    def set_price(self, price):
        self.price = price


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

    def set_date(self, date):
        self.date = date

    def get_status(self):
        return self.status

    def set_status(self, status):
        self.status = status

    def get_payment_method(self):
        return self.payment_method

    def set_payment_method(self, payment_method):
        self.payment_method = payment_method

    def get_delivery_location(self):
        return self.delivery_location

    def set_delivery_location(self, delivery_location):
        self.delivery_location = delivery_location

    def get_delivery_time(self):
        return self.delivery_time

    def set_delivery_time(self, delivery_time):
        self.delivery_time = delivery_time

    def add_item(self, item):
        self.items.append(item)

    def calculate_total(self, tax, delivery_charge):
        subtotal = 0.0

        for item in self.items:
            subtotal = subtotal + item.get_price()

        tax_amount = subtotal * tax
        total = subtotal + tax_amount + delivery_charge
        return total

    def confirm(self):
        self.status = "Confirmed"
        return True
    def validate_order(self):
        if not (1 <= len(self.items) <= 5):
            return False

        for item in self.items:
            price = item.get_price()
            if not (10.00 <= price <= 200.00):
                return False
        if self.payment_method not in ["Card", "Payroll", "Cash"]:
            return False
        phone = self.patron.get_phone()
        if not phone.isdigit() or len(phone) != 10:
            return False
        return True

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

#Dar todos los productos de la orden con su precio
order1.add_item(food_item2)
print("Your selected items are:")
order_items = order1.get_items()
for item in order_items:
    print(item.get_name(), (item.get_price()))

#Calcular precio de la orden
total = order1.calculate_total(tax=0.10, delivery_charge=10.0)
print("Total amount to pay: " + str(total))

#Dar estatus del pedido
order1.confirm()
print("Order status: " + order1.get_status())

#order summary final
print("\nORDER SUMMARY")

order_patron = order1.get_patron()

print("Patron:", order_patron.get_name())
print("Date:", order1.get_date())

print("Items:")
for item in order1.get_items():
    print(item.get_name(), item.get_price())

print("Total to pay:", total)
print("Payment method:", order1.get_payment_method())
print("Delivery location:", order1.get_delivery_location())
print("Delivery time:", order1.get_delivery_time())
print("Status:", order1.get_status())

print("\nTEST validate_order()")

# TC01 - Número mínimo de artículos (1)
patron = Patron("Ana Torres", "ana.torres@gmail.com", "5551234567")
order = MealOrder(patron, FoodItem("Chicken sandwich", 10.00), "2026-10-28", "Pending", "Card", "Building A", "12:30")
print("TC01 | Expected: True | Actual:", order.validate_order())

# TC02
patron = Patron("Ana Torres", "ana.torres@gmail.com", "5551234567")
order = MealOrder(patron, FoodItem("Chicken sandwich", 20.00), "2026-10-28", "Pending", "Card", "Building A", "12:30")
order.items = [
    FoodItem("Chicken sandwich", 20.00),
    FoodItem("Soup", 10.00),
    FoodItem("Salad", 30.00),
    FoodItem("Juice", 15.00),
    FoodItem("Cake", 25.00)
]
print("TC02 | Expected: True | Actual:", order.validate_order())
# TC03 - Menos de 1 artículo (0)
patron = Patron("Ana Torres", "ana.torres@gmail.com", "5551234567")
order = MealOrder(patron, FoodItem("Chicken sandwich", 20.00), "2026-10-28", "Pending", "Card", "Building A", "12:30")
order.items = []
print("TC03 | Expected: False | Actual:", order.validate_order())

# TC04
patron = Patron("Ana Torres", "ana.torres@gmail.com", "5551234567")
order = MealOrder(patron, FoodItem("Chicken sandwich", 20.00), "2026-10-28", "Pending", "Card", "Building A", "12:30")
order.items = [
    FoodItem("Chicken sandwich", 20.00),
    FoodItem("Soup", 10.00),
    FoodItem("Salad", 30.00),
    FoodItem("Juice", 15.00),
    FoodItem("Cake", 25.00),
    FoodItem("Pizza", 40.00)
]
print("TC04 | Expected: False | Actual:", order.validate_order())

# TC05 - Precio mínimo (10.00)
patron = Patron("Ana Torres", "ana.torres@gmail.com", "5551234567")
order = MealOrder(patron, FoodItem("Chicken sandwich", 10.00), "2026-10-28", "Pending", "Card", "Building A", "12:30")
print("TC05 | Expected: True | Actual:", order.validate_order())

# TC06 - Precio máximo (200.00)
patron = Patron("Ana Torres", "ana.torres@gmail.com", "5551234567")
order = MealOrder(patron, FoodItem("Chicken sandwich", 200.00), "2026-10-28", "Pending", "Card", "Building A", "12:30")
print("TC06 | Expected: True | Actual:", order.validate_order())

# TC07 - Precio menor a 10.00
patron = Patron("Ana Torres", "ana.torres@gmail.com", "5551234567")
order = MealOrder(patron, FoodItem("Chicken sandwich", 9.99), "2026-10-28", "Pending", "Card", "Building A", "12:30")
print("TC07 | Expected: False | Actual:", order.validate_order())

# TC08 - Precio mayor a 200.00
patron = Patron("Ana Torres", "ana.torres@gmail.com", "5551234567")
order = MealOrder(patron, FoodItem("Chicken sandwich", 200.01), "2026-10-28", "Pending", "Card", "Building A", "12:30")
print("TC08 | Expected: False | Actual:", order.validate_order())

# TC09 - Método de pago Card
patron = Patron("Ana Torres", "ana.torres@gmail.com", "5551234567")
order = MealOrder(patron, FoodItem("Sandwich", 20.00), "2026-10-28", "Pending", "Card", "Building A", "12:30")
print("TC09 | Expected: True | Actual:", order.validate_order())

# TC10 - Método de pago Payroll
patron = Patron("Ana Torres", "ana.torres@gmail.com", "5551234567")
order = MealOrder(patron, FoodItem("Sandwich", 20.00), "2026-10-28", "Pending", "Payroll", "Building A", "12:30")
print("TC10 | Expected: True | Actual:", order.validate_order())

# TC11 - Método de pago Cash
patron = Patron("Ana Torres", "ana.torres@gmail.com", "5551234567")
order = MealOrder(patron, FoodItem("Sandwich", 20.00), "2026-10-28", "Pending", "Cash", "Building A", "12:30")
print("TC11 | Expected: True | Actual:", order.validate_order())

# TC12 - Método de pago inválido
patron = Patron("Ana Torres", "ana.torres@gmail.com", "5551234567")
order = MealOrder(patron, FoodItem("Sandwich", 20.00), "2026-10-28", "Pending", "Transferencia", "Building A", "12:30")
print("TC12 | Expected: False | Actual:", order.validate_order())

# TC13 - Teléfono con 10 dígitos
patron = Patron("Ana Torres", "ana.torres@gmail.com", "1234567890")
order = MealOrder(patron, FoodItem("Sandwich", 20.00), "2026-10-28", "Pending", "Card", "Building A", "12:30")
print("TC13 | Expected: True | Actual:", order.validate_order())

# TC14 - Teléfono con letras
patron = Patron("Ana Torres", "ana.torres@gmail.com", "12345AB890")
order = MealOrder(patron, FoodItem("Sandwich", 20.00), "2026-10-28", "Pending", "Card", "Building A", "12:30")
print("TC14 | Expected: False | Actual:", order.validate_order())

# TC15 - Teléfono con menos de 10 caracteres
patron = Patron("Ana Torres", "ana.torres@gmail.com", "123456789")
order = MealOrder(patron, FoodItem("Sandwich", 20.00), "2026-10-28", "Pending", "Card", "Building A", "12:30")
print("TC15 | Expected: False | Actual:", order.validate_order())

# TC16 - Teléfono con más de 10 caracteres
patron = Patron("Ana Torres", "ana.torres@gmail.com", "12345678901")
order = MealOrder(patron, FoodItem("Sandwich", 20.00), "2026-10-28", "Pending", "Card", "Building A", "12:30")
print("TC16 | Expected: False | Actual:", order.validate_order())