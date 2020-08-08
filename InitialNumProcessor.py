income = int(input())
if income in range(0, 15528):
    percent = 0
    tax = float(income * 0/100)
    print(f'The tax for {income} is {percent}%. That is {tax:.0f} dollars!')
elif income in range(15528, 42708):
    percent = 15
    tax = float(income * 15/100)
    print(f'The tax for {income} is {percent}%. That is {tax:.0f} dollars!')
elif income in range(42708, 132407):
    percent = 25
    tax = float(income * 25/100)
    print(f'The tax for {income} is {percent}%. That is {tax:.0f} dollars!')
else:
    percent = 28
    tax = (income * 28/100)
    print(f'The tax for {income} is {percent}%. That is {tax:.0f} dollars!')

"{1} {1} {1}".format(1, 2, 3)