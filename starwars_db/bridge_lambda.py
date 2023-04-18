"""bridge lambda"""
import json
import logging
import boto3

# Creating a logger object
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context=None):
    """lambda function to add message to starwars_queue"""
    # Creating an AWS SQS client
    sqs_client = boto3.client("sqs")

    sqs_url = "https://sqs.ap-northeast-1.amazonaws.com/232363089347/starwars_queue"

    post_data = json.dumps(event["detail"])

    # Logging the post data
    logger.info(f"Received data: {post_data}")

    response = sqs_client.send_message(QueueUrl=sqs_url, MessageBody=post_data)

    response_code = response["ResponseMetadata"]["HTTPStatusCode"]

    logger.info(response_code)
    if response_code == 200:
        message = "Successfully added to queue"
    else:
        message = "Error in adding data to SQS"
        # Logging the error message
        logger.error(message)

    return {
        "StatusCode": response_code,
        "Message": message,
    }
