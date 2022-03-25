
import requests
from requests import session
from bs4 import BeautifulSoup
from bs4 import SoupStrainer


# Python3 code to remove whitespace
def cleanup_article_title_as_file_name(string):
    remove_whitespaces = string.replace(" ", "_")
    keep_first_40_characters = remove_whitespaces[:40]
    return keep_first_40_characters

# Ask user to enter URL
url = input("Please enter a valid URL: ")

# or just set the url here
# url = 'https://www.stltoday.com/news/local/govt-and-politics/logjam-breaks-in-missouri-senate-new-congressional-map-sent-to-house/article_fb7d664b-bd53-5e0b-99ea-2808ccab16d5.html#tracking-source=home-top-story'

page = requests.get(url)
  
# load the page content
text = page.content
 
# extra BS param that only finds paragraph (<p>) html elements
only_p_tags = SoupStrainer("p")

soup = BeautifulSoup(text, 'html.parser', parse_only=only_p_tags).prettify()

article_title = BeautifulSoup(text, 'html.parser').find("title")

file_name = cleanup_article_title_as_file_name(article_title.string)

with open(f"{file_name}.html", "w", encoding = 'utf-8') as file:
    file.write(article_title.string + "\n")
    file.write(url + "\n")
    file.write(soup)

print("Saved article as " + file_name + ".html")