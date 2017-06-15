__author__ = 'horlicke'
#!/usr/bin/python

import sys
import os
import Framework

############################################################################################
# Script Name: tstUserListTableHeader.py
#
#     Input parms
#           - filename (implicit)
#           - TestRail's Test run Id
#           - Browser type ("Chrome", "IE", or "Firefox")
##############################################################################################
fileName =  os.path.basename(sys.argv[0])
testRunId = os.path.basename(sys.argv[1])
browserType = os.path.basename(sys.argv[2])


#############################################################################################
#  testSetup()
#
#     This method sets up/assigns the:
#           - framework
#           - test data (which is defined in Testdata.py)
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
    _testdata = _framework.getProductTestData()                              #use to get testdata for the specific product.  See Testdata module
    _results = _framework.assignResultsManager()                             #use to set up results reporting. See Results module
    _webPortal = _framework.assignPortalAndBrowser(_testdata.PORTAL_URL)     #use for web portal testing to setup webdriver, url and product-specific web page locators

    _webPortal.openLoginScreen()                                             #Navigate to login screen
    _webPortal.Login(_testdata.PARTNER_USERNAME, _testdata.PARTNER_PASSWORD)
    _framework.sleep(5)
    _webPortal.GoToUsersListPage()
    _framework.sleep(3)

    print("****** Begin Test(s) ******")


##############################################################################################
#  testTeardown()
#
#
##############################################################################################
def testTearDown():
    _webPortal.closeWebdriver()
    print("\n\r*************** Total Tests Run: " + str(_results.getTotalRun()) + ", Total Passed: " + str(_results.getTotalPassed()) + ", Total Failed: " + str(_results.getTotalFailed()) + " ***************")
    _framework.sleep(3)

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

def testGoButtonIsNotEnabledOnInitialLoadOfUserListPage(testCaseID, outputMessage):
    _results.assertTrue((not _webPortal.GoButtonEnabled()), testCaseID, testGoButtonIsNotEnabledOnInitialLoadOfUserListPage.__name__ , fileName, outputMessage)
    _framework.sleep(3)

def testRoleDropdownOptionsAdmin(testCaseID, outputMessage):
    _webPortal.HoverOverUsersButtonInNavBar()
    #_framework.sleep(5)
    # _webPortal.SelectUserList()
    _framework.sleep(3)
    _webPortal.ClickRoleDropdown()
    _framework.sleep(3)
    textSelectRole, textPartner, textClient = _webPortal.GetDropDownOptionTextAdminP()
    _results.assertTrue(((textSelectRole == _testdata.USER_ROLE_SELECT_ROLE_TEXT) and
                         (textPartner == _testdata.USER_ROLE_PARTNER_TEXT) and
                         (textClient == _testdata.USER_ROLE_CLIENT_TEXT) ),
                        testCaseID, testRoleDropdownOptionsAdmin.__name__ , fileName, outputMessage)

def testPartnerUserListingTableHeader(testCaseID, outputMessage):
    _webPortal.SelectRoleP("partner")
    _results.assertTrue((_webPortal.TableHeaderIsCorrect("partner") and
                         _webPortal.AddUserButtonDisplays("Add User")
                         ),
                         testCaseID, testPartnerUserListingTableHeader.__name__ , fileName, outputMessage)

def testPartnerUserListingColumnHeaders(testCaseID, outputMessage):
    _results.assertTrue((_webPortal.ListTableFirstNameColumnHeaderIsCorrect(_testdata.USER_LIST_First_Name_Header) and
                         _webPortal.ListTableLastNameColumnHeaderIsCorrect(_testdata.USER_LIST_Last_Name_Header) and
                         _webPortal.ListTableUserNameColumnHeaderIsCorrect(_testdata.USER_LIST_User_Name_Header) and
                         _webPortal.ListTableRoleColumnHeaderIsCorrect(_testdata.USER_LIST_Role_Header) and
                         _webPortal.ListTablePhoneColumnHeaderIsCorrect(_testdata.USER_LIST_Phone_Header) and
                         _webPortal.ListTableEmailColumnHeaderIsCorrect(_testdata.USER_LIST_Email_Header) and
                         _webPortal.ListTableBlankColumnHeaderIsCorrect("")
                         ),
                         testCaseID, testPartnerUserListingColumnHeaders.__name__ , fileName, outputMessage)





def testClickingStatusButtonTakesUserToStatusPage(testCaseID, outputMessage):
    _webPortal.SelectRole("admin")
    #_results.assertTrue((_webPortal.OnStatusPage("client")), testCaseID, testClickingStatusButtonTakesUserToStatusPage.__name__ , fileName, outputMessage)


##############################################################################################
#  Main entry: Execute setup, test methods and teardown
#
#
##############################################################################################
testSetup()

testGoButtonIsNotEnabledOnInitialLoadOfUserListPage(77615, "Username: %s and password: %s" % (_testdata.PARTNER_USERNAME, _testdata.PARTNER_PASSWORD))
testRoleDropdownOptionsAdmin(77622, "Username: %s and password: %s" % (_testdata.PARTNER_USERNAME, _testdata.PARTNER_PASSWORD) )
testPartnerUserListingTableHeader(77777, "Username: %s and password: %s" % (_testdata.PARTNER_USERNAME, _testdata.PARTNER_PASSWORD))
testPartnerUserListingColumnHeaders(77777, "Username: %s and password: %s" % (_testdata.PARTNER_USERNAME, _testdata.PARTNER_PASSWORD))
testTearDown()