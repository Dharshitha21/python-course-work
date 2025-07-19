222# Task 1: Take Meal Details as Input
meal_id = int(input("Enter Meal ID: "))
meal_name = input("Enter Meal Name: ")
price = float(input("Enter Price (in ₹): "))
ingredients = input("Enter Ingredients (comma-separated): ").split(',')
nutrition_facts = tuple(map(float, input("Enter Nutrition Facts (Calories, Protein in grams): ").split(',')))
discount_percentage = float(input("Enter Discount Percentage: "))
meal_features = set(input("Enter Meal Features (comma-separated): ").split(','))
supplier = {
    "name": input("Enter Supplier Name: "),
    "contact": input("Enter Supplier Contact Number: "),
    "location": input("Enter Supplier Location: ")
}

# Task 2: Display Meal Details Using Different Formatting Methods

# 1. Using Comma Separation (sep=',')
print("\n--- Meal Summary (Comma Separation) ---")
print("Meal ID, Name, Price:", meal_id, meal_name, price, sep=',')

# 2. Using Percentage Formatting (% operator)
print("\n--- Discount Info (Percentage Formatting) ---")
print("Meal Discount: %.2f%%" % discount_percentage)

# 3. Using f-strings (f"")
print("\n--- Meal Details (f-strings) ---")
print(f"Meal Name: {meal_name}")
print(f"Price: ₹{price}")
print(f"Calories: {nutrition_facts[0]} kcal")
print(f"Protein: {nutrition_facts[1]}g")
print(f"Discount: {discount_percentage}%")

# 4. Using .format() method
print("\n--- Supplier Details (.format method) ---")
print("Supplier Details: Name - {name}, Contact - {contact}, Location - {location}".format(**supplier))

# Additional outputs for completeness
print("\n--- Ingredients List ---")
print(", ".join(ingredient.strip() for ingredient in ingredients))

print("\n--- Unique Meal Features ---")
print(", ".join(feature.strip() for feature in meal_features))
