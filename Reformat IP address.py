# Aaron Deaver
# October 8, 2023
# Reformat IP address program


def main():
    while True:
        # Ask the user to input an IP address or 'Q' to quit

        iploop = input(f'Please enter an IP address or \'Q\' to quit: ')
        # while the user has not entered 'Q' or 'q' to quit

        if iploop == 'Q' or iploop == 'q':
            return

    #  split the user input at each period and store the parts in a list

        sections = iploop.split('.')
        # if there are not 4 parts in the list
        if len(sections) != 4:
            # display an error message
            print(f'Error: An IP address should consist of 4 parts separated by periods.')
        # else
        else:
            # set error flag to False
            error_message = False

            # for each part in the list
            for num in sections:
                # if the part is not a number or if it is not between 0 and 255
                if not num.isdigit() or not (0 <= int(num) <= 255):
                    # display an error message
                    print(f'Error with {num}: Each part of the IP address should be a number between 0 and 255.')
                    # set error flag to True
                    error_message = True
                    # break the loop
                    break
                    # if no error has been displayed (i.e., error flag is False)
            if not error_message:
                     # replace each period in the user input with a colon
                    reformatted = ":".join(sections)
                    # display the new formatted IP address
                    print(f'Reformatted IP address: {reformatted}')

# ask the user to input an IP address or 'Q' to quit




main()
