# Food Expense Tracker
daily_info = (300.0, "2025-07-13")
budget, date = daily_info
food_items = []
meal_times = set()
print(f" Date: {date} | Budget: ₹{budget}")
print("Enter food items (type 'done' to stop):")

while True:
    name = input("Food Name: ")
    if name.lower() == "done":
        break

    meal = input("Meal Time (Breakfast/Lunch/Dinner): ")
    meal_times.add(meal)

    qty = int(input("Quantity: "))
    cost = float(input("Total Cost: ₹"))
    food = {"name": name, "meal": meal, "qty": qty, "cost": cost}
    food_items.append(food)
    total = sum(f["cost"] for f in food_items)
over_budget = total > budget
print("\n Food Summary:")
for f in food_items:
    print(f"{f['name']} ({f['meal']}) x{f['qty']} - ₹{f['cost']}")


    print(f"\n Total Spent: ₹{total}")
print(f" Over Budget: {over_budget}")
print(f" Meals Today: {meal_times}")




#Date: 2025-07-13 | Budget: ₹300.0
#Enter food items (type 'done' to stop):
#Food Name: Idli
#Meal Time (Breakfast/Lunch/Dinner): Breakfast
#Quantity: 2
#Total Cost: ₹50
#Food Name: Biryani
#Meal Time (Breakfast/Lunch/Dinner): Lunch
#Quantity: 1
#Total Cost: ₹160
#Food Name: Ice Cream
#Meal Time (Breakfast/Lunch/Dinner): Dinner
#Quantity: 1
#Total Cost: ₹90
#Food Name: done

 #Food Summary:
#Idli (Breakfast) x2 - ₹50.0

 #Total Spent: ₹300.0
#Biryani (Lunch) x1 - ₹160.0

 #Total Spent: ₹300.0
#Ice Cream (Dinner) x1 - ₹90.0

 #Total Spent: ₹300.0
 #Over Budget: False
 # Meals Today: {'Breakfast', 'Lunch', 'Dinner'}
