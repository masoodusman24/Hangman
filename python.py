import random

words = ("dog", "cow", "cat", "horse", "donkey", "tiger", "lion", "panther",
         "leopard", "cheetah", "bear", "elephant", "polarbear", "turtle",
         "tortoise", "crocodile", "rabbit", "porcupine", "hare", "hen", "pigeon",
         "albatross", "crow", "fish", "dolphin", "frog", "whale", "alligator",
         "eagle", "squirrel", "ostrich", "fox", "goat", "jackal", "emu", "armadillo",
         "eel", "goose", "wolf", "beagle", "gorilla", "chimpanzee", "monkey")

hang_man = {0: ("    ",
                "    ",
                "    "),
            1: ("  o ",
                "    ",
                "    "),
            2: ("  o ",
                "  | ",
                "    "),
            3: ("  o ",
                " /| ",
                "    "),
            4: ("  o ",
                " /|\\",
                "    "),
            5: ("  o ",
                " /|\\",
                " /  "),
            6: ("  o ",
                " /|\\",
                " / \\")}

def display_man(wrong_guesses):
    for line in hang_man[wrong_guesses]:
        print(line)

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
  print(" ".join(answer))

def main():
  answer = random.choice(words)
  hint = ["_"] * len(answer)
  print(hint)
  wrong_guesses = 0
  guessed_letters = set()
  is_running = True

  while is_running:
    display_man(wrong_guesses)
    display_hint(hint)
    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
      print("Invalid Input.")
      continue

    if guess in guessed_letters:
      print(f"{guess}is already guessed")  

    guessed_letters.add(guess)

    if guess in answer:
       for i in range(len(answer)):
          if answer[i] == guess:
            hint[i] = guess
    else:
      wrong_guesses += 1
    
    if "_" not in hint:
      display_man(wrong_guesses)
      display_answer(answer)
      print("You win!")
      is_running = False

    elif wrong_guesses >= len(hang_man) -1:
      display_man(wrong_guesses)
      display_answer(answer)
      print("You lose!")
      is_running = False

if __name__ == "__main__":
    main()


usman = open("html.txt", "r")
print(usman.read())
usman.close()


file = open("html.txt", "w")
file.write("Hello Usman\n")
file.write("Hello Irfan\n")
file.write("Hello Kamran\n")
file.close()

file = open("html.txt", "r")
print(file.read())
file.close()


file = open("html.txt", "r")
lines = file.read()

print(lines.splitlines())

class person:
  
  def __init__(self, name, age, cast):
    print("Hey I am a person")
    self.name = name
    self.age = age
    self.cast = cast
  def info(self):
    print(self.name, "is", self.age, "years old and his cast is", self.cast)
a = person("Usman", 22, "Pathan")
b = person("Irfan", 20, "Pathan")

a.info()
b.info()

class employee:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def showDetails(self):
    print(f"The name of employee is {self.name} and his age is {self.age}")  

class programmer(employee):
  def showLanguage(self):
    print("The default langugae is python")

a1 = employee("Ali", 21)
a1.showDetails()
a2 = programmer("Ahmed", 22)
a2.showDetails()
a2.showLanguage()



def bubble_sort(arr, ascending=True):
    n = len(arr)
    comparisons = 0
    swaps = 0
    for i in range(n):
        for j in range(0, n - i - 1):
            comparisons += 1
            if (ascending and arr[j] > arr[j + 1]) or (not ascending and arr[j] < arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
    return arr, comparisons, swaps

def selection_sort(arr, ascending=True):
    n = len(arr)
    comparisons = 0
    swaps = 0
    for i in range(n):
        idx = i
        for j in range(i + 1, n):
            comparisons += 1
            if (ascending and arr[j] < arr[idx]) or (not ascending and arr[j] > arr[idx]):
                idx = j
        if idx != i:
            arr[i], arr[idx] = arr[idx], arr[i]
            swaps += 1
    return arr, comparisons, swaps

arr = list(map(int, input("Enter integers separated by spaces: ").split()))
order = input("Enter 'asc' for ascending or 'desc' for descending order: ").lower()
algorithm = input("Enter 'bubble' for bubble or 'selection' for selection sort: ").lower()

ascending = order == 'asc'

if algorithm == 'bubble':
    sorted_arr, comparisons, swaps = bubble_sort(arr, ascending)
elif algorithm == 'selection':
    sorted_arr, comparisons, swaps = selection_sort(arr, ascending)
else:
    print("Invalid sorting algorithm choice.")
    exit()

print(f"\nSorted list: {sorted_arr}")
print(f"Number of comparisons: {comparisons}")
print(f"Number of swaps: {swaps}")


import json

# Initialize the inventory as an empty dictionary
inventory = {}

# Function to add a new product
def add_product():
    name = input("Enter product name: ")
    price = float(input("Enter price: "))
    category = input("Enter category: ")
    quantity = int(input("Enter quantity: "))
    inventory[name] = {'price': price, 'category': category, 'quantity': quantity}
    print(f"Product '{name}' added.")

# Function to update an existing product
def update_product():
    name = input("Enter product name to update: ")
    if name in inventory:
        print(f"Current details: {inventory[name]}")
        inventory[name]['price'] = float(input("Enter new price: "))
        inventory[name]['quantity'] = int(input("Enter new quantity: "))
        print(f"Product '{name}' updated.")
    else:
        print("Product not found.")

# Function to delete a product
def delete_product():
    name = input("Enter product name to delete: ")
    if name in inventory:
        del inventory[name]
        print(f"Product '{name}' deleted.")
    else:
        print("Product not found.")

# Function to view all products
def view_products():
    sorted_inventory = dict(sorted(inventory.items()))
    for name, details in sorted_inventory.items():
        print(f"Name: {name}, Price: {details['price']}, Category: {details['category']}, Quantity: {details['quantity']}")

# Function to search products by category
def search_by_category():
    category = input("Enter category to search: ")
    for name, details in inventory.items():
        if details['category'].lower() == category.lower():
            print(f"Name: {name}, Price: {details['price']}, Quantity: {details['quantity']}")

# Function to search products by price range
def search_by_price_range():
    min_price = float(input("Enter minimum price: "))
    max_price = float(input("Enter maximum price: "))
    for name, details in inventory.items():
        if min_price <= details['price'] <= max_price:
            print(f"Name: {name}, Price: {details['price']}, Category: {details['category']}, Quantity: {details['quantity']}")

# Function to save inventory to a file
def save_inventory():
    with open("inventory.txt", "w") as file:
        for name, details in inventory.items():
            file.write(f"{name},{details['price']},{details['category']},{details['quantity']}\n")
    print("Inventory saved to inventory.txt")

# Function to load inventory from a file
def load_inventory():
    try:
        with open("inventory.txt", "r") as file:
            for line in file:
                name, price, category, quantity = line.strip().split(',')
                inventory[name] = {'price': float(price), 'category': category, 'quantity': int(quantity)}
        print("Inventory loaded from inventory.txt")
    except FileNotFoundError:
        print("No saved inventory file found.")

# Main menu
while True:
    print("\nInventory Management System")
    print("1. Add Product")
    print("2. Update Product")
    print("3. Delete Product")
    print("4. View All Products")
    print("5. Search by Category")
    print("6. Search by Price Range")
    print("7. Save Inventory to File")
    print("8. Load Inventory from File")
    print("9. Exit")

    choice = input("Enter your choice: ")
    
    if choice == '1':
        add_product()
    elif choice == '2':
        update_product()
    elif choice == '3':
        delete_product()
    elif choice == '4':
        view_products()
    elif choice == '5':
        search_by_category()
    elif choice == '6':
        search_by_price_range()
    elif choice == '7':
        save_inventory()
    elif choice == '8':
        load_inventory()
    elif choice == '9':
        print("Exiting the Inventory Management System.")
        break
    else:
        print("Invalid choice. Please try again.")