import requests
from bs4 import BeautifulSoup

headers = {
    'Accept-Language': 'en-US,en;q=0.5',
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
}

class WebScrapper:
    def makeRequest(self, method, url, query_params=None, body=None, headers=None):
        try:
            if "imdb.com/title" in url:
                response = requests.request(method, url, params=query_params, json=body, headers=headers)
            else:
                print("Invalid quote resource!")
                raise SystemExit
            if response.status_code == 400:
                print("Invalid quote resource!")

            try:
                if response.content:
                    return response
                else: raise KeyError
            except KeyError:
                print("Invalid quote resource!")
                raise SystemExit
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

    def parseImdbDescription(self, description):
        appears = 0
        i_slice = 0

        for index, c in enumerate(description):
            if c == ".":
                appears += 1
                if appears == 2:
                    i_slice = index

        return description[i_slice+2:]

    def parseImdbTitle(self, title):
        i_index = title.index('(')

        return title[:i_index-1]
        


def main():
    web_scraper = WebScrapper()
    url = input("Input the URL: ")
    req = web_scraper.makeRequest("GET", url, headers=headers)
    soup = BeautifulSoup(req.content, 'html.parser')

    info = dict()

    title = soup.find('title')

    description = soup.find('meta', { 'name': 'description' })

    info["title"] = web_scraper.parseImdbTitle(title.text)
    info["description"] = web_scraper.parseImdbDescription(description["content"])

    print(info)
    

if __name__ == "__main__":
    main()