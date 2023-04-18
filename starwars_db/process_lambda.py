"""Process lambda"""
import json
import logging
import boto3


# Configure the root logger
logging.basicConfig(level=logging.INFO)

sqs_client = boto3.client("sqs")
dynamodb = boto3.client("dynamodb")
TABLE_NAME = "star-wars"


def convert_data(message):
    """convert the json data to dynamodb required format"""
    formated_message = {}

    for key, value in message.items():
        if isinstance(value, str):
            formated_message[key] = {"S": value}

        elif isinstance(value, int):
            formated_message[key] = {"N": str(value)}

        elif isinstance(value, list):
            formated_message[key] = {"SS": value}

    return formated_message


def lambda_handler(event, context):
    """Lambda function to process starwars_queue data"""
    try:
        message = json.loads(event["Records"][0]["body"])

        # to check whether the required fields are present or not
        check_requirements = [
            "title" in message,
            "release_date" in message,
            "characters" in message,
            "url" in message,
        ]

        if not all(check_requirements):
            error_message = "Missing fields in the given data"
            logging.error(error_message)
            raise BaseException(error_message)

        logging.info("Valid Data")

        # converting json data to dynamodb required format
        message = convert_data(message)
        response = dynamodb.put_item(TableName=TABLE_NAME, Item=message)

    except Exception as error_message:
        logging.error(f"An error occurred: {error_message}")
