import requests
import datetime
from newsapi import NewsApiClient

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHA_VANTAGE_API_KEY = "9JEF0FDJA59K2HWZ"
PRICE_DIFF = 0.01
NEWS_API = "0e2aa9afe1f4465491e283fc52b261f7"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
parameters_stocks = {
    "function": 'TIME_SERIES_DAILY',
    "symbol": STOCK,
    "apikey": ALPHA_VANTAGE_API_KEY
}
# def last_business_day():
#     today = datetime.datetime.now()
#     offset = max(1, (today.weekday() + 6) % 7 - 3)
#     timedelta = datetime.timedelta(offset)
#     most_recent = today - timedelta
#     return most_recent
#
# def second_last_bd(day):
#     offset = max(1, (day.weekday() + 6) % 7 - 3)
#     timedelta = datetime.timedelta(offset)
#     second_most_recent = day - timedelta
#     return second_most_recent
#
# def last_2_business_days():
#     last_bd = last_business_day()
#     sec_last_bd = second_last_bd(last_bd)
#     return last_bd.strftime("%Y-%m-%d"), sec_last_bd.strftime("%Y-%m-%d")

with requests.get(url="https://www.alphavantage.co/query?", params=parameters_stocks) as response:
    response.raise_for_status()
    stock_data = response.json()

dates_list = list(stock_data["Time Series (Daily)"])
last_bd_data_close = float(stock_data["Time Series (Daily)"][dates_list[0]]["4. close"])
second_last_bd_data_close = float(stock_data["Time Series (Daily)"][dates_list[1]]["4. close"])
ratio = last_bd_data_close/second_last_bd_data_close

print(ratio, last_bd_data_close, second_last_bd_data_close)

if ratio < 1-PRICE_DIFF or ratio > 1+PRICE_DIFF:
    print(ratio, "big change - get news")


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
parameters_news = {
    "apiKey": NEWS_API,
    "qInTitle": COMPANY_NAME
}
with requests.get(url="https://newsapi.org/v2/everything?", params=parameters_news) as response:
    response.raise_for_status()
    articles = response.json()["articles"]
print(articles)


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


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

