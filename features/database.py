from sqlalchemy import create_engine   
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql:///featureapp', convert_unicode=True, pool_pre_ping=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    import psycopg2
    Base.metadata.create_all(bind=engine)
    conn = psycopg2.connect(database = "featureapp")
    conn.autocommit = True
    conn.cursor()

