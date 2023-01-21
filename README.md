# Twitter-Quote-Bot
A twitter bot to automatically gather quotes from the internet and save them in a database. The bot uses web scraping techniques and libraries to extract quotes from websites and then stores them in a database for future use. 

The bot also has the capability to automatically tweet a quote at regular intervals using cron jobs. The bot uses Twitter API for authentication and posting tweets.

Visit - https://twitter.com/ko8bot to checkout the bot.

## Working 

`scrape.py` - Scrapes the [goodreads](https://www.goodreads.com/quotes) website to scrape multiple pages of quotes and saves it in google sheet using requests, beatifulsoup and [gspread](https://docs.gspread.org/en/latest/) API.

`main.py` - Fetches single quote from sheets db and Initializes and Authenticates twitter account then tweets the quote using official twitter developer API.

`.env` - Saves the secrets and API tokens.

## Setup

1. Clone the project on your local system using: `git clone https://github.com/adhirajpandey/Twitter-Quote-Bot`
2. Setup Virtual Environment using: `python -m venv venv` and activate it.
3. Install the dependencies: `pip install -r requirements.txt`
4. Enable the Google Drive API, create a service account and downloadd the json key file. 
   Check this out for reference - [here](https://mljar.com/blog/authenticate-python-google-sheets-service-account-json-credentials/)
5. Create a Twitter account and register for developer account to get access to API.
6. Copy the required token values in .env file in the cloned directory.
7. Create a google sheet and name it `Twitter-Bot` and share it with that service account.
8. Scrape and Store the quotes using: `python scrape.py`
9. Test the tweet functionality using: `python main.py`
10. Deploy the main.py file with cron job using any cloud service provider to autmate the tweet process at set time interval.

## Sample

![image](https://user-images.githubusercontent.com/87516052/213847620-6ef72844-eae2-4728-8dfa-ccea2bdd42ec.png)

![image](https://user-images.githubusercontent.com/87516052/213847652-fd862211-0787-429b-bf4c-e8fccab1f336.png)

  
