import os, email_sender, requests as r, pandas as pd
from dotenv import *
from bs4 import BeautifulSoup as bs

import email_sender.email_sender

email_data = dict(dotenv_values())
MY_EMAIL, PASSWORD, RECEIVER = email_data.values()


headers = {    
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", 
    "Accept-Encoding": "gzip, deflate, br, zstd", 
    "Accept-Language": "ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7", 
    "Priority": "u=0, i", 
    "Sec-Ch-Ua": "\"Not A(Brand\";v=\"8\", \"Chromium\";v=\"132\", \"Microsoft Edge\";v=\"132\"", 
    "Sec-Ch-Ua-Mobile": "?0", 
    "Sec-Ch-Ua-Platform": "\"Windows\"", 
    "Sec-Fetch-Dest": "document", 
    "Sec-Fetch-Mode": "navigate", 
    "Sec-Fetch-Site": "cross-site", 
    "Sec-Fetch-User": "?1", 
    "Upgrade-Insecure-Requests": "1", 
    "Cookie": 'session-id=132-4478545-8151263; session-id-time=2082787201l; i18n-prefs=USD; ubid-main=134-4265211-7975358; sp-cdn="L5Z9:GB"; session-token=XI6RxOCJ5MDNot6DWs9MVBWrqHMktLWfcaeFesMqhJJ+/fNxpl9c1XodbSBETPpQw0+Nuo1Q86dAq6WApJHwvBpv1phUhTAPO0WmLYmFBdklU5i8E8TNGsjwG6UdRULxdRtpUzdM5fqKPBGNMDqSeMNqSMUAZ8S3KdUJeeBQeKpTSIsHHYOg/q5tLbGie552qVwt5jzPn5/zgKB/q7fZoOzsEvBoahVNy1YoG8gGDAkETBUFLZZqek8VeqXTYMnqUtt/QfyUEh5T6bklOiFWsWoW00rYO2Hm5qkWRGuIZKhbCd/4JA+bjcrAXVRivoZusO08VAT03G8ZeMzLOWy6BOXD/UqdKhTg; csm-hit=tb:Q80CNTAXPVBNZ7PZRS35+b-AHS9G88MYY2V1AQQAJ0D|1738604111764&t:1738604111764&adb:adblk_no',
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0", 
  }

URL = 'https://www.amazon.com/dp/B01NBKTPTS?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1'
TARGET_PRICE = 150


responce = r.get(URL, headers=headers)
soup = bs(responce.text, features='lxml')
price = float(soup.select_one('span[class=\'aok-offscreen\']').string.strip(' $'))
product_title = soup.select_one('#productTitle').string.strip(' "')
if price < TARGET_PRICE:
    email_sender.email_sender.send_gmail(MY_EMAIL, PASSWORD, RECEIVER, f'Get {product_title} for ${price}', URL, 'me')



