import boto3
import json

sqs_client = boto3.client("sqs")


valid_url = "https://sqs.ap-northeast-1.amazonaws.com/232363089347/ValidQueue"


def lambda_handler(event, context):
    try:
        message = json.loads(event["Records"][0]["body"])

        # to check whether the required fields are present or not
        check_requirements = [
            "version" in message,
            "id" in message,
            "source" in message,
            "detail" in message,
        ]

        print(check_requirements)

        if not all(check_requirements):
            raise BaseException("Missing fileds in the given data")

        else:
            print("Valid Data")
            response = sqs_client.send_message(
                QueueUrl=valid_url, MessageBody=json.dumps(message)
            )

    except Exception as error_message:
        print("There are no messages available")

    # return
