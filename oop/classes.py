class Product:
    name: str
    description: str
    price: int
    quantity: str

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    name: str
    description: str
    products: str
    category_count: str
    products_count: str

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products


obj = Product("camera", "for streaming", 15000, "good")
obj_2 = Product("pc", "for playing the game", 150000, "best")
