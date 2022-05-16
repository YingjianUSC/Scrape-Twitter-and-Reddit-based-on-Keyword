1. Installe Requirements
Using the  requirements.txt file to install all the packages needed.

2. Get API
To scrape Twitter, you don't need to apply for API.
To scrape Reddit, you need to register the Reddit API. You can start from here:
https://www.reddit.com/wiki/api
First, you need to sign up for the API.
Second, record the client ID, client secret, and user agent.

3. Run the files
There are three mode to run the file.
	
	Mode 1: python scraper.py --scrape 

This will scrape the data but return only 5 entries of each 
dataset.

	Mode 2: python scraper.py --static <path_to_dataset> 
		eg: python scraper.py --static datasource1.csv

This will return the static dataset scraped from the web and 
stored in CSV file.

	Mode 3: scraper.py

This will scrape data and return the complete scraped datasets.
