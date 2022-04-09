from unittest import result
import requests
from bs4 import BeautifulSoup
import re
url = "http://www.sge.com.cn/sjzx/mrhqsj"
headers = {'User-Agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}

def purify(str_):
    result = re.sub('\t', '', str_)
    result = re.sub('\r', '', result)
    result = re.sub('\n', '', result)
    return result

def data_get(url):
    import time
    response = requests.get(url, headers=headers)
    time.sleep(6)
    html = BeautifulSoup(response.text, 'lxml')
    tds = html.find_all('td')
    time = re.findall("\d{4}-\d{1,2}-\d{1,2}", html.text)[0]
    id_ = re.sub('-', '', time)
    result = []
    temp_id = id_ + "_0"
    temp = [temp_id, time]
    for i in range(0, 182):
        temp.append(purify(tds[i].text))
        if (i+1) % 13 == 0:
            temp_id = id_ + '_' + str(int((i+1) / 13)-1)
            temp.insert(0, temp_id)
            result.append(temp)
            temp = [time]
    result.pop(0)
    return result
data_get("http://www.sge.com.cn/sjzx/mrhqsj/10002423")
