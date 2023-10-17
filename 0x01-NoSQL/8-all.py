#!/usr/bin/env python3
"""lists all documents in a collection"""
from pymongo import MongoClient


def list_all(mongo_collection):
    """
    lists all documents in a collection
    """
    res = mongo_collection.find()
    if (res == 0):
        return []
    return res
