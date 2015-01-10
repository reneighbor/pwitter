from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
tweet = Table('tweet', pre_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('date_created', DateTime),
    Column('body', String),
    Column('user_id', Integer),
)

user = Table('user', pre_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('username', String),
    Column('token', String),
    Column('date_created', DateTime),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['tweet'].drop()
    pre_meta.tables['user'].drop()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['tweet'].create()
    pre_meta.tables['user'].create()
