# Web scrapping Using Python3 
import requests
from bs4 import BeautifulSoup
import pprint


def sort_votes(hnlist):
    return sorted(hnlist, key=lambda k:k['votes'], reverse= True)


def custom_webpage(links, texts):
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


res = requests.get("https://news.ycombinator.com/news?p=1")
sp = BeautifulSoup(res.text, 'html.parser')
links = sp.select('.storylink')
text = sp.select('.subtext')

res2 = requests.get("https://news.ycombinator.com/news?p=2")
sp2 = BeautifulSoup(res2.text, 'html.parser')
links2 = sp2.select('.storylink')
text2 = sp2.select('.subtext')

mega_links = links + links2
mega_text = text + text2

pprint.pprint(custom_webpage(mega_links, mega_text))