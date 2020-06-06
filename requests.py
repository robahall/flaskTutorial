import requests

url = 'http://localhost:5000/results'
r = requests.post(url,json={'Median Income':4.86,
                            'House Age':29,
                            'Average Rooms':5,
                            'Average Bedrooms':1,
                            'House Population':759,
                            'Average Occupied':3.7
                            })

print(r.json())