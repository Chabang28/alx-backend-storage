#!/usr/bin/env python3
"""A function that changes all topics of a school document based on the name"""


def update_topics(mongo_collection, name, topics):
    """ Changes all topics of a school document based on the name
     Arguments
        mongo_collection: pymongo collection object
        name: The school to update (key)
        topics: The list of topics approached in the school (value)
    """

    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
