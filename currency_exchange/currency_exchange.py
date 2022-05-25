import json
import requests

class CurrencyExchange:
    currency = None
    cache = dict()
    _current = 0
    count = 0

    def __init__(self, currency) -> None:
        self.currency = currency

    def getFromApiStart(self, currency):
        try:
            response = requests.get(f"http://www.floatrates.com/daily/{currency}.json")
            parsed = json.loads(response.content)

            self.count = len(parsed)
            self.cache["eur"] = parsed["eur"]["rate"]
            self._current = self._current + 2
            if currency != "USD": 
                self._current = self._current - 1
                self.cache["usd"] = parsed["usd"]["rate"]
            
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

    def getFromApi(self, code, value):
        try:
            response = requests.get(f"http://www.floatrates.com/daily/{self.currency}.json")
            parsed = json.loads(response.content)

            self.cache[code] = parsed[code]["rate"]
            self._current = self._current + 1

            return round(parsed[code]["rate"] * value, 2)
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

    def makeExchange(self, currency, amount):
        formatted = currency.lower()
        print("Checking the cache...")
        if formatted in self.cache:
            print("It is in the cache!")
            return round(self.cache[formatted] * amount, 2)
        print("Sorry, but it is not in the cache!")
        return self.getFromApi(formatted, amount)


    def start(self):
        self.getFromApiStart(self.currency)
        
        while self.count != self._current:
                try:
                    currency = input(f"[Your currency: {self.currency}] Type code of currency to exchange: ")
                    if currency == "exit": break
                    amount = float(input("Amount to exchange: "))

                    result = self.makeExchange(currency, amount)
                    print(f"You received {result} {currency}.")
                except ValueError:
                    print("Incorrect format!")


def main():
    currency_code = input("Type code of your currency: ")
    exchange = CurrencyExchange(currency_code)
    exchange.start()


if __name__ == "__main__":
    main()
