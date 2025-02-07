import requests, email_sender.email_sender as sender # type: ignore

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = '7YORZTULWDBPC2PY' #'B7HX9OI7NMFH17JO'
NEWS_API_KEY = 'c826221cf49a4e6bb0713ede09a724a1'

MY_EMAIL = 'dansoltan05@gmail.com'
PASSWORD = 'jwka uwus daeb licl'
RECEIVER = 'mysecondaryaccpl123xyz@gmail.com'

stock_params = {
    'apikey': STOCK_API_KEY,
    'symbol': STOCK,
    'function': 'TIME_SERIES_DAILY'
}

news_params = {
    'apiKey': NEWS_API_KEY,
    'qInTitle': COMPANY_NAME
}

closing_prices = {}
time_series = list(requests.get(STOCK_ENDPOINT, params=stock_params).json()['Time Series (Daily)'].items())
closing_prices['yesterday'] = float(time_series[0][1]['4. close'])
closing_prices['the day before yesterday'] = float(time_series[1][1]['4. close'])
delta = abs(closing_prices['yesterday'] - closing_prices['the day before yesterday'])
percent = delta / closing_prices['the day before yesterday']
if percent >=0.05:
    print(closing_prices, delta, 'Get news')
    news = requests.get(NEWS_ENDPOINT, params=news_params).json()['articles'][:3:]
    print(news)
    messages_data = []
    for article in news:
        messages_data.append({'message_title': article['title'], 'message_body': article['description']})
    for article in messages_data:
        article['message_title'] = (f'{STOCK}: ' \
            f'{'🔺' if closing_prices["yesterday"]>closing_prices["the day before yesterday"] else '🔻'}'\
            f' {round(percent*100)}\t' + article['message_title'])
        if article['message_body']:
            article['message_body'] = article['message_body']
        print(article)
        sender.send_gmail(MY_EMAIL, PASSWORD, RECEIVER, **article, sender_name='me')



## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 



## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator



## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.



#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

