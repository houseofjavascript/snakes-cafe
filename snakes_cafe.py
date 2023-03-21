from textwrap import dedent

food = {
    "Wings": 0,
    "Cookies": 0,
    "Spring Rolls": 0,
    "Salmon": 0,
    "Steak": 0,
    "Meat Tornado": 0,
    "A Literal Garden": 0,
    "Ice Cream": 0,
    "Cake": 0,
    "Pie": 0,
    "Coffee": 0,
    "Tea": 0,
    "Unicorn Tears": 0,
}
order = {}


greeting = dedent(
    """
    **************************************
    **    Welcome to the Snakes Cafe!   **
    **    Please see our menu below.    **
    **
    ** To quit at any time, type "quit" **
    **************************************
    """
)


menu = dedent(
    """
    Appetizers
    ----------
    Wings
    Cookies
    Spring Rolls

    Entrees
    -------
    Salmon
    Steak
    Meat Tornado
    A Literal Garden

    Desserts
    --------
    Ice Cream
    Cake
    Pie

    Drinks
    ------
    Coffee
    Tea
    Unicorn Tears
    """
)

order_prompt = dedent(
    """
    ***********************************
    ** Hi! What would you like to order? **
    ***********************************
    """
)

farewell = dedent(
    """
    ***********************************
    **    Thanks for stopping by! Please return soon   **
    ***********************************
    """
)


def main():
    print(greeting)
    print(menu)

    while True:
        item = input("What would you like to order? (Enter 'quit' to exit)").lower()
        if item == "quit":
            break
        elif item in food:
            if item in order:
                order[item] += 1
            else:
                order[item] = 1
            print(f"You have ordered {order[item]} {item}(s).")
        else:
            print("Sorry, that item is not on the menu.")


print("Thank you for coming. Your complete order is:")
if order:
    for item, quantity in order.items():
        print(f"{quantity} {item}(s) - ${menu[item]*quantity}")
    print(f"Total cost: ${sum([menu[item]*quantity for item, quantity in order.items()])}")
else:
    print("No items were ordered. Thank you for stopping by.")


if __name__ == "__main__":
    main()