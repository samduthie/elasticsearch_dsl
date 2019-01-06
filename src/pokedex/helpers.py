import requests 

import pokebase as pb

ROOT_POKE_URL = 'https://pokeapi.co/api/v2'
POKE_URL = ROOT_POKE_URL + '/pokemon/'

# def get_pokemon(name):
# 	return pb.pokemon(name)

def get_sprite(name):
	import requests 
	url = POKE_URL + name
	data = requests.get(url).json()

	sprite = data['sprites']['front_shiny']
	return sprite

def get_image(name):
	return "<img src='{}'>".format(get_sprite(name))