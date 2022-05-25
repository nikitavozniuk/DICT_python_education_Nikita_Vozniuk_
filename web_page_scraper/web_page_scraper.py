import requests

class WebScrapper:
    def makeRequest(self, method, url, query_params=None, body=None):
        try:
            response = requests.request(method, url, params=query_params, json=body)
            if response.status_code == 400:
                print("Invalid quote resource!")

            response_content = response.json()
            try:
                return response_content["content"]
            except KeyError:
                print("Invalid quote resource!")
                raise SystemExit
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)


def main():
    web_scraper = WebScrapper()
    url = input("Input the URL: ")
    response = web_scraper.makeRequest("GET", url)
    print(response)


if __name__ == "__main__":
    main()