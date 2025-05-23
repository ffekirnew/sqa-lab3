def calculate_discount(price, quantity):
    total = price * quantity
    discount_rate = 0.0

    if total > 100:
        discount_rate = 0.1
    elif total > 50:
        discount_rate = 0.05

    final_price = total * (1 - discount_rate)
    return final_price
