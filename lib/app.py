from colorama import init, Fore, Back, Style
from peewee import *
from playhouse.shortcuts import model_to_dict, dict_to_model
from datetime import date


db = PostgresqlDatabase('contacts', user='titus',
                        password='1023', host='localhost', port=5432)


class ContactModel(Model):
    class Meta:
        database = db


class Contact(ContactModel):
    first_name = CharField()
    last_name = CharField()
    phone_number = CharField()


db.connect()
db.create_tables([ContactModel])
db.close()


first_name = input(" Enter the first name!")
last_name = input(" Enter the last name!")
phone_number = input(" Enter the phone number!")

contact = Contact.create(first_name=first_name,
                         last_name=last_name, phone_number=phone_number)
contact.save()

print(Fore.GREEN + "Data saved and created successfully!" + Fore.RESET)

contacts = Contact.select()
