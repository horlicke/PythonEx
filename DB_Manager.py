__author__ = 'horlicke'

import psycopg2
import sqlite3
import pypyodbc

debug = True


### Parent portal class
class Database:
   # def __init__(self, product):
    def __init__(self, dbUser, dbHost, dbName, dbPW, dbSQL_DBMS):
        """

        :type self: object
        """
        self.dbUser = dbUser
        self.dbHost = dbHost
        self.dbName = dbName
        self.dbPW   = dbPW
        self.dbSQL_DBMS = dbSQL_DBMS
        self.connection_string = "Driver={SQL Server}; Server="+self.dbHost+";Database="+self.dbName+";uid="+self.dbUser+";pwd="+self.dbPW
        self.connection_string = "Driver={"+self.dbSQL_DBMS+"}; Server="+self.dbHost+";Database="+self.dbName+";uid="+self.dbUser+";pwd="+self.dbPW

        # DB = sqlite3.connect(dbName)          FOR SQLITE

        if (debug):
            print ("Opening DB connection...")
            print ("Connection String: " + self.connection_string)
            print("User: %s, Host: %s, DB Name %s, DB PW: %s", dbUser, dbHost, dbName, dbPW)

        self.DB = pypyodbc.connect(self.connection_string)

        self.queryPointer = self.DB.cursor()

    def connect(self):
        # get a connection, if a connect cannot be made an exception will be raised here
        #self.DB = psycopg2.connect(user=self.dbUser, host=self.dbHost, dbname=self.dbName, password=self.dbPW)
        self.DB = pypyodbc.connect(self.connection_string)
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
        response = list(self.queryPointer)
        if (debug):
            for i in self.queryPointer:
                print(i)
        return response

    def close(self):
        self.DB.close()