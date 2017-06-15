__author__ = 'horlicke'

#!/usr/bin/python

import sys
import Framework
import os


#############################################################################################
# Script Name: tstPartnerDivisionStatusPage.py
#
#   Input parms
#           - filename (implicit)
#           - TestRail's Test run Id
#           - Browser type ("Chrome", "IE", or "Firefox")
#           - Partner Lab ("Labcorp", etc.)
#   Purpose:
#      As a PARTNER user, confirm the layout of the division status page and confirm
#      the node numbers add up properly for each division
##############################################################################################

fileName    =  os.path.basename(sys.argv[0])
testRunId   = os.path.basename(sys.argv[1])
browserType = os.path.basename(sys.argv[2])
partnerLab  = os.path.basename(sys.argv[3])


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
    _webPortal.Login(_testdata.PARTNER_USERNAME, _testdata.PARTNER_PASSWORD)
    _framework.sleep(7)
    _webPortal.GoToStatusPage()
    _framework.sleep(2)


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
def testDivisionPageLabels(testCaseID, Lab, Division, outputMessage):
    _webPortal.StatusPage_SelectDivision(Division)
    _results.assertTrue((_webPortal.IsLabelShowing(_testdata.STATUS_PAGE_Total_Nodes_Label_Text) and
                        _webPortal.IsLabelShowing(_testdata.STATUS_PAGE_Nodes_Activated_Label_Text) and
                        _webPortal.IsLabelShowing(_testdata.STATUS_PAGE_Online_Label_Text) and
                        _webPortal.IsLabelShowing(_testdata.STATUS_PAGE_Offline_Short_Label_Text) and
                        _webPortal.IsLabelShowing(_testdata.STATUS_PAGE_Offline_Long_Label_Text) and
                        _webPortal.IsLabelShowing(_testdata.STATUS_PAGE_Nodes_Not_Activated_Label_Text) and
                        _webPortal.IsLabelShowing(_testdata.STATUS_PAGE_Nodes_With_Errors_Label_Text) and
                        _webPortal.IsViewNodesButtonShowingAndActive(_testdata.STATUS_PAGE_View_Nodes_Button_Text)
                         ),
                        testCaseID, testDivisionPageLabels.__name__ , fileName, outputMessage)


def testNodeStats(testCaseID, outputMessage):
    _results.assertTrue((_webPortal.IsNumberShowing(_testdata.STATUS_PAGE_Total_Nodes_Label_Text) and
                        _webPortal.IsNumberShowing(_testdata.STATUS_PAGE_Nodes_Activated_Label_Text) and
                         _webPortal.IsNumberShowing(_testdata.STATUS_PAGE_Online_Label_Text) and
                         _webPortal.IsNumberShowing(_testdata.STATUS_PAGE_Offline_Short_Label_Text) and
                         _webPortal.IsNumberShowing(_testdata.STATUS_PAGE_Offline_Long_Label_Text) and
                         _webPortal.IsNumberShowing(_testdata.STATUS_PAGE_Nodes_Not_Activated_Label_Text) and
                         _webPortal.IsNumberShowing(_testdata.STATUS_PAGE_Nodes_With_Errors_Label_Text) and
                         _webPortal.TotalNodesEqualActivatedPlusInactivatedNodes() and
                         _webPortal.ActivatedNodesEqualOnlinePlusOffline()
                         ),
                        testCaseID, testNodeStats.__name__ , fileName, outputMessage)

def testNodeNumbersMakeSense(testCaseID, outputMessage):
    _results.assertTrue((_webPortal.TotalNodesEqualActivatedPlusInactivatedNodes() and
                         _webPortal.ActivatedNodesEqualOnlinePlusOffline()
                         ),
                        testCaseID, testDivisionPageLabels.__name__ , fileName, outputMessage)

#def testDivisionPageFooter(testCaseID, versionNumber, outputMessage):
#    _results.assertTrue((_webPortal.VersionShows("Version " + versionNumber)),
#                        testCaseID, testDivisionPage.__name__ , fileName, outputMessage)


##############################################################################################
#  Main entry: Execute setup, test methods and teardown
#
#
##############################################################################################
testSetup()
division = _testdata.STATUS_PAGE_Southeast
testDivisionPageLabels(78806, partnerLab, division, "Lab: %s, Divsion: %s, Check format of Division Status Page" % (partnerLab, division ) )
testNodeStats(78812, "Lab: %s, Divsion: %s, Check node numbers on Division Status Page" % (partnerLab, division ) )

division = _testdata.STATUS_PAGE_Atlantic
testDivisionPageLabels(78807, partnerLab, division, "Lab: %s, Divsion: %s, Check format of Division Status Page" % (partnerLab, division ) )
testNodeStats(78813, "Lab: %s, Divsion: %s, Check node numbers on Division Status Page" % (partnerLab, division ) )

division = _testdata.STATUS_PAGE_West
testDivisionPageLabels(78808, partnerLab, division, "Lab: %s, Divsion: %s, Check format of Division Status Page" % (partnerLab, division  ) )
testNodeStats(78814, "Lab: %s, Divsion: %s, Check node numbers on Division Status Page" % (partnerLab, division ) )

division = _testdata.STATUS_PAGE_Northeast
testDivisionPageLabels(78809, partnerLab, division, "Lab: %s, Divsion: %s, Check format of Division Status Page" % (partnerLab, division  ) )
testNodeStats(78815, "Lab: %s, Divsion: %s, Check node numbers on Division Status Page" % (partnerLab, division ) )

division = _testdata.STATUS_PAGE_Mid_America
testDivisionPageLabels(78810, partnerLab, division, "Lab: %s, Divsion: %s, Check format of Division Status Page" % (partnerLab, division  ) )
testNodeStats(78816, "Lab: %s, Divsion: %s, Check node numbers on Division Status Page" % (partnerLab, division ) )

division = _testdata.STATUS_PAGE_Central_North
testDivisionPageLabels(78811, partnerLab, division, "Lab: %s, Divsion: %s, Check format of Division Status Page" % (partnerLab, division ) )
testNodeStats(78817, "Lab: %s, Divsion: %s, Check node numbers on Division Status Page" % (partnerLab, division ) )

#testDivisionPageFooter()
testTearDown()