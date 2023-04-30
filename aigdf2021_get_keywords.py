from damndata.damn_geoSpider import geoautonavi, urlgrid
import pandas as pd

types = ['000000']
geocoor = [121.410108,31.175071,121.570918,31.320363] #bottomleft, topright #上海
url_collection = urlgrid.urlcreator_types(types, geocoor, grid=(0.02, 0.02))

keywords = 'KFC'

for typei in types:
    temp = []
    for i,url in enumerate(url_collection[typei]):
        urls = url.split('&')
        s = ""
        for urli in urls:
            if urli[0:6]=='types=':
                s += 'keywords=' + keywords + '&'
            else:
                s += urli + '&'
        temp.append(s[0:-1])
    url_collection[typei] = temp

#print(url_collection)

for typei in types:
    for i,url in enumerate(url_collection[typei]):
        pois = geoautonavi.getpois(url)
        geoautonavi.write_to_csv(pois,'./data/'+keywords+'_'+str(i)+'.csv')
        print(typei+'_'+str(i),':',url)
