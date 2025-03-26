def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.

    Argumentss:
        price: The original price of the item.
        discount_percent: The discount percentage.

    Returns:
        The final price after applying the discount, or the original price if no discount is applied.
    """
    if discount_percent >= 20:
        final_price = price - ((discount_percent/100) * price)
        return print("Final price:", final_price)
    else: 
       return print("Original price:", price)
final_price = calculate_discount(price= float(input("Price: ")), discount_percent= float(input("Discount: ")))
    #Uses the calculate_discount function, to prompt the user to enter the original price of an item and the discount percentage, then prints the final price after applying the discount, or if no discount was applied, prints the original price.
