'''
this module should be run once before interacting with api
this will fetch data of characters and quotes 
from https://the-one-api.dev/ and 
populate the database based on the design in models.py
'''

import requests
from decouple import config
from django.db import IntegrityError
from movie.models import Characters, Quotes

BEARER = config('BEARER')
base_url = 'https://the-one-api.dev/v2'
headers = {'Authorization': BEARER}


# get all characters
c = requests.get(
    url=base_url+'/character',
    headers = headers
)
characters = c.json()['docs']

# create character objects
for character in characters:
    name = character['name']
    try:
        Characters.objects.create(name=name)
    except IntegrityError:
        pass

# get all quotes
q = requests.get(
    url=base_url+'/quote',
    headers = headers
)
quotes = q.json()['docs']

# create quote objects
characters_id_name = {}
for character in characters:
    characters_id_name[character['_id']] = character['name']
for quote in quotes:
    text=quote['dialog']
    character_id = quote['character']
    character_name = characters_id_name[character_id]
    character=Characters.objects.get(name=character_name)
    Quotes.objects.create(text=text, character=character)
