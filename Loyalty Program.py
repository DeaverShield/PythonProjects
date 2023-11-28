#
# Aaron Deaver

# Gift card loyalty program
#


# Classification for the amount purchased
action = ''

spending = float(input(f"Enter the total purchase amount: "))
loyalty = input(f'Is the customer a loyalty program member (y/n): ')

tax = (0.065 * spending)
total_wtax = (spending + tax)

print(f'Sales tax: ${tax :,.2f}')
print(f'Total after tax: ${total_wtax :,.2f}')

if not loyalty == 'y' and loyalty != 'n':
    action = 'Not elgible for gift card'


# Determine gift card eligibility as member spending $50-100
else:
    if loyalty == 'y' and spending >= 50 or spending <= 100:
        action = 'Gift card awarded: $15'

    if loyalty == 'y' and spending >= 101:
        action = 'Gift card awarded: $25'

    if loyalty == 'n' and spending >= 100:
        action = 'Gift card awarded: $5'
    if loyalty == 'y' and spending <= 49:
        action = 'Gift card awarded: $0'
    else:
        if loyalty == 'n' and spending < 100:
            action = 'Gift card awarded: $0'

    print(action)
