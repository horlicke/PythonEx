__author__ = 'horlicke'

import psycopg2
import sqlite3

debug = False


### Parent portal class
class Database:
   # def __init__(self, product):
    def __init__(self, dbUser, dbHost, dbName, dpPW):
        self.dbUser = dbUser
        self.dbHost = dbHost
        self.dbName = dbName
        self.dpPW   = dpPW


        # DB = sqlite3.connect(dbName)          FOR SQLITE

        if (debug):
            print ("Opening DB connection...")
        # get a connection, if a connect cannot be made an exception will be raised here
        self.DB = psycopg2.connect(user=self.dbUser, host=self.dbHost, dbname=self.dbName, password=self.dpPW)

        self.queryPointer = self.DB.cursor()

    def connect(self):
        # get a connection, if a connect cannot be made an exception will be raised here
        self.DB = psycopg2.connect(user=self.dbUser, host=self.dbHost, dbname=self.dbName, password=self.dpPW)
        self.queryPointer = self.DB.cursor()

    def executeSQLAndCloseConnection(self, query):
        self.queryPointer.execute(query)
        response = list(self.queryPointer)           ## need to save since queryPointer go away when db is closed.
        if (debug):
            for i in self.queryPointer:
                print(i)
            print ("Closing DB connection.")
        self.DB.close()
        return response

    def executeSQL(self, query):
        self.queryPointer.execute(query)
        if (debug):
            for i in self.queryPointer:
                print(i)

    def close(self, query):
        self.DB.close()