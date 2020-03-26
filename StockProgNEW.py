# Markhus Dammar
# 3/26/2020
# This is Assignment 8, but with an attempt to not use repeat code.

from SQ import Stack, Queue
import time
                                                                                # start
print("Hello, I'm going to help you keep track of your stocks")
time.sleep(2)

print("Before we begin, I need to ask how you will operate.")
time.sleep(1)
                                                                                # Init Menu
print("""
1.) LIFO
2.) FIFO
""")
print("\nINPUT 1 OR 2")
operation = int(input("What method will you use to report your earnings? >>> "))

while operation > 2 or operation < 1:                                           # loop for if the user tries to enter an invalid character
    print("INVALID, try again.")
    time.sleep(1)
    print("""
    1.) LIFO
    2.) FIFO
    """)
    print("\nINPUT 1 OR 2")
    operation = int(input("What method will you use to report your earnings? >>> "))

if operation == 1:
    print("Okay, you wanna use LIFO. Got it.")
    shares = Stack()                                                            # Create stack list, doesn't exist in 1st prog
    price = Stack()

if operation == 2:
    print("Okay, you wanna use FIFO. Let's do it.")
    shares = Queue()
    price = Queue()

time.sleep(1)

while operation == 1 or operation == 2:                                         # 1 LIFO, so we'll use the Stack class.
    time.sleep(0.3)
    print("""
    1.) Buy Stocks
    2.) Sell Stocks
    3.) EXIT 
    """)
    print("\nINPUT 1, 2, or 3")
    choice = int(input("What would you like to do? >>> "))

    if choice > 3 or choice < 1:
        print("INVALID, try again.")
        time.sleep(1)

    if choice == 1:                                                                 # BUYING STOCK
        shares_input = int(input("How many shares would you like to buy? >>>"))
        shares.push(shares_input)                 # Pushes the amount purchased
        price_input = int(input("How much does each share cost? >>>$"))
        price.push(price_input)                   # Pushes the price
        print(f"{shares_input} will be purchased at ${price_input} per share")
        time.sleep(1)
        print('RETURNING TO MENU...')
        time.sleep(1)

    if choice == 2:                                                                # SELLING STOCK
        shares_selling = int(input("How many shares do you want to sell? >>>"))
        shares.pop(shares_selling)
        print(f"You're selling {shares_selling} shares,")
        sold = int(input("How much $ per share are you selling at? >>>$"))
        profit = (sold - price_input) * shares_input
        if profit < price_input:
            print("You actually lost money!")
        price.pop((price_input))
        print(f"You sold {shares_selling} shares at {sold} per share, equating to a ${profit} profit.")
        time.sleep(1)
        print('RETURNING TO MENU...')
        time.sleep(1)

    if choice == 3:                                                                 # EXIT
        print("EXITING MENU")
        time.sleep(1)
        exit()


