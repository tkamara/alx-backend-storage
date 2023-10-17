#!/usr/bin/env python3
""" changes all topics of a school document based on the name"""
from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):
    """
    changes all topics of a school document based on the name
    """
    mykey = { "name": name }
    new = { "$set": { "topics": topics }}
    mongo_collection.update_many(mykey, new)
