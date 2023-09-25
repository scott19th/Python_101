#Python Challenge 101 - Shopping Cart Organiser

products = [
    {"name": "Laptop", "price": 999.99},
    {"name": "Headphones", "price": 49.99},
    {"name": "Smartphone", "price": 599.99}
]

cust1_cart = [{"product" : "Laptop", "quantity": 1}, {"product" : "Headphones", "quantity": 2}]
cust2_cart = [{"product" : "Smartphone", "quantity": 1}]

def merge_cart_product_info(cart, products):
    merged_cart = list()
    for item in cart:
        for product in products:
            if item["product"] == product["name"]:
                item["price"] = product["price"]*item["quantity"]
                merged_cart.append(item)          
    return merged_cart

def total_cart_price(merged_cart):
    total_price = 0
    for product in merged_cart:
        total_price = total_price + product["price"]
    if total_price >= 1000:
        total_price = total_price * 0.9
    total_price = round(total_price, 2)
    print(merged_cart)
    print(total_price)

merge_cart_product_info(cust1_cart, products)
total_cart_price(merged_cart= merge_cart_product_info(cust1_cart, products))


merge_cart_product_info(cust2_cart, products)
total_cart_price(merged_cart= merge_cart_product_info(cust2_cart, products))