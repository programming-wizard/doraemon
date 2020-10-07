import pymongo
from pymongo import MongoClient
import env_file
token = env_file.get()
client = MongoClient(token['URI'])
db = client.doraemonbot
profiles = db.guild_profiles

#print(list(db.guild_profiles.find({})))


def add_guild(profile):
    profiles.insert_one(profile)


def remove_guild(guild):
    profiles.delete_one({'guild_id': guild})