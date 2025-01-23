product_name = input("Product name: ")
quantity = int(input("Quantity: "))
price_per_unit = float(input("Price per unit: "))

total_cost = quantity * price_per_unit

print("\nReceipt:")
print("Product: {}".format(product_name))
print("Quantity: {}".format(quantity))
print("Total Cost: ${:.2f}".format(total_cost))
