from peewee import Model, CharField, DateTimeField, ForeignKeyField
import os

from playhouse.db_url import connect

db = connect(os.environ.get('DATABASE_URL', 'sqlite:///my_database.db'))


class User(Model):
    name = CharField(max_length=235, unique=True)
    password = CharField(max_length=235)

    class Meta:
        database = db


class Task(Model):
    name = CharField(max_length=235)
    performed = DateTimeField(null=True)
    performed_by = ForeignKeyField(model=User, null=True)

    class Meta:
        database = db
