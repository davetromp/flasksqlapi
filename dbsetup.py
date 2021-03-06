#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, String, Date, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

"""
DB is setup here. Add tables and colomns here.
"""

Base = declarative_base()

class Trefwoord(Base):
    __tablename__ = 'trefwoord'
    ID = Column(Integer, primary_key = True)
    trefwoordnr = Column(String(20), nullable = False)
    bloknr = Column(String(20), nullable = False)
    woord = Column(String(80), nullable = False) 
    woord_zoek = Column(String(80), nullable = False) 
    toevoeg = Column(String(250)) 
    spel_afk = Column(String(250)) 
    spel_afk2 = Column(String(250)) 
    uitspraak = Column(String(250)) 
    uitspraak_zoek = Column(String(250)) 
    vertaling = Column(String(250)) 
    door_verw = Column(String(250)) 
    lit_verw = Column(String(250)) 
    zie_vorige = Column(String(250)) 
    zie_volgende = Column(String(250))

engine = create_engine('sqlite:///../db/main.db')
Base.metadata.create_all(engine)
