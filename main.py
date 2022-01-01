
print('Welcome to the tip calculator!')
bill = input('What was the total bill? ')
tip = input('How much tip would you like to give? 10, 12, or 15? ')
how_many = input('How many people to split the bill? ')
tip_to_add = float(tip) / 100 * float(bill)
new_total = float(bill) + float(tip_to_add)
total_each = round(new_total / float(how_many), 2)
print(f'Each person should pay: {total_each}')
