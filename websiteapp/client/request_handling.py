import requests
from faker import Faker
import random
from datetime import datetime

BASE_URL = "http://127.0.0.1:5000"
def generate_customer(fake):
    current_date = datetime.now().date()
    iso_formatted_date = current_date.isoformat()
    customer = {
        "customer_id": fake.uuid4(),
        "name": fake.name(),
        "email": fake.email(),
        "address": fake.address(),
        "age": random.randint(18, 70),
        "gender": random.choice(["Male", "Female", "Other"]),
        "created_date": fake.past_date().isoformat(),
        "last_login": iso_formatted_date
    }
    print(customer)
    return customer

def generate_product(fake):
    categories = ['Electronics', 'Books', 'Clothing', 'Home & Garden']
    product = {
        "product_id": fake.uuid4(),
        "name": fake.word().title(),
        "category": random.choice(categories),
        "price": round(random.uniform(10, 500), 2),
        "quantity": random.randint(0, 100),
        "supplier": fake.company()
    }
    print(product)
    return product
fake = Faker()
for i in range(10):
    if random.random() < 0.5:
        cus_data = generate_customer(fake)
        response = requests.post(BASE_URL + "/api/v1/customer",json=cus_data)
        print(response.json())
    else:
        prd_data = generate_product(fake)
        response = requests.post(BASE_URL + "/api/v1/product",json=prd_data)
        print(response.json())
