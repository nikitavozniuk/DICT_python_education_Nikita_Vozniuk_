import os
import string
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

path = os.getcwd()

class WebScrapper:
    data = []
    titles = []
    _temp = []
    _tag = None

    def __init__(self, tag) -> None:
        self._tag = tag

    def saveTitles(self, page):
        for index, title in enumerate(self.titles):
            file = None
            try:
                file = open(f"{path}\web_page_scraper\Page_{page}\{title}.txt", 'w')
            except IOError:
                print("Unable to create file on disk.")
                file.close()
                return
            finally:
                file.write(self.data[index]["title"])
                print(f"{self.data[index]['title']} saved.")
                file.close()
        self.data = []
        self.titles = []
        self._temp = []
        print(f"Saved all articles.")

    def formatTitles(self):
        for item in self.data:
            new_string = item["title"].translate(str.maketrans('', '', string.punctuation + "—"))
            _ = " ".join(new_string.split()).replace(" ", "_")
            self.titles.append(_)

    def setTitles(self, soup):
        for a in soup.find_all('a', { 'data-track-action': 'view article' }):
            self._temp.append({ "title": a.contents[0] })

    def setTags(self, soup):
        for index, tag in enumerate(soup.find_all('span', { 'data-test': 'article.type' })):
            _tag = tag.find('span')
            self._temp[index]["tag"] = _tag.text
        for value in self._temp:
            if self._tag in value["tag"]:
                self.data.append(value)

    def startScrapping(self, soup, page):
        self.setTitles(soup)
        self.setTags(soup)
        self.formatTitles()
        self.saveTitles(page)

    def makeRequest(self, method, url, query_params=None, body=None, headers=None):
        try:
            response = requests.request(method, url, params=query_params, json=body, headers=None)
            if response.status_code == 400 or response.status_code == 404:
                print(f"The URL returned {response.status_code}!")
                raise SystemExit

            try:
                if response.content:
                    return response
                else: raise KeyError
            except KeyError:
                print("Invalid quote resource!")
                raise SystemExit
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
        

def main():
    pages = int(input("Input number of pages: "))
    tag = input("Input tag name: ")
    webScrapper = WebScrapper(tag)

    for i in range(pages):
        page = i + 1
        os.mkdir(f"{path}\web_page_scraper\Page_{page}")
        page_content = webScrapper.makeRequest("GET", f"https://www.nature.com/nature/articles?sort=PubDate&year=2022&page={page}").content
        soup = BeautifulSoup(page_content, 'html.parser')
        webScrapper.startScrapping(soup, page)


if __name__ == "__main__":
    main()