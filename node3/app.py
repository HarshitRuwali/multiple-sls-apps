import pandas as pd
import boto3
import json


def lambda_handler(event, context):
    try:
        print("event", event)
        print("context", context)

        bucket_name = event['Records'][0]['s3']['bucket']['name']
        object_key = event['Records'][0]['s3']['object']['key']

        print("bucket_name", bucket_name)
        print("object_key", object_key)

        s3 = boto3.client('s3')
        csv_obj = s3.get_object(Bucket=bucket_name, Key=object_key)
        # csv_file = csv_obj['Body'].read().decode('utf-8')
        json_converted_file = json.loads(pd.read_csv(
            csv_obj['Body']).to_json(orient='records'))
        sqs = boto3.client('sqs')
        file_length = len(json_converted_file)
        for i in range(0, file_length, 10):
            message_batch = [{
                'Id': str(message['id']),
                'MessageBody': str(message)
            } for message in json_converted_file[i:i+10]]
            print("message_batch", message_batch)
            sqs.send_message_batch(
                QueueUrl="https://sqs.ap-south-1.amazonaws.com/247620070542/notification-poc", Entries=message_batch)
        return {"statusCode": 200, "body": json_converted_file}
    except Exception as e:
        print("Exception", e)
        return {"statusCode": 500}