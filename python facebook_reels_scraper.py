import requests
from bs4 import BeautifulSoup

# Replace with the target profile's Facebook URL
profile_url = 'https://www.facebook.com/share/18pxx7Uhvs/'

# Send a GET request to the profile
response = requests.get(https://www.facebook.com/share/18pxx7Uhvs/)

# Check if the request was successful
if response.status_code == 200:
# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find the reels section (adjust the selector as needed)
reels_section = soup.find('div', {'id': 'reels-section'})

if reels_section:
# Extract and print reels information
for reel in reels_section.find_all('div', {'class': 'reel-item'}):
print(reel.find('a')['href'])
else:
print("No reels found or the profile is private.")
else:
print(f"Failed to retrieve the profile. Status code: {response.status_code}")
python facebook_reels_scraper.py

