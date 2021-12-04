import math

choice_text = '''What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal:
'''


def year_payment(li, p, loan):
    i = (li * 0.01 / 12)
    num = pow(1 + i, p)

    return loan * ((i * num) / (num - 1))


def loan_sum(li, ann, p):
    i = (li * 0.01 / 12)
    num = pow(1 + i, p)

    return ann / ((i * num) / (num - 1))


def payment_count(li, mp, loan):
    i = (li * 0.01 / 12)
    A = (mp / (mp - i * loan))

    return math.ceil(math.log(A, i + 1))


def n():
    loan = int(input('Enter the loan principal: '))
    monthly_payment = int(input('Enter the monthly payment: '))
    loan_interest = int(input('Enter the loan interest: '))

    n = payment_count(loan_interest, monthly_payment, loan)

    years = n / 12
    month = (years - math.floor(years)) * 12
    print('It will take {} years and {} months to repay this loan!'.format(math.floor(years), math.floor(month)))


def a():
    loan = int(input('Enter the loan principal: '))
    periods = int(input('Enter the number of periods: '))
    loan_interest = int(input('Enter the loan interest: '))

    payment = math.ceil(year_payment(loan_interest, periods, loan))

    print('Your monthly payment = {}!'.format(payment))


def p():
    annuity_payment = float(input('Enter the annuity payment: '))
    periods = int(input('Enter the number of periods: '))
    loan_interest = float(input('Enter the loan interest: '))

    loan_principal = math.floor(loan_sum(loan_interest, annuity_payment, periods))

    print('Your loan principal = {}!'.format(loan_principal))


def CreditCalculator():
    choice = input(choice_text)

    if choice == 'n':
        n()
    elif choice == 'a':
        a()
    elif choice == 'p':
        p()


CreditCalculator()
