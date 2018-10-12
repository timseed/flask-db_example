#!/usr/bin/env python

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

DB_URI = 'sqlite:///./main.db'
Base = declarative_base()

class Note(Base):
    __tablename__ = 'notes'

    id = Column(Integer, primary_key=True)
    title = Column(String(80))
    description = Column(String(80))
    create_at = Column(String(80))
    create_by = Column(String(80))
    priority = Column(Integer)

if __name__ == "__main__":
    from sqlalchemy import create_engine

    engine = create_engine(DB_URI)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)