#1 The most surprising thing about Python lists is how easily they can be modified by adding, removing, and rearranging items. I also learned that indexing and slicing make it easy to access specific information without manually searching through a list.
#2 A business situation where Python lists would save time is managing inventory for a store. Instead of manually updating an Excel spreadsheet every time products are added or removed,a Python list can organize the products and make updates easier.

#inventory.py
#Author: Ashley Parker
#Module 10 Lab

# Exercise 1

print("---Exercise 1: Build a List---")

inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))

#exercise 2:Index practice

print("---Exercise 2: Index Practice---")
print(inventory[0]) # always grabs 1st item
print(inventory[-1]) # always grabs the last item

middle = len(inventory) // 2
print(inventory[middle]) # grabs middle item(not hard coded)


print("---Exercise 3: Slicing Practice---")
print(inventory[:3]) # grabs items from start to index 2
print(inventory[-2:]) # grabs items from the second-to-last to the end
print(inventory[::2]) # grabs every other item starting from the first


print("---Exercise 4: list methods---")

inventory.append("envelope")
print(inventory)

inventory.remove("tape")
print(inventory)

inventory.sort()
print(inventory)

print("---Exercise 5: tuple comparison---")
coords = (40.7128, -74.0060) #nyc coordinates
#coords[0] = 99 #this will give error
try:
   coords[0] = 99
except TypeError as error:
    print(f"TypeError caught: {error}")
    print("Tuples protect their elements from being changed.")


print("---Exercise 6: list average sales ---")

sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total / count
print(f"Average sales: {average}")
print(f"Best sales: {max(sales)}")
print(f"Worst sales: {min(sales)}")


print("--- Exercise 7: Accumulator pattern---")
prices = [9.99, 14.99, 4.99, 24.99, 1.99]

discounted = [] # anempty list
for price in prices:
    discounted.append(round(price * 0.9, 2)) # apply 10% discount


print(prices)
print(discounted)

print("---Exercise 8: filter---")
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]

high_sales = []

for sale in sales:
    if sale > 300:
        high_sales.append(sale)

print(high_sales)
print(f"Count: {len(high_sales)}")
print(f"Average: {sum(high_sales) / len(high_sales)}")