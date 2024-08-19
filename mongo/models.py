from mongoengine import Document, CASCADE
from mongoengine.fields import ListField, StringField, ReferenceField


class Author(Document):
    meta = {'collection': 'authors'}
    fullname = StringField()
    born_date = StringField()
    born_location = StringField()
    description = StringField()

class Quote(Document):
    meta = {'collection': 'quotes', 'allow_inheritance': True}
    owner = ReferenceField('Author', reverse_delete_rule=CASCADE)
    tags = ListField(StringField(max_length=50))
    quote = StringField()