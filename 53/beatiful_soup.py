import requests as r, pandas as pd
from bs4 import BeautifulSoup as bs
import urllib.parse
from pprint import pprint
import fake_useragent, ast, json, re

URL = f'https://www.zillow.com/san-francisco-ca/rentals/'
params = {

    'searchQueryState':
    {
        "pagination":{"currentPage":1},
        "isMapVisible":'false',
        "mapBounds":{"west":-122.58473483447266,
                    "east":-122.31488314990234,
                    "south":37.67495316396866,
                    "north":37.83971397283956},
        "mapZoom":12,
        "usersSearchTerm":"San Francisco CA",
        "regionSelection":[{"regionId":20330}],
        "filterState":{"fr":{"value":'true'},
                        "fsba":{"value":'false'},
                        "fsbo":{"value":'false'},
                        "nc":{"value":'false'},
                        "cmsn":{"value":'false'},
                        "auc":{"value":'false'},
                        "fore":{"value":'false'},
                        "price":{"min":'null',"max":586501},
                        "mp":{"min":'null',"max":3000},
                        "beds":{"min":1,"max":'null'},
                        "mf":{"value":'false'},
                        "land":{"value":'false'},
                        "manu":{"value":'false'}},
        "isListVisible":'true'
        }
    }

result_count = None
duplicates = 0
def get_data():
    user_agent = fake_useragent.UserAgent().random
    headers={
        "User-Agent": user_agent,  #"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
        "Accept-Language":"en-US,en;q=0.9",
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding":"gzip, deflate, br",
        "upgrade-insecure-requests":"1"
    }
    global params
    url = f'{URL}?{urllib.parse.urlencode(params).replace('+','').replace('\'null\'', 'null').replace('\'true\'', 'true').replace('\'false\'', 'false').replace('%27', '%22')}'
    responce = r.get(url, headers=headers)

    print(url)
    soup = bs(responce.text, features='lxml')
    #print(soup)
    # with open('53/page_source.html', 'w') as page_source:
    #     page_source.write(str(soup))
    # quit()
    global result_count
    result_count = int(soup.select_one('.result-count').string.split()[0])
    data = soup.find(attrs={'id': '__NEXT_DATA__'}).string
    #data = ast.literal_eval(str(data))
    data = json.loads(str(data))
    # with open('53/tmp.json', 'w') as tmp:
    #     json.dump(data, fp=tmp)
    # quit()

    #------------------ FIGURING OUT THE STRUCTURE OF THE SCRIPT ELEMENT WHICH CONTAINS PRICES ------------------#
    # pprint(data.keys())
    # pprint(data['props'].keys())
    # pprint(data['props']['pageProps'].keys())
    # pprint(data['props']['pageProps']['searchPageState'].keys())
    # pprint(data['props']['pageProps']['searchPageState']['cat1'].keys())
    # pprint(data['props']['pageProps']['searchPageState']['cat1']['searchResults'].keys())
    # pprint(data['props']['pageProps']['searchPageState']['cat1']['searchResults']['listResults'])

    try:
        next_page = data['props']['pageProps']['searchPageState']['cat1']['searchList']['pagination']['nextUrl']
    except:
        result_count = 0
    results = data['props']['pageProps']['searchPageState']['cat1']['searchResults']['listResults']
    try:
        data['props']['pageProps']['searchPageState']['cat2']['searchResults']['listResults']
    except:
        pass
    else:
        print('\n!!!TEST!!!\n')
    print(len(results))
    #------------------------------------------------------------------------------------------------------------#

    def get_page_dataframe(results)->pd.DataFrame:
        detailUrl = []
        price = []
        address = []

        for result in results:
            global duplicates
            #pprint(result.keys())
            #print(result['price'], result['address'], result['detailUrl'], sep=',\t')
            try:
                address.append(result['address'])
                price.append(result['price'])
                detailUrl.append(result['detailUrl'])
                # list(map(lambda x: x.append(result[f'{x=}'.split('=')[0]]), [address, price, detailUrl]))
            except KeyError:
                unit_prices = []
                #print(result.keys())
                for unit in result['units']:
                    duplicates +=1
                    unit_prices.append(unit['price'])
                price.append(min(unit_prices))
                detailUrl.append(f'https://www.zillow.com{result['detailUrl']}')

        price = ['$'+re.search(r'[0-9,\.\s]+', price_).group() for price_ in price]
        #print(detailUrl)

        df = pd.DataFrame(
            {
                'price': price,
                'address': address,
                'link': detailUrl
            }
        )
        return df

    df = get_page_dataframe(results)
    return df

df = pd.DataFrame()
df = df._append(get_data(), ignore_index=True)
while len(df)<result_count:
    print(len(df))
    params["searchQueryState"]['pagination']['currentPage']+=1
    df = df._append(get_data(), ignore_index=True)

df.to_csv('53/data.csv', index=False)
print(df)

