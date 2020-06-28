import requests
from bs4 import BeautifulSoup


url1 = 'https://www.merriam-webster.com/word-of-the-day'
url2 = 'https://www.keepinspiring.me/quote-of-the-day/'

source = requests.get(url1).content
soup = BeautifulSoup(source, 'lxml')
# print(soup)
word = soup.find('title').text.split('|')[0]
definition = soup.find(
    'div', {'class': 'wod-definition-container'}).p.text.replace(':', '-')

print('\n', word)
print(definition[1:])
s2 = BeautifulSoup(requests.get(url2).content, 'lxml').find(
    'div', {'class': 'author-quotes'}).text
print(f'\nQuote of the Day\n{s2}')
