from sqlalchemy import (
    MetaData, Table, Column, Integer, String
)
from migrate import *

metadata = MetaData()

users = Table(
    'users', metadata,

    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String(200), nullable=False)
)


def upgrade(migrate_engine):
    metadata.bind = migrate_engine
    users.create()


def downgrade(migrate_engine):
    raise NotImplementedError
