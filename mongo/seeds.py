import json
from db_connect import db_connect
from models import Author, Quote

def add_authors():
    with open('authors.json', 'r', encoding='utf-8') as file:
        authors = json.load(file)

        for author in authors:
            try:
                new_author = Author(
                    fullname = author['fullname'],
                    born_date = author['born_date'],
                    born_location = author['born_location'],
                    description = author['description']
                )
                new_author.save()
            except Exception as e:
                print(e)
        print("You successfully connected to authors!")

def add_quotes():
    with open('quotes.json', 'r', encoding='utf-8') as file:
        quotes = json.load(file)

        for quote in quotes:
            try:
                author = Author.objects(fullname=quote['author']).first()
                if not author:
                    author = Author(fullname = quote['author'])

                new_quote = Quote(
                    owner = author,
                    tags = quote['tags'],
                    quote = quote['quote']
                )
                new_quote.save()
            except Exception as e:
                print(e)
        print("You successfully connected to quotes!")




if __name__=='__main__':
    db_connect()
    add_authors()
    add_quotes()