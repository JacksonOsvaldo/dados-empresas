#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pymongo import MongoClient

client = MongoClient(
    'mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&ssl=false')

filter = {'message': {'$eq': 'Server Error'}}

result = client['dados']['empresas'].find(filter=filter)

a = 0

for i in result:

    a += 1

    client['dados']['empresas'].delete_one(i)

client.close()

print('Arquivos removidos: ', a)
