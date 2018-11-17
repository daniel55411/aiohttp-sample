import aiopg.sa
from sqlalchemy import (
    MetaData, Table,
    Column, Integer, String)

metadata = MetaData()

users = Table(
    'users', metadata,

    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('name', String(200), nullable=False)
)


async def init_pg(app):
    conf = app['config']['postgres']
    engine = await aiopg.sa.create_engine(
        database=conf['database'],
        user=conf['user'],
        password=conf['password'],
        host=conf['host'],
        port=conf['port']
    )
    app['db'] = engine


async def close_pg(app):
    app['db'].close()
    await app['db'].wait_closed()


async def get_users(conn, name='all'):
    query = users.select()
    if name != 'all':
        query = query.where(users.c.name == name)
    result = await conn.execute(query)

    return await result.fetchall()


async def add_user(conn, name):
    # TODO: send signal when query has executed
    query = users.insert().values(name=name)
    await conn.execute(query)
