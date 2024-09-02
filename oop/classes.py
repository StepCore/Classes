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
    category_count: int
    products_count: int

    def __init__(self, name, description, products, category_count, products_count):
        self.name = name
        self.description = description
        self.products = products
        self.category_count = category_count
        self.products_count = products_count


camera = Product("camera", "for streaming", 15000, "good")
pc = Product("pc", "for playing the game", 150000, "best")
gadget = Category("gadget", "digital", "pc", 2, 3)
video = Category("video", "record", "camera", 1, 5)
