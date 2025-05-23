def calculate_discount(price, quantity):
    # d(price, 1) - Definition of price (function parameter)
    # d(quantity, 1) - Definition of quantity (function parameter)

    # Line 2: Computation of total
    total = price * quantity
    # d(total, 2) - Definition of total
    # c-use(price, 2) - Computation-use of price
    # c-use(quantity, 2) - Computation-use of quantity

    # Line 3: Initial definition of discount_rate
    discount_rate = 0.0
    # d(discount_rate, 3) - Definition of discount_rate

    # Line 5: Predicate-use of total in the if condition
    if total > 100:
        # p-use(total, 5) - Predicate-use of total

        # Line 6: Redefinition of discount_rate
        discount_rate = 0.1
        # d(discount_rate, 6) - Definition of discount_rate
    # Line 7: Predicate-use of total in the elif condition
    elif total > 50:
        # p-use(total, 7) - Predicate-use of total

        # Line 8: Redefinition of discount_rate
        discount_rate = 0.05
        # d(discount_rate, 8) - Definition of discount_rate

    # Line 10: Computation of final_price
    final_price = total * (1 - discount_rate)
    # d(final_price, 10) - Definition of final_price
    # c-use(total, 10) - Computation-use of total
    # c-use(discount_rate, 10) - Computation-use of discount_rate

    # Line 11: Computation-use of final_price in the return statement
    return final_price
    # c-use(final_price, 11) - Computation-use of final_price
