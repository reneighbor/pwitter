from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
tweet = Table('tweet', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('date_created', DateTime),
    Column('body', String(length=140)),
    Column('user_id', Integer),
)

user = Table('user', pre_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('username', String),
    Column('userid', String),
    Column('token', String),
)

user = Table('user', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('date_created', DateTime),
    Column('username', String(length=64)),
    Column('token', String(length=64)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['tweet'].create()
    pre_meta.tables['user'].columns['userid'].drop()
    post_meta.tables['user'].columns['date_created'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['tweet'].drop()
    pre_meta.tables['user'].columns['userid'].create()
    post_meta.tables['user'].columns['date_created'].drop()
