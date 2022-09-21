hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20 ,35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0
for price in prices:
    total_price += price

average_price = total_price / len(prices)

new_prices = []
for price in prices:
    new_prices.append(price - 5)

total_revenue = 0
for i in range(len(new_prices)):
    total_revenue = new_prices[i] * last_week[i]

print(total_price)
print(average_price)
print(new_prices)
print(total_revenue)