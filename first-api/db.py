from peewee import *
from dotenv import load_dotenv
import os

load_dotenv()

PASSWORD = os.getenv('PASSWORD')

database = MySQLDatabase(
    'fastapi',
    user='root', password=PASSWORD,
    host='localhost',
    port=3306
)

class User(Model):
    username = CharField(max_length=50)
    email = CharField(max_length=50)

    def __str__(self):
        return self.username

    class Meta:
        database = database
        table_name = 'users'
