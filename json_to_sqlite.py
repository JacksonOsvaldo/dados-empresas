#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Ler JSONS e, com base na leitura, criar tabela no db
"""
import os
import json
import zipfile as zip
import sqlite3 as sq
from os import listdir
from os.path import isfile, join

from convert_json import lendoArquivos

if __name__ == "__main__":

    lendoArquivos.lendoArquivos()
