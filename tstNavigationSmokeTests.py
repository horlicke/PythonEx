__author__ = 'horlicke'

#!/usr/bin/python

import sys
import os
import Framework


fileName =  os.path.basename(sys.argv[0])
testRunId = os.path.basename(sys.argv[1])
browserType = os.path.basename(sys.argv[2])

## Sample  testSetup
def testSetup():
    global _framework
    global _testdata
    global _webPortal
    global _results
    global _eyes

    print("****** Test Setup ******")

    _framework = Framework.FW(testRunId, browserType)                      #mandatory to set up framework
    _eyes = _framework.assignEyeballs()
    _testdata = _framework.getProductTestData()                            #use to get testdata for the specific product.  See Testdata module
    _results = _framework.assignResultsManager()                           #use to set up results reporting. See Results module
    _webPortal = _framework.assignPortalAndBrowser(_testdata.PORTAL_URL)   #use for web portal testing to setup webdriver, url and product-specific web page locators                                                  #instantiate applitools eyes


    _webPortal.openLoginScreen()                                         #Navigate to login screen
    _webPortal.setDriver(_eyes.openEyes(_webPortal.getDriver()))         #Needed for Applitools support
    print("****** Begin Tests ******")


##############################################################################################
#  testTeardown()
#
#
##############################################################################################
def testTearDown():
    _framework.sleep(5)
    _webPortal.closeWebdriver()
    print("\n\r*************** Total Tests Run: " + str(_results.getTotalRun()) + ", Total Passed: " + str(_results.getTotalPassed()) + ", Total Failed: " + str(_results.getTotalFailed()) + " ***************")
    _eyes.abortEyesIfNotClosed()


##############################################################################################
#  Here are the test method(s)
#     Mandatory input for results reporting:
#        - testCaseID: Testcase ID (if interfacing with TestRail, this is the TestRail test case ID
#
#     Optional input for results reporting:
#        - outputMessage:  This is the text that will be displayed in the results
#
#     Other input as needed
#
##############################################################################################
def testBasicNavigationClientUser(testCaseID, outputMessage):
        everythingPassed = True
        _eyes.check_window('Login Page')
        _webPortal.Login(_testdata.ADMIN_USERNAME, _testdata.ADMIN_PASSWORD)
        _eyes.check_window('Admin Landing Page')
        _webPortal.HoverOverUsersButtonInNavBar()
        _framework.sleep(3)
        _eyes.check_window('Users Hover')
        _webPortal.GoToUsersPage()
        _eyes.check_window('Users Page')
        _webPortal.GoToSitesPage()
        _eyes.check_window('Sites Page')
        _webPortal.GoToReportsPage()
        _eyes.check_window('Reports Page')
        _webPortal.GoToStatusPage()
        _eyes.check_window('Status Page')
        _webPortal.GoToSearchPage()
        _eyes.check_window('Search Page')

    # End visual testing. Validate visual correctness.
        try:
            _eyes.closeEyes()
        except:
            everythingPassed = False

        _results.assertTrue(everythingPassed, testCaseID, testBasicNavigationClientUser.__name__, fileName, outputMessage )

##############################################################################################
#  Main entry: Execute setup, test methods and teardown
#
#
##############################################################################################
testSetup()

testBasicNavigationClientUser(78962, "Basic Web Page Navigation Smoke Test")

testTearDown()
