import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
# Define the base URL for the Wikipedia API
base_url = "https://en.wikipedia.org/w/api.php"

# Define the parameters for the API request
params = {
    "action": "query",
    "format": "json",
    "list": "search",
    "srprop": "size",
    "srsearch": "covid",
    "srnamespace": "0",
    "srlimit": "1"
}

# Create an empty dictionary to store the number of COVID-related articles per month
articles_per_month = {}

# Define the start date as January 2022
start_date = datetime(2022, 1, 1)

# Define the end date as December 2022
end_date = datetime(2022, 12, 31)

# Loop through each month in 2022
while start_date <= end_date:

    # Set the search string to the month and year
    search_string = start_date.strftime("%B %Y")
    params["srsearch"] = f"covid {search_string}"
    
    # Make a request to the Wikipedia API
    response = requests.get(base_url, params=params)
    data = response.json()
    
    # Get the number of articles for the current month and year
    num_articles = data["query"]["searchinfo"]["totalhits"]
    
    # Add the number of articles to the dictionary
    articles_per_month[start_date.strftime("%B %Y")] = num_articles
    
    # Move to the next month
    start_date = start_date + timedelta(days=31)

# Print the dictionary
print(articles_per_month)



# Create a list of the month-year strings and a list of the corresponding article counts
months = list(articles_per_month.keys())
counts = list(articles_per_month.values())

# Create a bar chart of the article counts
plt.bar(months, counts)

# Add a title and labels to the chart
plt.title("Number of COVID-related Wikipedia Pages by Month in 2022")
plt.xlabel("Month")
plt.ylabel("Number of Pages")

# Display the chart
plt.show()

