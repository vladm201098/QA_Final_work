import json

with open('/home/vladislav/QA_Final_work/helpers/api.json',
          'r') as file:
    object = json.load(file)


def user_creation():
    return object[0]


def pet_creation():
    return object[1]


def update_pet_name():
    return object[2]