##
# Aaron Deaver
# September 10, 2023
# Trish's Swap Shop Calculator
#
# Global Constants
BOOK_PRICE = 2.25
DVD_PRICE = 4.35
GAME_PRICE = 5.00
TAX_RATE = 0.065  # Tax Rate of 6.5%


def main():  # DO NOT CHANGE ANY CODE IN THE MAIN ROUTINE
    # NOTE: This program is NOT doing input validation to simplify the
    # program. To do input validation we would need to insert these lines
    # into while loops.
    num_books = int(input('Enter the number of books: '))
    num_dvds = int(input('Enter the number of DVDs: '))
    num_games = int(input('Enter the number of games: '))

    calc_and_display_total(num_books, num_dvds, num_games)


# Create a function called calc_and_display_total. It should take
# 3 parameters. Use the names provided here:
#    books  - Number of books
#    dvds  - Number of dvds
#    games  - Number of games
#
# It should calculate and display the total cost of each item. It should also
# calculate and display the total cost with tax.


def calc_and_display_total(num_books, num_DVDs, num_games):
    # Calculation of total book price
    books = BOOK_PRICE * num_books
    print(f'Books: ${books:.2f} ')
    # Calculation of total DVDs price
    DVDs = DVD_PRICE * num_DVDs
    print(f'DVDs: ${DVDs:.2f} ')
    # Calculation of total games price
    games = GAME_PRICE * num_games
    print(f'Games: ${games:.2f}')
    # Calculation of sub total
    sub_total = books + DVDs + games
    print(f'Subtotal: ${sub_total:.2f}')
    # Calculation of tax
    tax = TAX_RATE * sub_total
    print(f'Tax: ${tax:.2f}')
    # Calculation of total
    total = tax + sub_total
    print(f'Total: ${total:.2f}')


# Call the main function

main()
