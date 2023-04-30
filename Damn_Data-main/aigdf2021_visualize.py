import pandas as pd
import os

poi_filelist = []
for filename in os.listdir('.\data'):
    if filename.endswith('.csv'):
        poi_filelist.append('.\data'+'\\'+filename)
        
csv_0 = pd.read_csv(poi_filelist[0],index_col='Unnamed: 0')[['id','wgslng','wgslat']]
csv_0['type']=poi_filelist[0].split('_')[0]
for i in range(1,len(poi_filelist)):
    csv_i = pd.read_csv(poi_filelist[i],index_col='Unnamed: 0')[['id','wgslng','wgslat']]
    csv_i['type']=poi_filelist[i].split('_')[0]
    csv_0 = pd.concat([csv_0,csv_i],axis=0)
    csv_0.reset_index(drop=True,inplace=True)
    
from damndata.damn_geoBee.hotgrid import HotGridGenerator

hg = HotGridGenerator(gridUnit = 200, searchRadius = 200)
hg.grid_setting(csv_0,'wgslat','wgslng')
poi_hotMap = hg.gridCounting_basic(csv_0,'wgslat','wgslng')

'''
import seaborn as sns
from IPython.core.pylabtools import figsize

figsize(40,24)
sns.heatmap(poi_hotMap.sort_index(axis=0,ascending=False),cmap='Greys_r', cbar=False, xticklabels=False, yticklabels=False)
'''

import matplotlib
import matplotlib.pyplot as plt
from IPython.core.pylabtools import figsize

figsize(40,24)
plt.xticks([])  #去掉x轴
plt.yticks([])  #去掉y轴
plt.axis('off')  #去掉坐标轴
plt.scatter(csv_0['wgslng'],csv_0['wgslat'],c=[0,0,0,0.02],s=3000,marker='.',edgecolors = 'face',)
plt.savefig("200000.png")