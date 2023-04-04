import boto3
import json

sqs_client = boto3.client("sqs")
dynamodb = boto3.client("dynamodb")
table_name = "star-wars"


def convert_data(message):
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
            raise BaseException("Missing fileds in the given data")

        else:
            print("Valid Data")

            # converting json data to dynamodb required format
            message = convert_data(message)
            response = dynamodb.put_item(TableName=table_name, Item=message)

    except Exception as error_message:
        print("There are no messages available")

    # return
