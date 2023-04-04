import requests
from read_data import *

def get_cast_details(api_url, bucket_name, file_name):

    data = requests.get(api_url)
    movies_data = data.json()["results"]

    cast_data = read_data(bucket_name, file_name)
    
    #return cast_data
    
    result_json = {}

    for movie in movies_data:

        title = movie['title']
        character_list = movie["characters"]

        characters = []

        for character in character_list:

            name = cast_data[character]

            characters.append(name)

        result_json[title] = characters

    return result_json
