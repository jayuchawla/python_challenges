import requests
import re

next_url_idx = '82682'
count = 400
for idx in range(count):
    data = requests.get('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={}'.format(next_url_idx))
    print(data.text)
    m = re.search(re.compile(r'and the next nothing is ([\d]+)'), data.text)
    print(m.group(1))
    next_url_idx=m.group(1)
