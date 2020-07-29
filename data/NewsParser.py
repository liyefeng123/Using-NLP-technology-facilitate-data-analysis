import re
import time
from html.parser import HTMLParser
import datetime
from urllib import request
from bs4 import BeautifulSoup
import database_manipulation as dm

with request.urlopen('https://www.bbc.co.uk/news/localnews/2643123-manchester/20') as f:
    data = f.read().decode('utf-8')
soup = BeautifulSoup(data, 'html.parser')

# for i in soup.find_all("div",'travel-incident__body-content'):
#     print(i)
for i in soup.find_all("article","travel-incident"):
    Post_time = i.find_parents("article")[0].find_all('time')[0].get_text()
    News_Title = i.find("h3").get_text()
    News_content = i.find("div","travel-incident__body-content").get_text()
    if len(Post_time.split()) == 3:
        Post_time = str(datetime.date.today()) +' '+ Post_time.split()[2]
        print(Post_time)
        dm.News_insert(News_Title,News_content,Post_time)





