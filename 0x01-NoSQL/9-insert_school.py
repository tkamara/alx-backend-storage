#!/usr/bin/env python
"""inserts a new document in a collection based on kwargs"""
from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """
    inserts a new document in a collection based on kwargs
    """
    mongo_collection.insert_one(kwargs)
