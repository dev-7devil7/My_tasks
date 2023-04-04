import requests
import json
import boto3


api_url = "https://swapi.dev/api/people/"

#No of characters = 83
character_count = 83

#Creating s3 client to access S3 data
s3_client = boto3.client("s3")

#new file name to write data to
file_name = "movie_cast.json"

#Name of the bucket in s3
bucket = "star-wars-buckets"

#Empty dictionary to write cast details
cast_details = {}


def read_and_dump_to_json():

    for character_index in range(1, character_count+1):
    
        cast_api = api_url + str(character_index) + "/"
    
        data = requests.get(cast_api)
        json_data = data.json()
    
        if "name" not in json_data:
            continue
    
        cast_name = json_data["name"]
    
        cast_details[cast_api] = cast_name
    
    # Serializing json
    #json_object = json.dumps(cast_details, indent=4)
    
    bianry_stream = bytes(json.dumps(cast_details).encode("UTF-8"))
    
    s3_client.put_object(Bucket = bucket, Key = file_name, Body = bianry_stream)
    
    return "Success"