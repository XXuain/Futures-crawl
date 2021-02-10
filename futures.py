import requests
from bs4 import BeautifulSoup

r = requests.get(
    'https://www.taifex.com.tw/cht/3/futContractsDate?queryType=1&goDay=&doQuery=1&dateaddcnt=&queryDate=2021%2F02%2F05&commodityId=')
if r.status_code == requests.codes.ok:
    soup = BeautifulSoup(r.text, 'html.parser')
    print(soup.prettify())
