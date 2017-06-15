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

fileName =  os.path.basename(sys.argv[0])
testRunId = os.path.basename(sys.argv[1])
browserType = os.path.basename(sys.argv[2])

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
    _framework = Framework.FW(testRunId, browserType)                        #mandatory to set up framework
    _testdata = _framework.getProductTestData()                              #assign testdata for the specific product.  See Testdata module
    _results = _framework.assignResultsManager()                             #set up results reporting. See Results module
    _webPortal = _framework.assignPortalAndBrowser(_testdata.PORTAL_URL)     #create webportal object for web ui testing/navigation

    _webPortal.openLoginScreen()                                             #Navigate to login screen
    print("****** Begin Test(s) ******")
    _webPortal.Login(_testdata.CLIENT_USERNAME, _testdata.CLIENT_PASSWORD)
    _framework.sleep(10)

##############################################################################################
#  testTeardown()
#
#
##############################################################################################
def testTearDown():
    _framework.sleep(10)
    _webPortal.closeWebdriver()
    print("\n\r*************** Total Tests Run: " + str(_results.getTotalRun()) + ", Total Passed: " + str(_results.getTotalPassed()) + ", Total Failed: " + str(_results.getTotalFailed()) + " ***************")
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
def testClickingReportsButtonTakesUserToReportsPage(testCaseID, outputMessage):
    _webPortal.GoToReportsPage()
    _results.assertTrue((_webPortal.OnClientReportsPage()), testCaseID, testClickingReportsButtonTakesUserToReportsPage.__name__ , fileName, outputMessage)


def testClickingStatusButtonTakesUserToStatusPage(testCaseID, outputMessage):
    _webPortal.GoToStatusPage()
    _results.assertTrue((_webPortal.OnClientStatusPage()), testCaseID, testClickingStatusButtonTakesUserToStatusPage.__name__ , fileName, outputMessage)

def testClickingStatusButtonTakesUserToPrintStreamPage(testCaseID, outputMessage):
    _webPortal.GoToPrintStreamPage()
    _results.assertTrue((_webPortal.OnClientPrintStreamPage()), testCaseID, testClickingStatusButtonTakesUserToPrintStreamPage.__name__ , fileName, outputMessage)


##############################################################################################
#  Main entry: Execute setup, test methods and teardown
#
#
##############################################################################################
testSetup()
testClickingReportsButtonTakesUserToReportsPage(78837, "Username: %s and password: %s" % (_testdata.CLIENT_USERNAME, _testdata.CLIENT_PASSWORD) )
testClickingStatusButtonTakesUserToStatusPage(78836, "Username: %s and password: %s" % (_testdata.CLIENT_USERNAME, _testdata.CLIENT_PASSWORD) )
testClickingStatusButtonTakesUserToPrintStreamPage(78836, "Username: %s and password: %s" % (_testdata.CLIENT_USERNAME, _testdata.CLIENT_PASSWORD) )

testTearDown()
