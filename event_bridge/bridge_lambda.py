import json
import boto3


def lambda_handler(event, content):
    # creating an aws sqs clinet
    sqs_client = boto3.client("sqs")

    sqs_url = "https://sqs.ap-northeast-1.amazonaws.com/232363089347/StarWarsQueue"

    post_data = json.dumps(event["detail"])

    print(post_data)

    response = sqs_client.send_message(QueueUrl=sqs_url, MessageBody=post_data)

    response_code = response["ResponseMetadata"]["HTTPStatusCode"]

    if response_code == 200:
        message = "Succesfully added to queue"
    else:
        message = "Error in addding data to SQS"

    return {
        "StatusCode": response_code,
        "Message": message,
    }
