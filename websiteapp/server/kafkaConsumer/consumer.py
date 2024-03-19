from kafka import KafkaConsumer
from json import dumps, loads
import json
import boto3
import os
from datetime import datetime
from dotenv import load_dotenv

def consume_messages_kafka():
    load_dotenv()
    aws_ec2 = os.getenv("AWS_EC2")
    userInfo = KafkaConsumer(
        'ecommerce_customers',
        bootstrap_servers=[aws_ec2],
        value_deserializer=lambda x: loads(x.decode('utf-8'))
    )

    aws_access_key= os.getenv("AWS_ACCESS_KEY")
    aws_secret_key= os.getenv("AWS_SECRET_KEY")
    aws_region = os.getenv("AWS_REGION")
    aws_bucket = os.getenv("AWS_BUCKET")

    s3 = boto3.client(
        's3',
        aws_access_key_id=aws_access_key,
        aws_secret_access_key=aws_secret_key,
        region_name=aws_region
    )
    print(aws_bucket)
    for count, values in enumerate(userInfo):
        print(values.value)
        json_data = json.dumps(values.value)
        file_name = "ecommerce_customers_" + str(count) + "_" + str(datetime.now().date())
        s3.put_object(Body=json_data,Bucket=aws_bucket,Key=f'ecommerce_customers/{file_name}.json')

    productInfo = KafkaConsumer(
        'ecommerce_products',
        bootstrap_servers=[aws_ec2],
        value_deserializer=lambda x: loads(x.decode('utf-8'))
    )

    for count, values in enumerate(productInfo):
        print(values.value)
        json_data = json.dumps(values.value)
        file_name = "ecommerce_products_" + str(count) + "_" + str(datetime.now().date())
        s3.put_object(Body=json_data,Bucket=aws_bucket,Key=f'ecommerce_products/{file_name}.json')

if __name__ == "__main__":
    consume_messages_kafka()