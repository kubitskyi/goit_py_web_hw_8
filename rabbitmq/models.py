import random
from mongoengine import Document
from mongoengine.fields import StringField, EmailField, BooleanField
from faker import Faker
from db_connect import db_connect


class Contact(Document):
    meta = {'collection': 'contacts'}
    fullname = StringField()
    email = EmailField()
    phone = StringField()
    email_or_sms = StringField(default = "email")     # if email - True, if sms - False
    message_is_send = BooleanField(default = False)   # True or False



fake = Faker()
def complete_db():
    for _ in range(50):
        try:
            new_contact = Contact(
                fullname = fake.name(),
                email = fake.email(),
                phone = fake.phone_number(),
                email_or_sms = random.choice(["email","sms"])
            )
            new_contact.save()
        except Exception as e:
            print(e)
    print("You successfully completed to contacts!")

if __name__ == "__main__":
    db_connect()
    complete_db()