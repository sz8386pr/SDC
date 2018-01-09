#pip install --user requests
import requests
import os

'''
set omdb_key=something
export omdb_key = something
'''

key = os.environ['omdb_key']#something

base_url = 'http://www.omdbapi.com/'

movie = input('Movie title')

params = {'apikey' : key, 't' : movie}
data = requests.get(base_url, params).json()

print(data)
