from peewee import (Model, CharField, TextField, IdentityField, BooleanField,
                    TimestampField, ForeignKeyField)
from peewee import PostgresqlDatabase
import os
from dotenv import load_dotenv
load_dotenv()


dbname = os.environ.get('dbname')
user = os.environ.get('user')
password = os.environ.get('password')
host = os.environ.get('host')
port = os.environ.get('port')

db = PostgresqlDatabase(dbname, user=user, password=password,
                        host=host, port=port)


class Package(Model):
    id = IdentityField()
    name = TextField()
    title = TextField()
    version = CharField(max_length=120)
    notes = TextField()
    author = TextField()
    author_email = TextField()
    maintainer = TextField()
    url = TextField()
    maintainer_email = TextField()
    state = TextField()
    license_id = TextField()
    type = TextField()
    owner_org = TextField()
    private = BooleanField(default=False)
    metadata_modified = TimestampField()
    creator_user_id = TextField()
    metadata_created = TimestampField()

    class Meta:
        database = db


class Package_extra(Model):
    id = IdentityField()
    key = TextField()
    value = TextField()
    state = TextField()
    package_id = ForeignKeyField(Package, backref='packages_extras', on_delete='RESTRICT')

    class Meta:
        database = db
