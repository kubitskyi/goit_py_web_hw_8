import pika
from bson import ObjectId
from db_connect import db_connect
from models import Contact


def callback(body):
    id =  body.decode("utf-8")
    contact = Contact.objects().get(id = ObjectId(id))
    print(f" [x] Email send to {contact.fullname}")
    contact.message_is_send = True
    contact.save()


def main():
    db_connect()
    credentials = pika.PlainCredentials('admin', '12345')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost', port=8080, credentials=credentials)
    )
    channel = connection.channel()

    channel.queue_declare(queue='email', durable=False)
    channel.basic_consume(queue='email', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    main()