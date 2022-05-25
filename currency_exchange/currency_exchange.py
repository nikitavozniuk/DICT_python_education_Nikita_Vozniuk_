currencies = {
    "CAD": 1.29,
    "UAH": 29.53,
    "YEN": 126.94
}

coins = float(input())

for index, item in enumerate(currencies):
    total = round(coins * currencies[item], 2)
    print(f"I will get {total} {item} from the sale of {coins} mycoins.")
