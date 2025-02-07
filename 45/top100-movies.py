import requests as r, pandas as pd, re
from bs4 import BeautifulSoup as bs

URL = 'https://empireonline.com/movies/features/best-movies-2'

responce = r.get(URL)
soup = bs(responce.text, 'html.parser')
data = {
    'ranking': [],
    'title': [],
    'year': []
}
for el in soup.select('h2 strong')[::-1]:
    ranking = int(re.search(r'^[^)]+\)',el.string).group().rstrip(')'))
    data['ranking'].append(ranking)
    title = re.search(r'\s[^()]+', el.string).group().strip()
    data['title'].append(title)
    year = int(re.search(r'\(.+\)', el.string).group().strip('()'))
    data['year'].append(year)
data = pd.DataFrame(data)
print(data)
data.to_csv('45/movies.csv', index=False)
    