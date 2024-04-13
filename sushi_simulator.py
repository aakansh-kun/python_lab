import numpy as np

# Define the sushi types
sushi_types = np.array(['Salmon', 'Tuna', 'Shrimp', 'Eel', 'Octopus'])

# Simulate the kitchen's sushi preparation
kitchen = np.zeros(len(sushi_types), dtype=int)

# Function to place an order
def place_order(sushi_name, quantity):
    if sushi_name in sushi_types:
        index = np.where(sushi_types == sushi_name)[0][0]
        kitchen[index] += quantity
        print(f"Ordered {quantity} piece(s) of {sushi_name} sushi.")
    else:
        print("Sorry, we don't have that type of sushi.")

# Function to prepare the sushi
def prepare_sushi():
    for i in range(len(kitchen)):
        if kitchen[i] > 0:
            print(f"Preparing {kitchen[i]} piece(s) of {sushi_types[i]} sushi.")
            kitchen[i] = 0

# Example usage
place_order('Salmon', 3)
place_order('Eel', 2)
prepare_sushi()
