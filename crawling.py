import time
import hashlib
from bs4 import BeautifulSoup
import requests

# Ravida Saitova and Egor Gubanov


loot = ''
visited = set()

def find_loot(url1):
    global visited, loot
    page = requests.get(url1)
    soup = BeautifulSoup(page.content, 'html.parser')
    text = soup.get_text()

    loot_index = text.find('LOOT:')
    if (loot_index != -1):
        loot = text[text.find('LOOT:')+5:].split('\n')[0]
        return 
    else:
        for link in soup.find_all('a'):
            if (link.get('href').find('htm') != -1):
                link1 = 'http://sprotasov.ru/files/AIR/' + link.get('href')
                if (link1 not in visited):
                    visited.add(link1)
                    find_loot(link1)
        for iframe in soup.find_all('iframe'):
            if (iframe.attrs['src'].find('htm') != -1):
                link1 = 'http://sprotasov.ru/files/AIR/' + iframe.attrs['src']
                if (link1 not in visited):
                    visited.add(link1)
                    find_loot(link1)
        for form in soup.find_all('form'):
            if (form.attrs['action'].find('htm') != -1):
                link1 = 'http://sprotasov.ru/files/AIR/' + form.attrs['action']
                if (link1 not in visited):
                    visited.add(link1)
                    find_loot(link1)
        return 

with open('input.txt', 'r') as fin:
    url = fin.read()

visited.add(url)
find_loot(url)

with open('output.txt', 'w') as fout:
    fout.write(loot)