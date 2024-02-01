from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import requests

url = "https://www.sec.gov/Archives/edgar/data/1652044/000165204424000022/goog-20231231.htm"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}


req = Request(
    url=url, 
    headers=headers
)
website = requests.get(url = url, headers = headers)

html = website.content.decode("utf-8")
parser = BeautifulSoup(html,"html.parser")





file = open("Google10k-4Q-2024.txt","w", encoding = "utf-8")






#a.documentlink