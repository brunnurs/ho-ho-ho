import pandas as pd
from haversine import haversine

gifts_df = pd.read_csv("data/gifts.csv")

for idx in range(1, 10):
    north_pole = (90, 0)
    distance_to_north_pole = haversine(north_pole, (gifts_df['Latitude'][idx], gifts_df['Longitude'][idx]))
    print("Lat:{}, Long:{}, distance to north pole:{}".format(gifts_df['Latitude'][idx]
                                                              , gifts_df['Longitude'][idx]
                                                              , distance_to_north_pole))




