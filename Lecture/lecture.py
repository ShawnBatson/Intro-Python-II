# composition relationship
# player HAS-A class/profession

# inheritance
# sneaker IS-A product.  sneaker cannot exist without a product class to inherit properties from

class Product:
    def __init__(self, name, price, discount=0):
        self.name = name
        self.price = price
        self.discount = discount

    def __str__(self):
        return f"{self.name}: ${self.price}"


class Sneaker(Product):
    def __init__(self, name, price, shoe_size, brand, color):
        super().__init__(name, price)
        self.shoe_size = shoe_size
        self.brand = brand
        self.color = color


class SoccerBall(Product):
    def __init__(self, name, price, material):
        super().__init__(name, price)
        self.material = material

    def __str__(self):
        return f"{self.name}: ${self.price}, The best {self.material} ball in town"

    def kick(self):
        print("The ball flew away")


nike_free = Sneaker("Nike Free", "100", "9.5", "Nike", "Black")
soccer_ball = SoccerBall("Gildan", "20", "Rubber")
generic_product = Product("Generic Thing", "99.99")

# print(nike_free.name)
print(nike_free)
print(generic_product)
print(soccer_ball)
soccer_ball.kick()
