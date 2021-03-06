#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dbsetup import Base, Trefwoord
import json

"""
all queries will be implemented here. basically we want to be able to query
every colomn seperately and do one query on the entire db, which may be expensive.
however the db is very small and readonly.
"""

engine = create_engine('sqlite:///../db/main.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind = engine)

session = DBSession()

def queryVertalingContains(q):
    ids = []
    rows = session.query(Trefwoord.ID,Trefwoord.vertaling).filter(Trefwoord.vertaling.contains(q)).order_by(Trefwoord.ID).all()
    for row in rows:
        ids.append(row.ID)
    return ids

def queryWoordZoekContains(q):
    ids = []
    rows = session.query(Trefwoord.ID,Trefwoord.woord_zoek).filter(Trefwoord.woord_zoek.contains(q)).order_by(Trefwoord.ID).all()
    for row in rows:
        ids.append(row.ID)
    return ids

def queryAllContains(q):
    ids = queryWoordZoekContains(q) + queryVertalingContains(q)
    unduppedIds = []
    for i in ids:
        if i not in unduppedIds:
            unduppedIds.append(i)
    sortedIds = sorted(unduppedIds)
    return sortedIds

def queryID(q):
    row = session.query(Trefwoord).filter(Trefwoord.ID==q).one()
    d = {}
    for column in row.__table__.columns:
        d[column.name] = getattr(row, column.name)
    return d
    #return json.dumps(d)
  
#q=u"אבאיע"
#print queryID("1")
