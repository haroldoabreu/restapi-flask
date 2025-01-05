from mongomock import MongoClient
import os


class DevConfig:

    MONGODB_SETTINGS = {
        'db': os.getenv('MONGODB_DB'),
        'host': os.getenv('MONGODB_HOST'),
        'username': os.getenv('MONGODB_USERNAME'),
        'password': os.getenv('MONGODB_PASSWORD')
    }


class MockConfig:

    MONGODB_SETTINGS = {
        'db': 'users',
        'mongo_client_class': MongoClient
    }
