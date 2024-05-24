def calculate_discount(original_price, discount_percent):
    if discount_percent >= 20:
        final_price = original_price-(original_price*(discount_percent/100))
        return final_price
    else:
        return price
    try:
        original_price = float(input("Enter original price:"))
        discount_percent = float(input("Enter discount percentage:"))

        final_price = calculate_discount(original_price, discount_percentage)

        if discount_percentage >= 20:
            print(f"The final price after applying the discount is:${final_price:.2f}")
        else:
            print(f"No discount applied. The original price is:${original_price:.2f}")
    except ValueError:
            print("Invalid input. Input the valid values.")
