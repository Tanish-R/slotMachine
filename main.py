MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

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
            print("Please enter an appropriate number \n")
            continue

        amount = int(amount)

        if amount <= 0:
            print("Amount must be greater than $0 \n")
        else:
            isValidAmount = True
    return amount


'''
Asks users how many lines they would like to bet on
Continues in a while loop until user enters a number in the given range
'''
def get_number_of_lines():
    isValidLines = False

    while not isValidLines:
        lines = input(f"Enter the number of lines to bet on (1-{MAX_LINES}): ")

        if not lines.isdigit():
            print("Please enter an appropriate number \n")
            continue

        lines = int(lines)

        if lines < 1 or lines > MAX_LINES:
            print(f"Number of lines must be between 1 and {MAX_LINES} \n")
        else:
            isValidLines = True
    return lines


'''
Asks users how much they want to bet
Continues in a while loop until user enters a number in the given betting range
'''
def get_bet():
    isValidBet = False

    while not isValidBet:
        print(f"\nValid bets are between ${MIN_BET} and ${MAX_BET} per line.")
        bet = input(f"How much would you like to bet on each line? $")

        if not bet.isdigit():
            print("Please enter an appropriate number \n")
            continue

        bet = int(bet)

        if bet < MIN_BET or bet > MAX_BET:
            print(f"Bets must be between ${MIN_BET} - ${MAX_BET}\n")
        else:
            isValidBet = True
    return bet

def main():
    balance = deposit()
    lines = get_number_of_lines()
    bet = get_bet()
    totalBet = lines * bet
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to ${totalBet}")


main()