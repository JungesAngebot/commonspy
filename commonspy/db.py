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


class BaseMongoConcern:
    __metaclass__ = ABCMeta

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
        self.documents = None

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

    def _collection(self):
        return self.client[self.database][self.collection]


class MongoWriteConcern(Concern, BaseMongoConcern):
    """
    This write concerns writes a document to a mongo db server. You can eather write a
    single document to the server or multiple (batch import).

    Useage: MongoWriteConcern().create_write_concern_to_server(MongoClient('localhost', 27017)).and_use_database(
    'mytestdb').and_use_collection('coll').with_document({'test': 'test'}).execute()
    """

    def __init__(self):
        super().__init__()

    def create_write_concern_to_server(self, client):
        """
        Sets the client class for later connecting to the mongo db server and finally returns itself.
        :param client: mongo db client for establishing a db connection
        :return: self
        """
        self.client = client
        return self

    def with_document(self, json_document):
        """
        Document to insert into the mongo db. This method only takes a single document.
        :param json_document: single document (dict)
        :return: self
        """
        self.document = json_document
        return self

    def with_documents(self, json_documents):
        """
        Setter method for inserting multiple documents.
        :param json_documents: multiple json documents (list of dict)
        :return: self
        """
        self.documents = json_documents
        return self

    def execute(self):
        """
        Finally executes the concern. The method checks weather it should insert a single document or multiple
        documents.
        :return: id of the inserted record
        """
        return self._collection().insert_one(
            self.document).inserted_id if self.document is not None else self._collection().insert(
            self.documents).inserted_id


class MongoReadConcern(Concern, BaseMongoConcern):
    """
    Concern for reading documents from the mongo db server. The concern supports
    both single and multi document search queries.
    """
    def __init__(self):
        """
        The concern needs to know the query and if it should search for a single document (find_one(...))
        or multiple documents(find(...)). On default the concern will search for multiple documents and
        will return a mongo cursor instance for iterating through the results.
        """
        super().__init__()
        self.document_query = None
        self.single_doc = False

    def find_only_one_document(self):
        """
        Make the concern only search for a single document.
        :return: self
        """
        self.single_doc = True
        return self

    def use_query(self, query):
        """
        Specifies the search query as dict.
        :param query: query dict
        :return: self
        """
        self.document_query = query
        return self

    def execute(self):
        return self._collection().find(self.document_query) if not self.single_doc else self._collection().find_one(
            self.document_query)
