# Markhus Dammar
# 3/25/2020
# This is the program for Assignment 8, stock market

from SQ import Stack, Queue
import time

shares_lifo = Stack()
price_lifo = Stack()
shares_fifo = Queue()
price_fifo = Queue()

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

while operation > 2 or operation < 1:                        # loop for if the user tries to enter an invalid character
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

if operation == 2:
    print("Okay, you wanna use FIFO. Let's do it.")

time.sleep(1)

while operation == 1:                                        # 1 LIFO, so we'll use the Stack class.
    time.sleep(0.3)
    print("""
    ---LIFO---
    1.) Buy Stocks
    2.) Sell Stocks
    3.) EXIT 
    """)
    print("\nINPUT 1, 2, or 3")
    choice = int(input("What would you like to do? >>> "))

    if choice > 3 or choice < 1:
        print("INVALID, try again.")
        time.sleep(1)

    if choice == 1:
        shares_lifo_input = int(input("How many shares would you like to buy? >>>"))
        shares_lifo.push(shares_lifo_input)                 # Pushes the amount purchased
        price_lifo_input = int(input("How much does each share cost? >>>$"))
        price_lifo.push(price_lifo_input)                   # Pushes the price
        print(f"{shares_lifo_input} will be purchased at ${price_lifo_input} per share")
        time.sleep(1)
        print('RETURNING TO MENU...')
        time.sleep(1)

    if choice == 2:
        shares_selling = int(input("How many shares do you want to sell? >>>"))
        shares_lifo.pop(shares_selling)
        print(f"You're selling {shares_selling} shares,")
        sold = int(input("How much $ per share are you selling at? >>>$"))
        profit = (sold - price_lifo_input) * shares_lifo_input
        if profit < price_lifo_input:
            print("You actually lost money!")
        price_lifo.pop((price_lifo_input))
        print(f"You sold {shares_selling} shares at {sold} per share, equating to a ${profit} profit.")
        time.sleep(1)
        print('RETURNING TO MENU...')
        time.sleep(1)

    if choice == 3:
        print("EXITING MENU")
        time.sleep(1)
        exit()


while operation == 2:                                        # 2 FIFO, so we'll use the Queue class.
    time.sleep(0.3)
    print("""
    ---FIFO---
    1.) Buy Stocks
    2.) Sell Stocks
    3.) EXIT 
    """)
    print("\nINPUT 1, 2, or 3")
    choice = int(input("What would you like to do? >>> "))

    if choice > 3 or choice < 1:
        print("INVALID, try again.")
        time.sleep(1)

    if choice == 1:
        shares_fifo_input = int(input("How many shares would you like to buy? >>>"))
        shares_fifo.push(shares_fifo_input)                 # Pushes the amount purchased
        price_fifo_input = int(input("How much does each share cost? >>>$"))
        price_fifo.push(price_fifo_input)                   # Pushes the price
        print(f"{shares_fifo_input} will be purchased at ${price_fifo_input} per share")
        time.sleep(1)
        print('RETURNING TO MENU...')
        time.sleep(1)

    if choice == 2:
        shares_selling = int(input("How many shares do you want to sell? >>>"))
        shares_fifo.pop(shares_selling)
        print(f"You're selling {shares_selling} shares,")
        sold = int(input("How much $ per share are you selling at? >>>$"))
        profit = (sold - price_fifo_input) * shares_fifo_input
        if profit < price_fifo_input:
            print("You actually lost money!")
        price_fifo.pop((price_fifo_input))
        print(f"You sold {shares_selling} shares at {sold} per share, equating to a ${profit} profit.")
        time.sleep(1)
        print('RETURNING TO MENU...')
        time.sleep(1)

    if choice == 3:
        print("EXITING MENU")
        time.sleep(1)
        exit()
