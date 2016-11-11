__author__ = 'horlicke'

#!/usr/bin/python

import sys
import os
import Framework

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
    _webPortal = _framework.assignPortalAndBrowser(_testdata.PORTAL_URL)     #for web portal testing to setup webdriver, url and product-specific web page locators

    _webPortal.openLoginScreen()                                             #Navigate to login screen
    print("****** Begin Test(s) ******")


##############################################################################################
#  testTeardown()
#
#
##############################################################################################
def testTearDown():
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

def testBadCredentials(testCaseID, username, pw, outputMessage):
    _webPortal.Login(username, pw)
    _results.assertTrue((not _webPortal.OnLandingPage("client") and (_webPortal.IsInvalidLoginTextDisplayed())), testCaseID, testBadCredentials.__name__ , fileName, outputMessage)

def testValidClientUserLoginGoesToLandingPage(testCaseID, user,  pw, outputMessage):
    _webPortal.Login(user, pw)
    _results.assertTrue(_webPortal.OnLandingPage("client"), testCaseID, testValidClientUserLoginGoesToLandingPage.__name__, fileName, outputMessage )
    _webPortal.Logout()

def testValidAdminUserLoginGoesToLandingPage(testCaseID, user,  pw, outputMessage):
    _webPortal.Login(user, pw)
    _results.assertTrue(_webPortal.OnLandingPage("admin"), testCaseID, testValidAdminUserLoginGoesToLandingPage.__name__, fileName, outputMessage )
    _webPortal.Logout()

def testValidPartnerUserLoginGoesToLandingPage(testCaseID, user,  pw, outputMessage):
    _webPortal.Login(user, pw)
    _results.assertTrue(_webPortal.OnLandingPage("admin"), testCaseID, testValidPartnerUserLoginGoesToLandingPage.__name__, fileName, outputMessage )
    _webPortal.Logout()

##############################################################################################
#  Main entry: Execute setup, test methods and teardown
#
#
##############################################################################################
testSetup()

testValidClientUserLoginGoesToLandingPage(77533, _testdata.CLIENT_USERNAME, _testdata.CLIENT_PASSWORD, " Username: %s and password: %s" % (_testdata.CLIENT_USERNAME, _testdata.CLIENT_PASSWORD))
testValidAdminUserLoginGoesToLandingPage(77532, _testdata.ADMIN_USERNAME, _testdata.ADMIN_PASSWORD, " Username: %s and password: %s" % (_testdata.ADMIN_PASSWORD, _testdata.ADMIN_PASSWORD))
testValidPartnerUserLoginGoesToLandingPage(77534, _testdata.PARTNER_USERNAME, _testdata.PARTNER_PASSWORD, " Username: %s and password: %s" % (_testdata.PARTNER_PASSWORD, _testdata.PARTNER_PASSWORD))
testBadCredentials(77536, _testdata.CLIENT_USERNAME, "badPassword", "Username: %s and password: %s" % (_testdata.CLIENT_USERNAME, "badPassword"))
testBadCredentials(77521, _testdata.CLIENT_USERNAME, "", "Username: %s and password: %s" % (_testdata.CLIENT_USERNAME, ""))
testBadCredentials(78963, _testdata.ADMIN_USERNAME, "badPassword", "Username: %s and password: %s" % (_testdata.ADMIN_USERNAME, "badPassword"))
testBadCredentials(78964, _testdata.ADMIN_USERNAME, "", "Username: %s and password: %s" % (_testdata.ADMIN_USERNAME, ""))
testBadCredentials(78965, _testdata.PARTNER_USERNAME, "badPassword", "Username: %s and password: %s" % (_testdata.PARTNER_USERNAME, "badPassword"))
testBadCredentials(78966, _testdata.PARTNER_USERNAME, "", "Username: %s and password: %s" % (_testdata.PARTNER_USERNAME, ""))
testBadCredentials(78856, "", "", "Username: %s and password: %s" % ("", ""))

testTearDown()