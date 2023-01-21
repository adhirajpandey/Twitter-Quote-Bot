import gspread
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://www.goodreads.com/quotes?page="

STARTING_PAGE = 1
ENDING_PAGE = 5


#FUNTION DEFINITIONS

def scrape_quotes():
    try :
        all_quotes = []
        
        for page in range(STARTING_PAGE, ENDING_PAGE + 1):
            res = requests.get(f"{BASE_URL}{page}")
            soup = BeautifulSoup(res.text, "html.parser")
            quotes = soup.find_all(class_="quote")
            print("Currently Scraping Page - " + str(page))

            for quote in quotes:
                all_quotes.append({
                    "text": quote.find(class_="quoteText").get_text(),
                    "author": quote.find(class_="authorOrTitle").get_text()
                })
        return all_quotes
    
    except:
        print("Error while scraping quotes")


def cleanQuotes(list_of_quotes):
    try :
        clean_quotes = []

        for t in list_of_quotes:
            text = (t["text"]).strip()
            q = (text[1:text.index('\n') - 1])
            
            #to filter only small sized quotes in our db
            if len(q) < 300:
                clean_quotes.append(q)
        
        return clean_quotes
    
    except:
        print("Error while cleaning quotes")


def pushQuotes(clean_quotes):
    #google api service account key json path
    SERVICE_KEY_FILE = 'twitter-bot-service-key.json'

    try:
        #connecting with google sheet
        gc = gspread.service_account(SERVICE_KEY_FILE)
        wks = gc.open("Twitter-Bot").sheet1

        for quote in clean_quotes:
            wks.append_row([quote])
            print("Added")

    except:
        print("Error while pushing quotes to sheet")


#DRIVER CODE
def main():
    all_quotes = scrape_quotes()
    clean_quotes = cleanQuotes(all_quotes)

    print("Total Number of Quotes Scraped - " + str(len(clean_quotes)))

    print("Now pushing clean quotes to quotes database")
    
    pushQuotes(clean_quotes)

    print("Successfully pushed quotes to database")


if __name__ == "__main__":
    main()
