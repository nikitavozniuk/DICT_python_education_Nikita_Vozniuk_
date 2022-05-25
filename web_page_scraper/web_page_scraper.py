import os
import requests

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
    webScrapper = WebScrapper()
    url = input("Input the URL: ")
    page_content = webScrapper.makeRequest("GET", url)

    file = None
    try:
        file = open(f"{os.getcwd()}\web_page_scraper\source.html", 'wb')
    except IOError:
        print("Unable to create file on disk.")
        file.close()
        return
    finally:
        file.write(page_content.content)
        print("Content saved.")
        file.close()
    

if __name__ == "__main__":
    main()