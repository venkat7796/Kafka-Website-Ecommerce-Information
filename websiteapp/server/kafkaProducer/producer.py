from dotenv import load_dotenv
from kafka import KafkaProducer
import json
from json import dumps
import os


load_dotenv()

def kafkaProduce(topic,message):
    aws_ec2 = os.getenv("AWS_EC2")
    producer = KafkaProducer(bootstrap_servers=[aws_ec2],
                            value_serializer=lambda x: json.dumps(x).encode('utf-8'))
    if topic == "user_info":
        payload = {'ecommerce_customers': message}
        producer.send('ecommerce_customers',value=payload)
        producer.flush()
    elif topic == "product_info":
        payload = {'ecommerce_products': message}
        producer.send('ecommerce_products',value=payload)
        producer.flush()

def consume_user_info(message):
    kafkaProduce("user_info",message)
    

def consumer_product_info(message):
    kafkaProduce("product_info",message)

