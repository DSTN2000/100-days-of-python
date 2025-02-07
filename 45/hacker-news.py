import requests as r, pandas as pd
from bs4 import BeautifulSoup as bs

URL = 'https://news.ycombinator.com/news'

responce = r.get(URL)
soup = bs(responce.text, 'html.parser')
titles = [next(titleline.children) for titleline in soup.select('span[class=\'titleline\']')] 
#note 0: titles are inside of anchor elements which are contained inside of span elements wirh the class 'titleline'
#note 1: almost every titleline span contains two anchor elements: the second one is host website (some might have just one anchor though)
scores = soup.select('span[class=\'score\']')


articles_data = {
    'title': [title.string for title in titles],
    'link': [title.get('href') for title in titles],
    'score': [int(score.string.split()[0]) for score in scores]
}
articles_data = pd.DataFrame(articles_data)
articles_data = articles_data.sort_values(by=['score'], ascending=False)
print(articles_data)
