from datetime import datetime

# Aaron Deaver
current_date = datetime.now()
print(current_date)  # November 12th, 2023
# ITS Python Certification Review - Problem 1 (string format method)
#
TAX_RATE = 0.07

def main():
    title = 'I love Cyber Security'
    price = 4.50
    count = 7

    # TODO: Convert these 4 output statements so they are using f-strings
    #  instead of the string format method
    # Converted to f string
    print(f'We have {count} copies of the book.')
    # Converted to f string
    print(f'The {count} copies cost {price:.2f} each.')
    # Converted to f string
    print(f'Title: {title}\nCount: {count}\nPrice: {price:.2f}')
    # Converted to f string
    print(f'The tax on {price:.2f} is {price * TAX_RATE:.2f}.')

    print()

    # TODO: Convert these 4 output statements so they are using the string
    #  format method instead of f-strings
    # Converted to string format
    print('The title of the book is {0}.'.format(title))
    # Converted to string format
    print('"{0}" costs {1:.2f}'.format(title, price))
    # Converted to string format
    print('We have {0} copies of "{1}" in stock.'.format(count, title))
    # Converted to string format
    print('To buy all {0} copies of "{1}" will cost {2:.2f}'.format(count, title, count * price))


main()
