#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dbsetup import Base, Trefwoord
import codecs

engine = create_engine('sqlite:///../db/main.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

with codecs.open('../data/trefwoord.csv', encoding="utf-8") as f:
    f.readline()
    lines = f.readlines()
    for line in lines:
        try:
            fields = line.strip().split(",")
            trefwoord = Trefwoord(
                trefwoordnr = fields[0],
                bloknr = fields[1],
                woord = fields[2],
                woord_zoek = fields[3],
                toevoeg = fields[4],
                spel_afk = fields[5],
                spel_afk2 = fields[6],
                uitspraak = fields[7],
                uitspraak_zoek = fields[8],
                vertaling = fields[9],
                door_verw = fields[10],
                lit_verw = fields[11],
                zie_vorige = fields[12],
                zie_volgende = fields[13]
            )
            session.add(trefwoord)
        except Exception as e:
            print str(e)
session.commit()
