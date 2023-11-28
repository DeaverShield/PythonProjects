#
# Aaron Deaver


# Aaron's Athletic store Inventory System - Using pickle module

import pickle

CATEGORY_LIST = ['Footwear', 'Apparel', 'Equipment']
# Footwear example: Running shoes, Basketball Shoes, Soccer Cleats, Training Shoes, Hiking Boots
# Apparel example: Running Apparel, Yoga Pants, Athletic Jackets, Basketball Jerseys, Compression Gear
# Equipment example: Dumbbells, Tennis Rackets, Soccer Balls, Basketball Hoops, Baseball Bats



def main():
    inventory_counts, inventory_costs, inventory_categories = read_inventory_file()

    print("Welcome to Aaron's Inventory Input System")
    print("Current Inventory:")
    display_all_inventory(inventory_counts, inventory_costs, inventory_categories)

    response = ''
    while response != '0':
        display_menu()
        response = input('Enter your choice: ')

        if response == "1":  # Add an item
            item_name, item_count, unit_cost, category = get_item_input()
            if item_name not in inventory_counts:
                inventory_counts[item_name] = item_count
                inventory_costs[item_name] = unit_cost
                inventory_categories[item_name] = category
                print(f'{item_name} added to inventory.')
            else:
                print(f'{item_name} already exists.')

        elif response == "2":  # Display a single item
            item_name = input('Enter item name: ')
            if item_name in inventory_counts:
                print(f'Item: {item_name}')
                print(f'Count: {inventory_counts[item_name]}')
                print(f'Cost: {inventory_costs[item_name]:.2f}')
                print(f'Category: {inventory_categories[item_name]}')
            else:
                print("Not found")

        elif response == "3":  # Display items in a category
            category_name = input('Enter category name: ')
            print(f'\nItems in {category_name}:')
            if category_name in CATEGORY_LIST:
                category_items = [item_name for item_name, item_category in inventory_categories.items() if item_category == category_name]
                if category_items:
                    for item_name in category_items:
                        print(item_name)
                else:
                    print(f'No items found in the category: {category_name}')
            else:
                print(f'{category_name} not in the list of categories: {CATEGORY_LIST}')

        elif response == "4":  # Delete a single item
            item_name = input('Enter item name: ')
            if item_name in inventory_counts:
                del inventory_counts[item_name]
                del inventory_costs[item_name]
                del inventory_categories[item_name]
                print(f'{item_name} deleted from inventory')
            else:
                print("Not found")

        elif response == "5":  # Display all inventory
            display_all_inventory(inventory_counts, inventory_costs, inventory_categories)
        elif response != "0":
            print("Invalid choice. Try again.\n")

    print("Final Inventory:") # Ready to exit the program, display and save inventory as last steps
    if not inventory_counts:
        print("== Empty ==")
    else:
        print("\nFinal Inventory:")
        print(f"{'Item name':<15} {'Count':<7} {'Unit Cost':<10} {'Category':<20}")
        print(f"{'-' * 15} {'-' * 7} {'-' * 10} {'-' * 20}")

        for item_name in inventory_counts:
            count = inventory_counts[item_name]
            cost = inventory_costs[item_name]
            category = inventory_categories[item_name]

            # Use f-string formatting to achieve the specified alignment
            print(f"{item_name:<15} {count:>7} {cost:.2f} {category:<20}")
    print("\nInventory saved to inventory.dat.")

def display_menu():
    print("What would you like to do?")
    print("(1) Add an item\n"
          "(2) Display an item\n"
          "(3) Display a category\n"
          "(4) Delete an item\n"
          "(5) Display all inventory\n"
          "(0) Exit")

def display_all_inventory(inventory_counts, inventory_costs, inventory_categories):
    if not inventory_counts:
        print("== Empty ==")
    else:
        for item_name in inventory_counts:
            print(f'Item: {item_name}')
            print(f'Count: {inventory_counts[item_name]}')
            print(f'Cost: {inventory_costs[item_name]:.2f}')
            print(f'Category: {inventory_categories[item_name]}')
            print()

def save_inventory_file(inventory_counts, inventory_costs, inventory_categories):
    with open('inventory.dat', 'wb') as file:
        pickle.dump((inventory_counts, inventory_costs, inventory_categories), file)

def read_inventory_file():
    try:
        with open('inventory.dat', 'rb') as file:
            inventory_counts, inventory_costs, inventory_categories = pickle.load(file)
    except FileNotFoundError:
        inventory_counts = {}
        inventory_costs = {}
        inventory_categories = {}
    return inventory_counts, inventory_costs, inventory_categories


# This function is complete, no changes needed, but feel free to review
def get_item_input():
    # Get item name
    item_name = input('Enter the item name: ')
    # Get item count
    while True:
        try:
            item_count = int(input('Enter the item count: '))
            if item_count < 0:
                print('Item count must be 0 or greater.')
            else:
                break
        except ValueError:
            print('Item count must be an integer.')
    # Get unit cost
    while True:
        try:
            unit_cost = float(input('Enter the unit cost: '))
            if unit_cost < 0:
                print('Unit cost must be 0 or greater.')
            else:
                break
        except ValueError:
            print('Unit cost must be an integer.')
    # Get category
    while True:
        category = input('Enter the category: ')
        if category not in CATEGORY_LIST:
            print(f'Category must be in this list: {CATEGORY_LIST}')
        else:
            break
    return item_name, item_count, unit_cost, category


main()
