# Python Challenge 101 - Sales Revenue Calculation

# Challenge : Calculate total revenue generated from the sales report

Sales_report = [
    {"poduct": "Hammer", "Price": 10.99, "Quantity": 47},
    {"poduct": "Saw", "Price": 5.49, "Quantity": 112},
    {"poduct": "Nails 100x", "Price": 6.15, "Quantity": 232},
    {"poduct": "Soft Drinks", "Price": 1.15, "Quantity": 120},
    {"poduct": "Mars Bar", "Price": 0.75, "Quantity": 150}
]


def total_sales_calculator(sales):
    total_sales = 0
    for item in sales:
        total_sales = total_sales + (item["Price"] * item["Quantity"])
    print(total_sales)


total_sales_calculator(Sales_report)
