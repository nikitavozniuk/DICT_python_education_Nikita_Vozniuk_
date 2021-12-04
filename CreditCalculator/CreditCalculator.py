import math

choice_text = '''
What do you want to calculate?
type "m" – for number of monthly payments,
type "p" – for the monthly payment:
'''


def CreditCalculator():
    loan = int(input('Enter the loan principal: '))
    choice = input(choice_text)

    if choice == "m":
        payment = int(input('Enter the monthly payment: '))
        months = round(loan / payment)
        print('It will take {} months to repay the loan'.format(months))
    elif choice == "p":
        month = int(input('Enter the number of months: '))
        monthly_payment = math.ceil(loan / month)
        last_payment = loan - (month - 1) * monthly_payment
        if monthly_payment != last_payment:
            print('Your monthly payment = {} and the last payment = {}'
                  .format(monthly_payment, last_payment))
        else:
            print('Your monthly payment = {}'.format(monthly_payment))


CreditCalculator()
