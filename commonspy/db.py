from abc import ABCMeta, abstractmethod


"""
Module for database connections. This module contains helper classes and mechanims for easy db access.
"""


class Concern:
    """
    Base class for all concerns according to database connections.
    A concern could be:
    - a write concern to insert data into the database
    - a read concern to read data from the database
    - a update concern to update data in the database
    - a delete concern to delete data in the databse
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def execute(self):
        """
        Every concern must be 'executable'. So this method must be implemented and
        should execute the required logic to read, write, update delete data
        in the database.
        :return: id of the record processed
        """
        pass


class MongoWriteConcern(Concern):
    """
    This write concerns writes a document to a mongo db server. You can eather write a
    single document to the server or multiple (batch import).

    Useage: MongoWriteConcern().create_write_concern_to_server(MongoClient('localhost', 27017)).and_use_database(
    'mytestdb').and_use_collection('coll').with_document({'test': 'test'}).execute()
    """
    def __init__(self):
        """
        The constructor sets the basic members of the concern that are required to actual persist data.
        The client is a mongo db client instance used to connect to the mongo db server. The
        database is the name of the database that should be used for persistance. The collection is the
        name of the collection that should be used and finally the document / documents are the data
        that should be persisted.
        """
        self.client = None
        self.database = None
        self.collection = None
        self.document = None

    def create_write_concern_to_server(self, client):
        """
        Sets the client class for later connecting to the mongo db server and finally returns itself.
        :param client: mongo db client for establishing a db connection
        :return: self
        """
        self.client = client
        return self

    def and_use_database(self, database_name):
        """
        Name of the database the client should use as string.
        :param database_name: name of the database as string
        :return: self
        """
        self.database = database_name
        return self

    def and_use_collection(self, collection_name):
        """
        Name of the collection that the client should use.
        :param collection_name: collection to use as string
        :return: self
        """
        self.collection = collection_name
        return self

    def with_document(self, json_document):
        """
        Document to insert into the mongo db. This method only takes a single document.
        :param json_document: single document (dict)
        :return: self
        """
        self.document = json_document
        return self

    def execute(self): return self.client[self.database][self.collection].insert_one(self.document).inserted_id
