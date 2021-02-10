import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta


def crawl(date):
    r = requests.get(
        'https://www.taifex.com.tw/cht/3/futContractsDate?queryType=1&goDay=&doQuery=1&dateaddcnt=&queryDate={}%2F{}%2F{}'.format(date.year, date.month, date.day))
    if r.status_code == requests.codes.ok:
        soup = BeautifulSoup(r.text, 'html.parser')
        print('successfully got data from ', date)
    else:
        print('connect error')


date = datetime.today()
# get data from five days ago
while True:
    crawl(date)
    date = date - timedelta(days=1)
    if date < datetime.today() - timedelta(days=5):
        break
