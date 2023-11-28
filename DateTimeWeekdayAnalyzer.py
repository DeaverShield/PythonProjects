#
# Aaron Deaver
# November 12, 2023
# Program that gathers the current date and time, and shows the week day that a date took place


from datetime import datetime
def main():
    # Get the current date and time
    current_date = datetime.now()

    print("The current date/time is:")

    print(current_date.strftime('%m/%d/%y %I:%M:%S %p'))
    print(current_date.strftime('%a, %b %d, %Y'))
    print(current_date.strftime('%A, %B %d, %Y'))

    input_info = input('Enter a date (e.g. mm-dd-yyyy): ')

    try:
        date_entered = datetime.strptime(input_info, '%m-%d-%Y')

        week_day = date_entered.strftime('%A')

        print('That date was on a {0}.'.format(week_day))
    except ValueError:
        print("Date in the wrong format.")

main()
