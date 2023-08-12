import json
import traceback

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine("mysql://user:password@localhost/db", echo=True)
conn = engine.connect()
Base = declarative_base()


class Sample(Base):
    __tablename__ = 'SAMPLE'
    id = Column(Integer, primary_key=True)
    name = Column(String)


# Base.metadata.create_all(engine)
try:
    Session = sessionmaker(bind=engine)
    session = Session()
    session.begin()
    sample = session.query(Sample) \
        .filter(Sample.id == 1) \
        .with_for_update(nowait=True, of=Sample) \
        .one_or_none()

    sample.name = 'name3'
    session.add(sample)
    session.commit()
except Exception:
    print(traceback.format_exc())
