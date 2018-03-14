import pika
from config import Config

cfg = Config()

class MQManager:

    def __init__(self, local_queue):
        self.local_queue = local_queue
        credentials = pika.PlainCredentials('nois', 'odorico')
        self.params = pika.ConnectionParameters(cfg.mq_machine_ip,
                                                cfg.mq_machine_port,
                                                '/', credentials)

    def callback(self, ch, method, properties, body):
        self.local_queue.put(body)

    def subscribeTo(self, queue_name):
        connection = pika.BlockingConnection(self.params)
        channel = connection.channel()
        channel.queue_declare(queue=queue_name)
        channel.basic_consume(self.callback,
                                   queue=queue_name,
                                   no_ack=True)
        channel.start_consuming()

    def publishIn(self, queue_name):
        connection = pika.BlockingConnection(self.params)
        channel = connection.channel()
        while True:
            body = self.local_queue.get()
            channel.queue_declare(queue=queue_name)
            channel.basic_publish(exchange='',
                                  routing_key=queue_name,
                                  body=body)
        connection.close()
