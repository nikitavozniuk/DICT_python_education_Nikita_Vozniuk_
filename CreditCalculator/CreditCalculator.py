import math
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--type', type=str)
parser.add_argument('--principal', type=int)
parser.add_argument('--payment', type=int)
parser.add_argument('--interest', type=float)
parser.add_argument('--periods', type=int)
parser.add_argument('--annuity', type=float)

arguments = parser.parse_args()


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


def diff(li, per, loan):
    i = (li * 0.01 / 12)
    mon = 0
    res = 0
    s = list(reversed(range(2, per + 2)))
    for monthly in s:
        monthly -= 1
        d = math.ceil(loan / per) + i * ((loan * monthly) / per)
        res += d
        mon += 1
        print(f"Month {mon}: payment is {math.ceil(d)}")
    print('Overpayment {}'.format(math.ceil(res - loan)))


def n(pr, pay, i):
    n = payment_count(i, pay, pr)

    years = n / 12
    month = (years - math.floor(years)) * 12
    if math.floor(month) != 0:
        print('It will take {} years and {} months to repay this loan!'.format(math.floor(years), math.ceil(month)))
    else:
        print('It will take {} years to repay this loan!'.format(math.ceil(years)))
    print('Overpayment {}'.format(int(pr * (1 + i * 0.01 / 0.75) - pr)))


def a(loan, per, i):
    payment = math.ceil(year_payment(i, per, loan))

    print('Your monthly payment = {}!'.format(payment))
    print('Overpayment {}'.format(math.ceil(payment) * per - loan))


def p(pay, per, i):
    loan_principal = math.floor(loan_sum(i, pay, per))

    print('Your loan principal = {}!'.format(loan_principal))
    print('Overpayment {}'.format((pay * per - i)))


def CreditCalculator():
    try:
        if arguments.type == 'diff':
            if arguments.interest and arguments.periods and arguments.principal:
                diff(arguments.interest, arguments.periods, arguments.principal)
        elif arguments.type == 'annuity':
            if arguments.payment and arguments.principal:
                if arguments.principal != 0 and arguments.payment != 0 and arguments.interest != 0:
                    n(arguments.principal, arguments.payment, arguments.interest)
                else:
                    print("Incorrect parameters")
            elif arguments.principal and arguments.periods:
                if arguments.principal != 0 and arguments.periods != 0 and arguments.interest != 0:
                    a(arguments.principal, arguments.periods, arguments.interest)
                else:
                    print("Incorrect parameters")
            elif arguments.payment:
                if arguments.payment != 0 and arguments.periods != 0 and arguments.interest != 0:
                    p(arguments.payment, arguments.periods, float(arguments.interest))
                else:
                    print("Incorrect parameters")
        else:
            print("Incorrect parameters")
    except TypeError:
        print("Incorrect parameters")


CreditCalculator()
