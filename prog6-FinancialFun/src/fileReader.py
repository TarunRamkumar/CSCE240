from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import requests
import re

#Make sure URLs are HTML version of website links. To do this, open the company's 10k in the EDGAR viewer, then click the menu button. There should be an option to open in the HTML view. Click this, and this is the URL you should use.
def scrapeFile(company):
    if(company == "google"):
        url = "https://www.sec.gov/Archives/edgar/data/1652044/000165204424000022/goog-20231231.htm"
        #Need to change these filepaths to work within other project directories
        file = open("../data/Google10k-4Q-2024.txt","w", encoding =  "utf-8")

    else:
        url = "https://www.sec.gov/Archives/edgar/data/1467858/000146785823000029/gm-20221231.htm"
        file = open("../data/GM10k-4Q-2024.txt","w", encoding =  "utf-8")

    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    }
    
    website = requests.get(url = url, headers = headers)
    html = website.content.decode("utf-8")
    parser = BeautifulSoup(html,"html.parser")
    start = False
    headers = []
    for i in parser.stripped_strings:
        line = str(i)

        if "UNITED" in i and start == False:
            start = True
        if(start):
            #print(line)
            if(len(line) > 1):
                file.write(line+"\n")
                

    #print(headers)
    file.close
    return file
#a.documentlink