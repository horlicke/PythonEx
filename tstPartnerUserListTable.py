__author__ = 'horlicke'
#!/usr/bin/python

import sys
import os
import Framework

############################################################################################
# Script Name: tstUserListTable.py
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


def testIsBreadCrumbDisplayedCorrectly(testCaseID, outputMessage):
    _results.assertTrue((_webPortal.IsFirstLevelBreadCrumbCorrect(_testdata.USERS_LIST_MAIN_BREADCRUMB_TEXT) and
                         _webPortal.IsSecondLevelBreadCrumbCorrect(_testdata.USERS_LIST_SECOND_BREADCRUMB_TEXT)
                         ),
                         testCaseID, testIsBreadCrumbDisplayedCorrectly.__name__ , fileName, outputMessage)

def testGoButtonIsNotEnabledOnInitialLoadOfUserListPage(testCaseID, outputMessage):
    _results.assertTrue((not _webPortal.GoButtonEnabled()), testCaseID, testGoButtonIsNotEnabledOnInitialLoadOfUserListPage.__name__ , fileName, outputMessage)
    _framework.sleep(3)

def testRoleDropdownOptionsP(testCaseID, outputMessage):
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
                        testCaseID, testRoleDropdownOptionsP.__name__ , fileName, outputMessage)

def testPartnerUserListingTableHeader(testCaseID, outputMessage):
    _webPortal.SelectRoleP("partner")
    _results.assertTrue((_webPortal.UsersTableHeaderIsCorrect(_testdata.USER_ROLE_PARTNER_TEXT) and
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

def testClientUserSelectionDropdownOptions(testCaseID, outputMessage):
    #Select Client Role
    _webPortal.ClickRoleDropdown()
    _framework.sleep(3)
    _webPortal.SelectRoleP("Client")
    _framework.sleep(3)
    _webPortal.ClickDivisionDropdown()
    _framework.sleep(3)
    textSelectDivision, textAtlantic, textCentralNorth, textMidAmerica, textNE, textSE, textWest = _webPortal.GetDivisionDropDownOptionTextsP()
    _results.assertTrue(((textSelectDivision == _testdata.USER_DIVISION_SELECT_ROLE_TEXT) and
                         (textAtlantic == _testdata.STATUS_PAGE_Atlantic) and
                         (textCentralNorth == _testdata.STATUS_PAGE_Central_North) and
                         (textMidAmerica == _testdata.STATUS_PAGE_Mid_America) and
                         (textNE == _testdata.STATUS_PAGE_Northeast) and
                         (textSE == _testdata.STATUS_PAGE_Southeast) and
                         (textWest == _testdata.STATUS_PAGE_West)  and
                         _webPortal.UsersListPageSiteDropdownIsDisabled() ),
                        testCaseID, testClientUserSelectionDropdownOptions.__name__ , fileName, outputMessage)


def testClientUserSelectDivisionAndSite(testCaseID, division, site, outputMessage):
    _webPortal.ClickSiteDropdownOnUsersListPage()
    _framework.sleep(2)
    _webPortal.SelectDivisionP(division)
    _framework.sleep(2)
    _webPortal.SelectSiteP(site)
    print("end...")
    _framework.sleep(20)



def testClientUserListingTableHeader(testCaseID, outputMessage):
    _results.assertTrue((_webPortal.UsersTableHeaderIsCorrect(_testdata.USER_ROLE_CLIENT_TEXT) and
                         _webPortal.AddUserButtonDisplays("Add User")
                         ),
                         testCaseID, testClientUserListingTableHeader.__name__ , fileName, outputMessage)

##############################################################################################
#  Main entry: Execute setup, test methods and teardown
#
#
##############################################################################################
testSetup()

print("Begin tests for listing of Partner Admin users...")
testIsBreadCrumbDisplayedCorrectly(77777, "Username: %s and password: %s" % (_testdata.PARTNER_USERNAME, _testdata.PARTNER_PASSWORD))
testGoButtonIsNotEnabledOnInitialLoadOfUserListPage(77601, "Username: %s and password: %s" % (_testdata.PARTNER_USERNAME, _testdata.PARTNER_PASSWORD))
testRoleDropdownOptionsP(77609, "Username: %s and password: %s" % (_testdata.PARTNER_USERNAME, _testdata.PARTNER_PASSWORD) )
testPartnerUserListingTableHeader(77777, "Username: %s and password: %s" % (_testdata.PARTNER_USERNAME, _testdata.PARTNER_PASSWORD))
testPartnerUserListingColumnHeaders(77777, "Username: %s and password: %s" % (_testdata.PARTNER_USERNAME, _testdata.PARTNER_PASSWORD))

print("Begin tests for listing of Client users...")
testClientUserSelectionDropdownOptions(77777, "Username: %s and password: %s" % (_testdata.PARTNER_USERNAME, _testdata.PARTNER_PASSWORD))
testClientUserSelectDivisionAndSite(77777, _testdata.STATUS_PAGE_Southeast, _testdata.LABCORP_SITE_Under_Test, "Username: %s and password: %s" % (_testdata.PARTNER_USERNAME, _testdata.PARTNER_PASSWORD))
testClientUserListingTableHeader(77777, "Username: %s and password: %s" % (_testdata.PARTNER_USERNAME, _testdata.PARTNER_PASSWORD))


testTearDown()