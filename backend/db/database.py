from sqlalchemy import create_engine
#create engine buat connect ke database atau bungkus database
from sqlalchemy.orm import sessionmaker
#sessionmaker buat create session yg bisa diakses buat interaksi sama database engine
from sqlalchemy.ext.declarative import declarative_base
#declarative_base buat create base class buat model

from core.config import settings

engine = create_engine(
    settings.DATABASE_URL
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally: #finally itu kalo try ga error, finally ga error
        #finally bakal dieksekusi kalo program dimatiin
        db.close()

#create_tables berguna buat create table di database berdasarkan model yang udah didefnisikan
def create_tables():
    Base.metadata.create_all(bind=engine)