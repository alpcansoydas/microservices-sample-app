import pika
import json
from products.models import Product

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.setings")

import django
django.setup()
from django.core.management import call_command

params = pika.URLParameters("your-rabbitmq-key")

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    print('Receive in admin')
    data = json.loads(body)
    print(data)
    product = Product.objects.get(id=id)
    product.likes = product.likes + 1
    product.save()
    print('Product likes increased.')

channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print('Started Consuming')
channel.start_consuming()
channel.close()
