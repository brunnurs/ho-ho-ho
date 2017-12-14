import math
import pandas as pd
from haversine import haversine
import numpy as np

def updatePheromon(pheromon, gift1, gift2, value):
    d = pheromon.get(min(gift1, gift2), 0)
    if d == 0:
        pheromon[min(gift1,gift2)] = {}
    pheromon[min(gift1,gift2)][max(gift1,gift2)] = value

def getPheromon(pheromon, gift1, gift2):
    d = pheromon.get(min(gift1,gift2), 0)
    if d != 0:
        d = d.get(max(gift1,gift2),0)
    return d


gifts_df = pd.read_csv("..\\data\\gifts.csv")

for idx in range(1, 10):
    north_pole = (90, 0)
    distance_to_north_pole = haversine(north_pole, (gifts_df['Latitude'][idx], gifts_df['Longitude'][idx]))
    print("Lat:{}, Long:{}, distance to north pole:{}".format(gifts_df['Latitude'][idx]
                                                              , gifts_df['Longitude'][idx]
, distance_to_north_pole))
nrGifts = gifts_df['GiftId'].count()
pheromon = {}
print(nrGifts)

updatePheromon(pheromon,2,24,12)

NR_ANT = 100
bestSolution = 1000*1000*1000



