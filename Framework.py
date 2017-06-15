__author__ = 'horlicke'


import Results
import DB_Manager
#TCP Client script
import socket
import WebPortal
import urllib.request
import requests
import json
import Testdata
import time
from pprint import pprint



debug = False
verbose = True

##############################################################################################
#  Framework class
#
#
##############################################################################################
class FW:

    def __init__(self, testRunId, browser):
        # generic data
        self.testRunId = testRunId
        self.browser = browser
        self.product = "MedNx"               #hard  code  for now

        #assign test data based on product
        if (self.product == "MedNx"):
            self.testdata = Testdata.MedNx_Testdata
        elif (self.product == "PPro"):
            self.testdata =  Testdata.PPro_Testdata
        else:
            return Testdata.PPro_Testdata

        self.resultsObj  = Results.ResultManager(self.testRunId, self.testdata.TEST_RAIL_URL, self.testdata.TEST_RAIL_USER, self.testdata.TEST_RAIL_PW )

    def getProductTestData(self):      #specific data for product
        return self.testdata

    def sleep(self, delay):
        time.sleep(delay)


##############################################################################################
#  Database/sql methods
#
#
##############################################################################################
    def connectToDB(self, dbUser, dbHost, dbName, dbPW):
        self.dbInstance = DB_Manager.Database(dbUser, dbHost, dbName, dbPW, "SQL Server")   #hardcoded for SQL Server dbms for now, fix in future

    def sqlQuery(self, query):
        return self.dbInstance.executeSQL(query)

    def sqlQueryAndCloseConnection(self, query):
        return self.dbInstance.executeSQLAndCloseConnection(query)   #return response to query

    def closeDBConnection(self):
        self.dbInstance.close()
    ##########    End database/sql methods

##############################################################################################
#  assignPortalAndBrowser()
#
#
##############################################################################################
    def assignPortalAndBrowser(self, url):
        if self.browser != "NONE":
            if(self.product == "MedNx"):
                return WebPortal.MedNx_Portal(self.browser, self.product, url)
            elif (self.product == "PPro"):
                return WebPortal.PPro_Portal(self.browser, self.product, url)
            else: #default to MedNx locators
                return WebPortal.MedNx_Portal(self.browser, self.product, url)
##############################################################################################
#  assignEyeballs()
#     Used for interfacing with Applitools visual web page comparison tool
#
##############################################################################################
    def assignEyeballs(self):
        return WebPortal.Eyeballs()

##############################################################################################
#  TCP Methods
#
#
##############################################################################################
    #TCP methods
    def TCPCreateAndSendMessageAndGetResponse(self, message, serverHost, serverPort):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((serverHost, serverPort))

        #now send http request
        try:
            if (debug):
               print ("TCPCreateAndSendMessageAndGetResponse::Send message")
            client.send(message.encode())

        finally:
            if (debug):
                print("Get response...")
            response=client.recv(4096).decode()
            if (debug):
                print (response)
            client.close()
        return response

    def TCPSendMessage(self, message, serverHost, serverPort):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((serverHost, serverPort))

        #now send TCP
        try:
            print ("Send message")
            client.send(message.encode())

        finally:
            client.close()

##############################################################################################
#  Email Methods  (still under  construction, right now this uses mailgun account to send emails)
#
#
##############################################################################################
    def sendEmail(self):
        return requests.post(
        "https://api.mailgun.net/v3/sandbox256f8a2956b94f599e4d4271272dc055.mailgun.org/messages",
        auth=("api", "key-73b25ece01b016bcda09565def14aae6"),
        data={"from": "Mailgun Sandbox <postmaster@sandbox256f8a2956b94f599e4d4271272dc055.mailgun.org>",
              "to": "Ed <ed.horlick@gmail.com>",
              "subject": "From PPro team - Please reply with your PIN code",
              "text": "Dear user who is in some crazy location where phone service blows,\n\rPlease reply to  this email with your PIN code in the message body.\n\rThank you,\n\rThe Fabulous PPro team"})


##############################################################################################
#  assignResultsManager(): Create the ResultManager
#        Input parms are what is necessary to interface with TestRail, since that is the test
#             case/results app we are currently using
#
##############################################################################################
    def assignResultsManager(self):
         return Results.ResultManager(self.testRunId, self.testdata.TEST_RAIL_URL, self.testdata.TEST_RAIL_USER, self.testdata.TEST_RAIL_PW)

##############################################################################################
#  webServiceRestRequest()
#
#
##############################################################################################
    def webServiceRestRequest(self, url):
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.readall().decode('utf-8'))
        if (verbose):
            pprint (result)
        return result
