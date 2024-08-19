import time
import pika
from db_connect import db_connect
from models import Contact, complete_db


credentials = pika.PlainCredentials('admin', 'k12345')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', port=8080, credentials=credentials)
)

channel = connection.channel()
channel.exchange_declare(exchange='message_sendler', exchange_type='topic')

channel.queue_declare(queue='sms', durable=False)
channel.queue_bind(exchange='message_sendler', queue='sms', routing_key="send.sms")

channel.queue_declare(queue='email', durable=False)
channel.queue_bind(exchange='message_sendler', queue='email', routing_key="send.email")

def main():
    db_connect()
    complete_db()
    all_contacts = Contact.objects.all()
    for contact in  all_contacts:
        if contact.message_is_send:
            continue
        else:
            if contact.email_or_sms == "email":
                routing_key = "send.email"
            else:
                routing_key = "send.sms"

            message = str(contact.id)
            channel.basic_publish(
                exchange='message_sendler',
                routing_key=routing_key,
                body=message,
                properties=pika.BasicProperties(
                    delivery_mode=pika.spec.TRANSIENT_DELIVERY_MODE
                )
            )

            time.sleep(1)
            print(" [x] Sent %r" % message)


    connection.close()


if __name__ == '__main__':
    main()
