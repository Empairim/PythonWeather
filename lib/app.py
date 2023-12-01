from colorama import init, FOre, Back, Style
from peewee import *
from playhouse.shortcuts import model_to_dict, dict_to_model
from datetime import date


db = PostgresqlDatabase('contacts', user='titus',
                        password='1023', host='localhist', port=5432)
