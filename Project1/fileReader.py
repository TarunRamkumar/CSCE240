from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import requests
import re

#Opening Files
#url = "https://www.sec.gov/Archives/edgar/data/1652044/000165204424000022/goog-20231231.htm"
url = "https://www.sec.gov/Archives/edgar/data/1467858/000146785823000029/gm-20221231.htm"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
}


req = Request(
    url=url, 
    headers=headers
)
website = requests.get(url = url, headers = headers)
file = open("Google10k-4Q-2024.txt","w", encoding =  "utf-8")
html = website.content.decode("utf-8")
parser = BeautifulSoup(html,"html.parser")

parts = len(parser.find_all("span",string=re.compile("PART")))/2

print(parts)
start = False
for i in parser.stripped_strings:
    line = str(i)
    if "UNITED" in i and start == False:
       start = True
    if(start):
        file.write(line+"\n")













#a.documentlink