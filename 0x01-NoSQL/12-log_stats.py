#!/usr/bin/env python3
"""provides some stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient

def counter(nginx_col):
    """counting no. of documents"""
    num = nginx_col.count_documents({})
    return num

def counter_get(nginx_col):
    """counting logs for GET"""
    get = nginx_col.count_documents({"method": "GET"})
    return get

def counter_post(nginx_col):
    """counting logs for POST"""
    post = nginx_col.count_documents({"method": "POST"})
    return post

def counter_put(nginx_col):
    """counting logs for PUT"""
    put = nginx_col.count_documents({"method": "PUT"})
    return put

def counter_patch(nginx_col):
    """counting logs for PATCH"""
    patch = nginx_col.count_documents({"method": "PATCH"})
    return patch

def counter_delete(nginx_col):
    """counting deleted logs"""
    deleted = nginx_col.count_documents({"method": "DELETE"})
    return deleted

def status_check(nginx_col):
    """returning status check"""
    stats = nginx_col.count_documents({"method": "GET", "path": "/status"})
    return stats

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    # obtaining number of documents
    print("{} logs".format(counter(nginx_collection)))
    print("Methods:")
    print("\tmethod GET: {}".format(counter_get(nginx_collection)))
    print("\tmethod POST: {}".format(counter_post(nginx_collection)))
    print("\tmethod PUT: {}".format(counter_put(nginx_collection)))
    print("\tmethod PATCH: {}".format(counter_patch(nginx_collection)))
    print("\tmethod DELETE: {}".format(counter_delete(nginx_collection)))
    print("{} status check".format(status_check(nginx_collection)))
