
import requests
from requests import session
from bs4 import BeautifulSoup
from bs4 import SoupStrainer

# # Ask user to enter URL
# url = input("Please enter a valid URL: ")

url = 'https://www.stltoday.com/news/local/govt-and-politics/logjam-breaks-in-missouri-senate-new-congressional-map-sent-to-house/article_fb7d664b-bd53-5e0b-99ea-2808ccab16d5.html#tracking-source=home-top-story'
page = requests.get(url)
  
# load the page content
text = page.content
 
# extra BS param that only finds paragraph (<p>) html elements
only_p_tags = SoupStrainer("p")

soup = BeautifulSoup(text, 'html.parser', parse_only=only_p_tags).prettify()

article_title = BeautifulSoup(text, 'html.parser').find("title") + ".html"

with open(str(article_title), "w", encoding = 'utf-8') as file:
    
    # prettify the soup object and convert it into a string
    file.write(str(soup))

print("Saved article as " + article_title + ".html")