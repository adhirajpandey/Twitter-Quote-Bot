import gspread
import twitter
import os
from dotenv import load_dotenv

load_dotenv()

def connectTwitter():
    
    #twitter key values
    TOKEN = os.getenv("TOKEN")
    TOKEN_SECRET = os.getenv("TOKEN_SECRET")

    CONSUMER_KEY = os.getenv("CONSUMER_KEY")
    CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")

    try:
        #creating twitter object while authenticating
        t = twitter.Twitter(
        auth = twitter.OAuth(TOKEN, TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET))

        return t

    except:
        print("Error while authenticating with twitter")

def connectSheet():
    
    #google api service account key json path
    SERVICE_KEY_FILE = os.getenv("SERVICE_KEY_FILE")

    try:
        #connecting with google sheet
        gc = gspread.service_account(SERVICE_KEY_FILE)
        wks = gc.open("Twitter-Bot").sheet1

        return wks

    except:
        print("Error while connecting with google sheet")

def main():
    
    wks = connectSheet()
    t = connectTwitter()

    #get quote text value from sheet  (i.e 2nd row since 1st row is header)
    quote_text = wks.acell('A2').value

    #tweet the fetched quote
    t.statuses.update(status = quote_text)

    #delete the quote from sheet
    wks.delete_rows(2)

print("Successfully tweeted a quote from the database")

if __name__ == "__main__":
    main()