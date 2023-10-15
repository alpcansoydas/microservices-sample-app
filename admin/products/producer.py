import pika, json

params = pika.URLParameters("amqps://xrptvbev:rm30Oy1-faBybWxGEF2H9tRDa36giNso@stingray.rmq.cloudamqp.com/xrptvbev")

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)
