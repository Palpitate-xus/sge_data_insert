import requests
from bs4 import BeautifulSoup
import re
from sge_url import data_get
from databaseInsert import insertToDatabase
url = "http://www.sge.com.cn/sjzx/mrhqsj"
headers = {'User-Agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}
response = requests.get(url, headers=headers)
html = BeautifulSoup(response.text, 'html.parser')
raw_list = html.find_all('a', class_ = "title fs14 color333 clear")
url_list = []
pattern = "/sjzx/mrhqsj/\d+"
for i in raw_list:
    url_list.append("http://www.sge.com.cn"+re.findall(pattern, str(i))[0])

for url in url_list:
    insertToDatabase(data_get(url))


