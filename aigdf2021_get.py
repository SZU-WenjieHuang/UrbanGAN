from damndata.damn_geoSpider import geoautonavi, urlgrid
import pandas as pd

types = ['160000']
geocoor = [121.410108,31.175071,121.570918,31.320363] #bottomleft, topright #上海
url_collection = urlgrid.urlcreator_types(types, geocoor, grid=(0.01, 0.01))

for typei in types:
    for i,url in enumerate(url_collection[typei]):
        pois = geoautonavi.getpois(url)
        geoautonavi.write_to_csv(pois,'./data/'+typei+'_'+str(i)+'.csv')
        print(typei+'_'+str(i),':',url)

