
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

class BeatifullSoupOperator:

    def __init__(self):
        self.header = {'User-Agent': 'Mozilla/5.0'}
        self.soup = None
        self.val = None
        self.pvp = None
        self.div = None

    def get_page(self,url):
        req = Request(url,headers=self.header)
        page = urlopen(req)
        self.soup = BeautifulSoup(page)
        

    def get_value(self,tag,class_):
        self.value = self.soup.find(tag, class_=class_).text
        
    def get_all_fundamentals(self):
        self.value = self.soup.find_all('strong', class_='value')
        for index, value in enumerate(self.value):
            if index == 0:
                self.fii_value = str(value.text)

            elif index == 3:
                self.fii_div = str(value.text)

            elif index == 6:
                self.fii_pvp = str(value.text)
                break
            else:
                pass
