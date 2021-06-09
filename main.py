# Scrape Hacker News for stories with the most votes.
import requests
import pprint
from bs4 import BeautifulSoup
# check out Scrapy framework


resp = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(resp.text, 'html.parser')
links = soup.select('.storylink')
subtxt = soup.select('.subtext')


def sort_stories_by_votes(hn_list):
    return sorted(hn_list, key=lambda k: k['points'], reverse=True)


def create_custom_hn(link_list, subtxt_list):
    hn = []
    for idx, item in enumerate(link_list):
        title = link_list[idx].getText()
        href = link_list[idx].get('href', None)
        votes = subtxt_list[idx].select('.score')
        if len(votes):
            points = int(votes[0].getText().replace(' points', ''))
            if points > 500:
                hn.append({'title': title, 'link': href, 'points': points})
    return sort_stories_by_votes(hn)


pprint.pprint(create_custom_hn(links, subtxt))
