# This is a web scraper program built with Python 3 using requests and bs4
# I'll likely come back and update this at a later date with more functionality

import requests
from bs4 import BeautifulSoup as bs

github_user = input('Input Github Username: ')
url = 'https://github.com/' + github_user
r = requests.get(url)
soup = bs(r.content, 'html.parser')
profile_pic = soup.find('img', {'alt' : 'Avatar'})['src']

print("\nAccount Username: " + github_user)
print("Account Link: " + url)
print("Account Profile Picture: " + profile_pic)