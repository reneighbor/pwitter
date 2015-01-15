from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
tweet = Table('tweet', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('date_created', DateTime),
    Column('date_updated', DateTime),
    Column('body', String(length=140)),
    Column('user_id', Integer),
)

user = Table('user', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('date_created', DateTime),
    Column('date_updated', DateTime),
    Column('username', String(length=64)),
    Column('user_sid', String(length=16)),
    Column('hashed_token', String(length=16)),
)

broadcaster2_follower = Table('broadcaster2_follower', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('date_created', DateTime),
    Column('date_updated', DateTime),
    Column('broadcaster_id', Integer),
    Column('follower_id', Integer),
    Column('active', Boolean, default=ColumnDefault(True)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['tweet'].columns['date_updated'].create()
    post_meta.tables['user'].columns['date_updated'].create()
    post_meta.tables['broadcaster2_follower'].columns['date_updated'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['tweet'].columns['date_updated'].drop()
    post_meta.tables['user'].columns['date_updated'].drop()
    post_meta.tables['broadcaster2_follower'].columns['date_updated'].drop()
