# 1 the first bug i spotted was for sale in sales was missing ":" so it wasnt running correctly. I found it from running it and explaining it out loud. It tells me that if I know the right code I can find the erro quickly but if I didnt know that the colon had to be there I would have needed AI to help explain.
# 2 The inouts are the price and discount tier. It uses the tier t detemine how much of a discount to use. The output is the price after the discount. A colleague could understand the function by its name and inputs but adding a docstring would help.
# 3 I used AI to help me understand the bug so that I could go and fix it. AI helped build my undertsanding because i didnt have it dothe work for me, I had it help explain the problem.

# exercise 1 

# defining a fucntion
def calculate_tax(price, rate):
    return price * rate

# calling a function

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax for $100 at 7%: ${tax1:.2f}")
print(f"Tax for $250 at 8%: ${tax2:.2f}")
print(f"Tax for $350 at 5%: ${calculate_tax(350, 0.05):.2f}")

# exercise 2

#defining a function
def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85  # Apply 20% discount
    elif tier == "silver":
        return price * 0.9  # Apply 10% discount
    elif tier == "bronze":
        return price * 0.95  # Apply 5% discount
    else:
        return price  # No discount

#calling the function with different tiers
original_price = 200

for tier in ["gold", "silver", "bronze", "none"]:
    print(f"{tier}: ${apply_discount(original_price, tier):.2f}")

# exercise 3

def final_price(price, tax_rate, discount_tier):
    discounted_price = apply_discount(price, discount_tier)
    tax = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax   

#calling the final_price function
print(f"final_price(200, 0.07, 'gold'): ${final_price(200, 0.07, 'gold'):.2f}")

# exercise 4

orders = [(200, 'gold'), (150, 'silver'), (80, 'bronze'), (500, 'none')]

rate = 0.07
for price, tier in orders:
    total = final_price(price, rate, tier)
    print(f"Price ${price} | Tier {tier} | Total: ${total:.2f}")

# exercise 6

x = 100 # global x
def double_it():
    x = 999 # local x
    return x * 2

print(x)
print(double_it())
print(x)