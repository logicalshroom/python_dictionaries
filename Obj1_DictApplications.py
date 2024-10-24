restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

# Add a new category caled "Beverages" with two or more items

restaurant_menu["Beverages"] = {"Mimosa": 3.99, "Blue Drank": 2.99}

print(restaurant_menu)

# Update the price of Steak to 17.99

restaurant_menu["Main Course"] = {"Steak": 17.99}

print(restaurant_menu)

# Remove Bruschetta from Starters

delvalue = restaurant_menu["Starters"].pop("Bruschetta")

print(restaurant_menu)