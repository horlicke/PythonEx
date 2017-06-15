__author__ = 'horlicke'

#!/usr/bin/python

import sys
import Framework
import os

#############################################################################################
# Script Name: tstBasicLogin.py
#
#     Input parms
#           - filename (implicit)
#           - TestRail's Test run Id
#           - Browser type ("Chrome", "IE", or "Firefox")
##############################################################################################
fileName    =  os.path.basename(sys.argv[0])
testRunId   = os.path.basename(sys.argv[1])
browserType = os.path.basename(sys.argv[2])

verbose = True


##############################################################################################
#  testSetup()
#
#     This method sets up/assigns the:
#           - framework
#           - test data (which is defined in TestData.py)
#           - results reporting
#           - web portal (optional, for web UI testing with Selenium webdriver)
#
#     Other functionality for setting up the test methods can be added
##############################################################################################
def testSetup():
    global _framework
    global _testdata
    global _webPortal
    global _results

    print("****** Test Setup ******")
    _framework = Framework.FW(testRunId, browserType)                       #mandatory to set up framework
    _testdata = _framework.getProductTestData()                             #use to get testdata for the specific product.  See Testdata module
    _results = _framework.assignResultsManager()                            #use to set up results reporting. See Results module
    #_webPortal = _framework.assignPortalAndBrowser(_testdata.PORTAL_URL)    #use for web portal testing to setup webdriver, url and product-specific web page locators
    _framework.connectToDB(_testdata.DB_USERNAME, _testdata.DB_HOST, _testdata.DB_NAME, _testdata.DB_PASSWORD)        #use if doing database queries.  See Framework and DB_Manager modules
    #_webPortal.openLoginScreen()                                             #Navigate to login screen
    print("****** Begin Test(s) ******")



##############################################################################################
#  testTeardown()
#
#
##############################################################################################
def testTearDown():
   #_webPortal.closeWebdriver()
    print("\n\r*************** Total Tests Run: " + str(_results.getTotalRun()) + ", Total Passed: " + str(_results.getTotalPassed()) + ", Total Failed: " + str(_results.getTotalFailed()) + " ***************")
    _framework.closeDBConnection()
    #response = _framework.sqlQueryAndCloseConnection("UPDATE [user] SET u_failed_login_attempts=0, u_locked=0 where u_username=\'_testdata.USERNAME\'")
    _framework.sleep(5)

##############################################################################################
#  Here are the test methods
#     Mandatory input for results reporting:
#        - testCaseID: Testcase ID (if interfacing with TestRail, this is the TestRail test case ID
#
#     Optional input for results reporting:
#        - outputMessage:  This is the text that will be displayed in the results
#
#     Other input as needed
#
##############################################################################################
def testSQLQuery(testCaseID, query):
    outputMessage = ""
    #_framework.connectToDB(_testdata.DB_USERNAME, _testdata.DB_HOST, _testdata.DB_NAME, _testdata.DB_PASSWORD)        #use if doing database queries.  See Framework and DB_Manager modules
    #response = _framework.sqlQueryAndCloseConnection(query)
    response = _framework.sqlQuery(query)
    if (verbose):
        print ("Reply from query is:")
        for i in response:
            print(i)
        print ("\n\r")

    _results.assertTrue(True, testCaseID, testSQLQuery.__name__, fileName, "Actual response:\n\r" + str(response) )

def tstPartnerUserAddPartner_DB(testCaseID, provisioningData):

##############################################################################################
#  Main entry: Execute setup, test methods and teardown
#
#
##############################################################################################
testSetup()

#make provisiong data readable from config file in future, hardcode for now.
tstPartnerUserAddPartner_DB(67315, _testdata.PARTNER_USER_PROVISIONING_DATA, "Provisioned Partner Username: %s" % (_testdata.PROV_PARTNER_USERNAME ))
testSQLQuery(67315, 'select * from partner')
testSQLQuery(67315, 'select * from client_site_contact')


testTearDown()






