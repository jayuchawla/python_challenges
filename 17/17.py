from urllib.request import Request, urlopen
import requests
response = requests.get('http://www.pythonchallenge.com/pc/def/linkedlist.php')
# print(session.cookies.get_dict())
print(response.headers)

# header
# {'Set-Cookie': 'info=you%20should%20have%20followed%20busynothing...; expires=Sun, 10-Apr-2022 09:13:59 GMT; Max-Age=604800; path=/; domain=.pythonchallenge.com', 'Content-type': 'text/html; charset=UTF-8', 'Content-Length': '524', 'Date': 'Sun, 03 Apr 2022 09:13:59 GMT', 'Server': 'lighttpd/1.4.55'}
response = requests.get('http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing={}'.format(12345))
# print(response.text)


# import re
# aggregate_info = ''
# next_url_idx = '12345'
# count = 400
# for idx in range(count):
#     try:
#         data = requests.get('http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing={}'.format(next_url_idx))
#         cookie_header = data.headers
        
#         print(data.text)
#         m1 = re.search(re.compile(r'info=(.*?);'), cookie_header['Set-Cookie'])
#         aggregate_info += m1.group(1)
#         m = re.search(re.compile(r'and the next busynothing is ([\d]+)'), data.text)
        
#         print(m.group(1))
#         print(m1.group(1))
        
#         next_url_idx=m.group(1)
#     except:
#         break
# # below url gives: that's it
# # http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=83051

# print(aggregate_info)
# above gives: BZh91AY%26SY%94%3A%E2I%00%00%21%19%80P%81%11%00%AFg%9E%A0%20%00hE%3DM%B5%23%D0%D4%D1%E2%8D%06%A9%FA%26S%D4%D3%21%A1%EAi7h%9B%9A%2B%BF%60%22%C5WX%E1%ADL%80%E8V%3C%C6%A8%DBH%2632%18%A8x%01%08%21%8DS%0B%C8%AF%96KO%CA2%B0%F1%BD%1Du%A0%86%05%92s%B0%92%C4Bc%F1w%24S%85%09%09C%AE%24%90

aggregate_info = 'BZh91AY%26SY%94%3A%E2I%00%00%21%19%80P%81%11%00%AFg%9E%A0%20%00hE%3DM%B5%23%D0%D4%D1%E2%8D%06%A9%FA%26S%D4%D3%21%A1%EAi7h%9B%9A%2B%BF%60%22%C5WX%E1%ADL%80%E8V%3C%C6%A8%DBH%2632%18%A8x%01%08%21%8DS%0B%C8%AF%96KO%CA2%B0%F1%BD%1Du%A0%86%05%92s%B0%92%C4Bc%F1w%24S%85%09%09C%AE%24%90'
import bz2
from urllib.parse import unquote_to_bytes
str_to_bytes = unquote_to_bytes(aggregate_info.replace("+", " "))
print(str_to_bytes)
print(bz2.decompress(str_to_bytes))

# gives: is it the 26th already? call his father and inform him that "the flowers are on their way". he\'ll understand.
# mozart father name: leopold
import xmlrpc.client
conn = xmlrpc.client.ServerProxy('http://www.pythonchallenge.com/pc/phonebook.php')
print(conn.phone('Leopold'))

# send message via cookie
request = Request(
    "http://www.pythonchallenge.com/pc/stuff/violin.php",
    headers={"Cookie":"info=the flowers are on their way"}
)

response = urlopen(request).read().decode()
print(response)