import random

class MaidCafe:
    def __init__(self):
        self.menu = {'Tea': 5, 'Cake': 10, 'Coffee': 7}
        self.funds = 100
        self.orders = []

    def show_menu(self):
        print("Welcome to the Maid Cafe!")
        for item, price in self.menu.items():
            print(f"{item}: ${price}")

    def take_order(self):
        print("Please place your order:")
        for item in self.menu.keys():
            quantity = int(input(f"How many {item}s would you like? "))
            self.orders.append((item, quantity))

    def serve_order(self):
        total_cost = 0
        print("Serving the order:")
        for item, quantity in self.orders:
            print(f"{quantity} {item}(s) coming right up!")
            total_cost += self.menu[item] * quantity
        print(f"That will be ${total_cost} please.")
        self.funds += total_cost
        self.orders = []

    def end_day(self):
        print(f"The day has ended. The cafe made ${self.funds} today.")
        # Random event that affects the funds
        event = random.choice(['breakage', 'tip', 'none'])
        if event == 'breakage':
            loss = random.randint(5, 20)
            print(f"Oh no! There was some breakage which cost the cafe ${loss}.")
            self.funds -= loss
        elif event == 'tip':
            tip = random.randint(5, 20)
            print(f"Yay! A generous customer left a tip of ${tip}.")
            self.funds += tip
        print(f"The cafe's total funds are now ${self.funds}.")

# Example usage
cafe = MaidCafe()
cafe.show_menu()
cafe.take_order()
cafe.serve_order()
cafe.end_day()
