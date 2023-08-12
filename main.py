import json
import traceback

from sqlalchemy import create_engine, and_
from sqlalchemy import Table, Column, Integer, String, MetaData, Row


def convert(sampleEntity: Row) -> dict:
    return {
        "id": sampleEntity.id,
        "name": sampleEntity.name
    }


engine = create_engine("mysql://user:password@localhost/db", echo=True)

conn = engine.connect()
meta = MetaData()

sample = Table(
    'SAMPLE', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String),
)

try:

    conn.begin()

    query = sample.select().filter(Column('id', Integer) == 1).with_for_update(nowait=True)
    results = conn.execute(query)
    o = results.one()
    o.name = 'nameee'

    sampleById = {result.id: convert(result) for result in results}
    responseRoot = {"root": sampleById}

    responseJson = json.dumps(responseRoot, indent=2)
    print(responseJson)

    conn.commit()
except Exception:
    print(traceback.format_exc())
