# Web scrapping Using Python3 
import requests
from bs4 import BeautifulSoup
import pprint

# Function to sort the list into the descending order
def sort_votes(hnlist):
    return sorted(hnlist, key=lambda k:k['votes'], reverse= True)

# Funtion to Create a Webpage using links and text items
def custom_webpage(links, texts):
    # Creating an empty list to store all the Story links having votes greater than 99
    hn = []
    for idx,item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        votes = texts[idx].select('.score')
        if len(votes):
            points = int(votes[0].getText().replace(' points', ''))
            if points >99:
              hn.append({'sl no.':idx+1,'title':title, 'link':href, 'votes': points})
    return sort_votes(hn)

# Create an object to requests HTML data from the Hackernews Website
res = requests.get("https://news.ycombinator.com/news?p=1")
sp = BeautifulSoup(res.text, 'html.parser')
links = sp.select('.storylink')
text = sp.select('.subtext')

# Object 2 
res2 = requests.get("https://news.ycombinator.com/news?p=2")
sp2 = BeautifulSoup(res2.text, 'html.parser')
links2 = sp2.select('.storylink')
text2 = sp2.select('.subtext')

# Combining both the links to access the news from the page 1 and page 2
mega_links = links + links2
mega_text = text + text2

# pprint is a function used for the prettty printing basically..... It will print the output in a good and formatted manner
pprint.pprint(custom_webpage(mega_links, mega_text))
