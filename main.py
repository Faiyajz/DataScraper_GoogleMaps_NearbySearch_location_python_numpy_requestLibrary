import pandas as pd, numpy as np
import requests
import json
import time
from google.colab import files

final_data = []  # Parameters
coordinates = ['-8.705833, 115.261377']
keywords = ['restaurant']
radius = '1000' #meter
api_key = 'your api'  # insert your Places API
for coordinate in coordinates:
    for keyword in keywords:
        url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=' + coordinate + '&radius=' + str(radius) + '&keyword=' + str(keyword) + '&key=' + str(api_key)
        while True:
            print(url)
            response = requests.get(url)
            json_response = json.loads(response.text)
            results = json_response['results']
            for result in results:
                name = result['name']
                place_id = result['place_id']
                latitude = result['geometry']['location']['lat']
                longitude = result['geometry']['location']['lng']
                rating = result['rating']
                types = result['types']
                vicinity = result['vicinity']
                data = [name, place_id, latitude, longitude, rating, types, vicinity]
                final_data.append(data)
                time.sleep(5)
                if 'next_page_token' not in json_response:
                    break
                else:
                    next_page_token = json_response['next_page_token']
                    url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?key=' + str(api_key) + '&pagetoken=' + str(next_page_token)
                    labels = ['Place Name', 'Place ID', 'Latitude', 'Longitude', 'Types', 'Vicinity']
                    export_dataframe_1_medium = pd.DataFrame.from_records(final_data, columns=labels)
                    export_dataframe_1_medium.to_csv('restaurantsNearbyOneKilometer.csv')
