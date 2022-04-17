import os
import time

import pandas as pd
import requests
import re

from tqdm import tqdm

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
}
def download(objID,ra,dec):
    httpurl="https://skyserver.sdss.org/dr17/SkyServerWS/ImgCutout/getjpeg?TaskName=Skyserver.Explore.Image&ra="+str(ra)+"&dec="+str(dec)+"&scale=0.2&width=200&height=200"
    response = requests.get(httpurl,headers=headers)
    print(httpurl)
    with open('photo/sdss_objID_'+ str(objID) + '.png', 'wb') as f:
        f.write(response.content)
Lmore15=pd.read_csv('200wLmore15_notrepeat.csv')
objID=Lmore15['objID']
ra=Lmore15['RA_ICRS']
dec=Lmore15['DE_ICRS']
for i in tqdm(range(len(objID))):
    download(objID[i],ra[i],dec[i])


#https://media1.99b10.com/albums/main/960x870/6000/6910/51234.jpg
#https://media2.99b10.com/albums/main/960x870/15000/15851/119438.jpg