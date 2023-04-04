import json
from get_cast_details import *

def lambda_handler(event, context):
    
    
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    file_name = event['Records'][0]['s3']['object']['key']
    
    api_url = "https://swapi.dev/api/films/"
    
    result_json = get_cast_details(api_url, bucket_name, file_name)

    return result_json
    
#lambda_handler(1,2)
