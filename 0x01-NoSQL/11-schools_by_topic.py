#!/usr/bin/env python3
""" returns the list of school having a specific topic"""
from pymongo import MongoClient


def schools_by_topic(mongo_collection, topic):
    """
    returns the list of school having a specific topic
    """
    res = mongo_collection.find({ "topic": topic })
    return res
