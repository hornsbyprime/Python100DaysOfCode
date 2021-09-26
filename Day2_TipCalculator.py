print("Welcome to the tip calculator.")
bill = float(input('What is the total of the bill?\n'))
tip = int(input('What percentage do you want to tip?\n'))
split = int(input('How many people are there?\n'))
total = tip / 100 * bill + bill
share = total / split
share = '{:.2f}'.format(share)
print(f'Everyone owes ${share}')