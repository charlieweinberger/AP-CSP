lovely_loveseat_description = "A red, two person loveseat"
lovely_armchair_description = "A confortable blue, one person armchair"
lovely_table_description = "A nice round four person table"

lovely_loveseat_price = 200
lovely_armchair_price = 150
lovely_table_price = 300

sales_tax = 0.0825

customer_itemization = ""
customer_total = 0

continueBuying = True

while continueBuying:
    
    cart = input("Would you like to buy a loveseat, an armchair, or a table? ")
    
    if cart == "loveseat":
        customer_itemization += lovely_loveseat_description
        customer_total += lovely_loveseat_price + lovely_loveseat_price * sales_tax
    elif cart == "armchair":
        customer_itemization += lovely_armchair_description
        customer_total += lovely_armchair_price + lovely_armchair_price * sales_tax
    elif cart == "table":
        customer_itemization += lovely_table_description
        customer_total += lovely_table_price + lovely_table_price * sales_tax
    
    ask = input("Would you like to buy anything else? ")

    if ask == "yes":
        customer_itemization += ", "
    else:
        continueBuying = False

print(f"Your items: {customer_itemization}")
print(f"Total cost: {customer_total}")