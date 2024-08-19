from models import Author, Quote
from db_connect import db_connect


def find_by_name(name):
    authors = Author.objects.filter(fullname__icontains=name.strip())
    if len(authors) == 0:
         return "Author not found!"
    quotes = []
    quotes.extend(Quote.objects(owner__in=authors))
    if len(quotes) == 0:
        return "Quotes not found!"
    return  "\n".join([f"{quote.quote} - {quote.owner.fullname}" for quote in quotes])


def find_by_tag(tag):
    quotes = Quote.objects.filter(tags__icontains=tag.strip())
    if len(quotes) == 0:
        return "Quotes not found!"
    # tags = ", ".join(["#" + tag for tag in quote.tags])
    return  "\n".join([f"{quote.quote} - {quote.owner.fullname}\n-- Tags: {", ".join(quote.tags)}\n" for quote in quotes])


def find_by_tags(tags):
    tags_list = [tag.strip() for tag in tags.split(",")]
    quotes = Quote.objects.filter(tags__in=tags_list)
    if len(quotes) == 0:
        return "Quotes not found!"
    return "\n".join([f"{quote.quote} - {quote.owner.fullname}\n-- Tags: {", ".join(quote.tags)}\n" for quote in quotes])


def main():
    db_connect()
    while True:
        try:
            cmd = input(">>>")
            action, query = cmd.strip().split(":")
            if query == None:
                print("A search query is required!")
                break
            else:
                query == query.strip()
        except ValueError:
            print("Please enter in the format - command:query\nExamples:\nname: Steve Martin\ntags:life,live ")
            continue


        match action.strip():
            case 'name':
                result = find_by_name(query)
            case 'tag':
                result = find_by_tag(query)
            case 'tags':
                result = find_by_tags(query)
            case 'exit':
                break
            case _ :
                result = "Unknown command!"

        print(result)
if __name__=="__main__":
    main()