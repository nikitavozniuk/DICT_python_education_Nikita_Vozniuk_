i_number_of_coins = "Please, enter the number of mycoins you have: "
i_exchange_rate = "Please, enter the exchange rate: "
i_total_amount = "The total amount of dollars: "

coins = float(input(i_number_of_coins))
rate = float(input(i_exchange_rate))

print(f"{i_total_amount} {coins * rate}")
