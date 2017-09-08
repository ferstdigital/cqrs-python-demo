from __future__ import print_function
from sqlalchemy import Column, Integer, String, DateTime, Text, ARRAY, Float
from apps.database import Base

class Account(Base):
    __tablename__ = 'accounts'
    id = Column(Integer, primary_key=True)
    balance = Column(Float(), default=0)
    sequence = Column(Integer, default=-1)

    def __init__(self, *kwargs):
        for key in kwargs[0]:
            setattr(self, key, kwargs[0][key])

    def __repr__(self):
        return '<Account %r>' % (self.id)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}