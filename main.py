
'''
Asks users how much money they want to deposit into their balance
Continues in a while loop until user enters a positive number
'''
def deposit():
    isValidAmount = False

    while not isValidAmount:
        amount = input("How much would you like to deposit? $")
        #checks if amount is a number
        if not amount.isdigit():
            print("Please enter a number \n")
            continue
        amount = int(amount)
        if amount <= 0:
            print("Amount must be greater than 0 \n")
        isValidAmount = True
    return amount

deposit()