class Customer:
    def __init__(self, id, name, quantity, price, discount):
        self.id = id
        self.name = name
        self.quantity = quantity
        self.price = price
        self.discout = discount
        self.total = price * quantity - discount

    def __str__(self):
        return f'{self.id} {self.name} {self.quantity} {self.price} {self.discout} {self.total}'

if __name__ == '__main__':
    a = []
    for _ in range(int(input())):
        a.append(Customer(input(), input(), int(input()), int(input()), int(input())))
    a.sort(key = lambda x : -x.total)
    for x in a: print(x)

