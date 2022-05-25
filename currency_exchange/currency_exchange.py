import json
import requests

currencies = ["USD", "EUR"]
currency = input()

try:
    response = requests.get(f"http://www.floatrates.com/daily/{currency}.json")
    parsed = json.loads(response.content)

    usd = round(parsed["usd"]["rate"], 2)
    eur = round(parsed["eur"]["rate"], 2)
    print(f"USD: {usd}")
    print(f"EUR: {eur}")
except requests.exceptions.RequestException as e:
    raise SystemExit(e)
