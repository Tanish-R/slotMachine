import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3 
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


'''
Populates the slot machines with data (symbols).
Uses nested for loop to randomly choose which symbols will come. Each nested list in columns is one column in our slots. Not to be confused as a row.
'''
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []

    #.items - get all key-value pairs in dictionary
    #populating all_symbols with each corresponding number of symbols (2 A's, 4 B's, etc.)
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    #storing values that go in each column of slot. Each nested list represents 1 column, not row
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns


#Printing out a transposed version of columns
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end = " | ")
            else:
                print(column[row], end = "")
        
        print()


'''
Iterate through each line (row) and check the first column of that row to see what symbol to look for.
We then see if all the remaining columns have the same symbol. If all the columns have the same symbol, user wins their bet on that line. Their bet is multiplied by the value of the symbol. 
If the symbols are not the same, we break out of the loop and check the next line.
'''
def check_winnings(columns, lines, bet, values):
    winnings = 0
    winningLines = []
    for line in range(lines):
        #gets the symbol in first column of the line we are checking
        symbol = columns[0][line]
        for column in columns:
            symbolToCheck = column[line]
            if symbol != symbolToCheck:
                break
        else:
            winnings += values[symbol] * bet
            winningLines.append(line + 1)

    return winnings, winningLines


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

'''
Primary function that calls all other functions. Gets user input and outputs winnings of each spin.
Returns the profit of each spin (winnings - bet)
'''
def playGame(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        totalBet = lines * bet

        if totalBet > balance:
            print(f"You don't have enough to bet that amount. Your current balance is ${balance}")
        else:
            break

    print(f"\nYou are betting ${bet} on {lines} lines. Total bet is equal to ${totalBet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winningLines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    if winnings > 0:
        # * unpacks the list
        print(f"You won on lines:", *winningLines)
    return winnings - totalBet


#Allows users to play the game multiple times.
def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        spin = input("\nPress enter to play (q to quit) ")
        if spin == "q":
            break
        balance += playGame(balance)
    
    print(f"You left with ${balance}")
 
main()