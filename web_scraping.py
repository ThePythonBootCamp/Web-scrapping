import requests # This helps us access HTTPS
from bs4 import BeautifulSoup
import json

url = 'http://www.bu.edu/president/boston-university-facts-stats/'

# Fetch the webpage content
response = requests.get(url)
webpage_content = response.content

# Parse the HTML content
soup = BeautifulSoup(webpage_content, 'html.parser')

# Extract relevant data
data = {}
sections = soup.find_all('section', class_='facts')

for section in sections:
    heading = section.find('h2').get_text(strip=True)
    facts = section.find_all('p')
    facts_list = [fact.get_text(strip=True) for fact in facts]
    data[heading] = facts_list

# Save the data as a JSON file
with open('bu_facts_stats.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)

print("Data has been scraped and stored in 'bu_facts_stats.json'")
