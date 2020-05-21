from bs4 import BeautifulSoup
from Task2.url import page

soup = BeautifulSoup(page, 'html.parser')

print(soup.find_all('a'))



