loan = 1000
months = [250, 250, 500]

print('Loan principal: {}'.format(loan))

for index, value in enumerate(months):
    print('Month {}: repaid {}'.format(index+1, value))

print('The loan has been repaid!')
