import re
import requests

def get_pokemon_info(name):
    
    
    """
    Gets info about a specified pokemon 
    :para, name: Pokemon name
    :return: Dictionary of pokemon info
    
    
    """
    print('Getting Pokemon Info...', end='')
    
    
    #checks if given pokemon name is valid
    if name == None:
        print("Invalid name")
        return
    
    name = name.strip().lower()
    
    if name == '':
        print("empty name paramaerter")
        
        
    url="https://pokeapi.co/api/v2/pokemon/" + name
    resp_msg = requests.get(url)
    
    if resp_msg.status_code == 200:
        print('success')
        return resp_msg.json()
    
    else:
        print('failed. Code', resp_msg.status_code)
        print("That's not a pokemon, Please try another name")
        return
    


def get_pokemon_image_url(name):
    
    """
    This gets the pokemon url of the photo for download
    :param limit: name of the pokemon
    
    :return: the pokemon info url in dictionary
    """
    pokemon_dict = get_pokemon_info(name)
    
    if pokemon_dict:
        return pokemon_dict['sprites']['other']['official-artwork']['front_default']
    





def get_pokemon_list (limit =100, offset =0):

    """
    This gets all the pokemon list of 100 from the PokeApi
    :param limit: 100 pokemon max
    :param offset:0 pokemon min
    :return: the pokemon info in dictionary to get the names
    """
    url = 'https://pokeapi.co/api/v2/pokemon'

    params = {
        
        'limit' : limit,
        'offset': offset
            
    }
    #connection to the pokemon api
    resp_msg = requests.get(url,params=params)


    #checks if resquests is successful
    if resp_msg.status_code == 200:
        
        dict = resp_msg.json() #convert to dictionary 
        return [p['name']for p in dict['results']]
        
        
    else:
        print("Failed to get pokemon list.")
        print("Response code:", resp_msg.status_code)
        print(resp_msg.text)
        