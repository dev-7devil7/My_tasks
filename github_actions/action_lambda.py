import json


def lambda_handler(event, context):
    message = "Hello there! This is a samaple test lamdba for github actions"

    return {"statusCode": 200, "body": json.dumps(message)}
