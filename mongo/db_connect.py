import configparser
from mongoengine import connect


config = configparser.ConfigParser()
config.read("config.ini") 

user = config["DB"]["username"]
pswd = config["DB"]["password"]
url = config["DB"]["url"]
db_name = config["DB"]["name"]

def db_connect():
    try:
        connect(host=f"mongodb+srv://{user}:{pswd}@{url}?retryWrites=true&w=majority", ssl=True)
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)


if __name__=="__main__":
    db_connect()