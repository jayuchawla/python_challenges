import requests
import re

next_url_idx = '90052'
count = 1000
comments=[]


import zipfile
archive = zipfile.ZipFile('channel.zip', 'r')

for idx in range(count):
    try:
        data = None
        with open('channel/' + next_url_idx+'.txt', 'r') as f:
            data = f.read()
        print(data)
        m = re.search(re.compile(r'Next nothing is ([\d]+)'), data)
        print(m.group(1))
        comments.append(archive.getinfo(next_url_idx+'.txt').comment)
        next_url_idx=m.group(1)
    except:
        break

comments = [comment.decode('utf-8') for comment in comments]
for c in comments:
    print(c, end='')
