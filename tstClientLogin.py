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
    _webPortal = _framework.assignPortalAndBrowser(_testdata.PORTAL_URL)    #use for web portal testing to setup webdriver, url and product-specific web page locators

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
    #_framework.connectToDB(_testdata.DB_USERNAME, _testdata.DB_HOST, _testdata.DB_NAME, _testdata.DB_PASSWORD)        #use if doing database queries.  See Framework and DB_Manager modules
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
def testBadCredentials(testCaseID, username, pw, outputMessage):
    _webPortal.Login(username, pw)                                                   #Attempt login
    _results.assertTrue((not _webPortal.OnLandingPage("client") and (_webPortal.IsInvalidLoginTextDisplayed())), testCaseID, testBadCredentials.__name__ , fileName, outputMessage)

def testValidClientUserLoginGoesToLandingPage(testCaseID, user,  pw, outputMessage):
    _webPortal.Login(user, pw)
    _results.assertTrue(_webPortal.OnLandingPage("client"), testCaseID, testValidClientUserLoginGoesToLandingPage.__name__, fileName, outputMessage )
    _webPortal.Logout()

def testSQLQuery(testCaseID, query):
    outputMessage = ""
    _framework.connectToDB(_testdata.DB_USERNAME, _testdata.DB_HOST, _testdata.DB_NAME, _testdata.DB_PASSWORD)        #use if doing database queries.  See Framework and DB_Manager modules
    response = _framework.sqlQueryAndCloseConnection(query)
    if (verbose):
        print ("Reply from query is:")
        for i in response:
            print(i)
        print ("\n\r")

    _results.assertTrue(True, testCaseID, testSQLQuery.__name__, fileName, "Actual response:\n\r" + str(response) )

def testSendHTTPGet(testCaseID, outputMessage, message):
    response = _framework.TCPCreateAndSendMessageAndGetResponse(message, _testdata.SERVER_HOST, _testdata.SERVER_PORT)
    _results.assertTrue(("200 OK" in response), testCaseID, testSendHTTPGet.__name__, fileName )
    _framework.sendEmail()

def testRestWebServiceCaryWeatherFiveDayForecast(testCaseID, url):
    response = _framework.webServiceRestRequest(url)
    #response is an array reflecting the JSON response

    errorOutput = ""
    for index1 in range(len(response["list"])):
        dailyTemperature = response["list"][index1]["main"]["temp"]
        date = response["list"][index1]["dt_txt"]
        errorOutput += date + ", Temperature: " + str(dailyTemperature) + "\n\r"

    _results.assertTrue(True, testCaseID, testRestWebServiceCaryWeatherFiveDayForecast.__name__, fileName, errorOutput )

##############################################################################################
#  Main entry: Execute setup, test methods and teardown
#
#
##############################################################################################
testSetup()

#testRestWebServiceCaryWeatherFiveDayForecast(67317, _testdata.REST_WEBSERVICE_URL)
#testSQLQuery(67315, 'select * from ha_definitions')
#testSendHTTPGet(67316, "HTTP message sent=>\n\r " + _testdata.HTTP_GET_MESSAGE, _testdata.HTTP_GET_MESSAGE)
testValidClientUserLoginGoesToLandingPage(77533, _testdata.CLIENT_USERNAME, _testdata.CLIENT_PASSWORD, " Username: %s and password: %s" % (_testdata.CLIENT_USERNAME, _testdata.CLIENT_PASSWORD))
testBadCredentials(77536, _testdata.CLIENT_USERNAME, "badPassword", "Username: %s and password: %s" % (_testdata.CLIENT_USERNAME, "badPassword"))


testTearDown()





