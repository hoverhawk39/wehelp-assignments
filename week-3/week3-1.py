import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import json
import urllib.request as request
src='https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json'
with request.urlopen(src) as response:
    page_data = json.load(response)
    # print(page_data)
tlist=page_data['result']['results']
with open('data.csv','w',encoding='utf-8') as fw:
    for spot in tlist:
        fw.write(spot['stitle']+',')
        fw.write(spot['address'][5:8]+',')
        fw.write(spot['longitude']+',')
        fw.write(spot['latitude']+',')
        first=spot['file'].split('https')[1]
        fw.write('https'+first+'\n')