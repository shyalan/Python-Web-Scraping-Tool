import requests
from bs4 import BeautifulSoup

def scrape_quotes():
    # Send a GET request to the website
    url = 'http://quotes.toscrape.com'
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract quotes and authors
        quotes = soup.select('.quote .text')
        authors = soup.select('.quote .author')

        # Display the scraped data
        for quote, author in zip(quotes, authors):
            print(f'"{quote.get_text()}" - {author.get_text()}')

    else:
        print(f'Error: Unable to retrieve data. Status code: {response.status_code}')

if __name__ == "__main__":
    scrape_quotes()
