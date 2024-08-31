class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products


obj = Product('camera', 'for streaming', 15000, 'good')

print(obj.price)
