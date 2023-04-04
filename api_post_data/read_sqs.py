import boto3
import json

sqs_client = boto3.client("sqs")

queue_url = "https://sqs.ap-northeast-1.amazonaws.com/232363089347/StarWarsQueue"


valid_url = "https://sqs.ap-northeast-1.amazonaws.com/232363089347/ValidQueue"
invalid_url = "https://sqs.ap-northeast-1.amazonaws.com/232363089347/InvalidQueue"


def lambda_handler(event, context):
    try:
        message = json.loads(event["Records"][0]["body"])

        if "name" not in message:
            raise BaseException("Missing fields")

        else:
            print("Valid Data")
            sqs_client.send_message(QueueUrl=valid_url, MessageBody=message)

    except Exception as error_message:
        print("There are no messages available")

    return
