__author__ = 'horlicke'

from Testrail import *
from pprint import pprint
import json

verbose = False

TESTRAIL_PASS_CODE = 1
TESTRAIL_FAIL_CODE = 5

class ResultManager:
    def __init__(self, testRunId, testRailURL, testRailUser, testRailPW):
        self.runId   = testRunId
        self.testsRun    = 0
        self.testsPassed = 0
        self.testsFailed  = 0
        #self.TestRailclient  = APIClient('https://anx.testrail.com')
        self.TestRailclient  = APIClient(testRailURL)

        self.TestRailclient.user = testRailUser
        self.TestRailclient.password = testRailPW

    def reportResult(self, result, testCaseId, testOutputMessage, testFunctionName, testScriptName):
        self.testsRun += 1
        resString = "PASS"
        #print to console, FUTURE: Log to file as well if necessary

        if not result:
            statusId = TESTRAIL_FAIL_CODE
            resString = "FAIL"
            self.testsFailed += 1
        else:
            statusId = TESTRAIL_PASS_CODE
            self.testsPassed += 1

        if testOutputMessage and (not result):
            print("***Result: " + resString + ", TC ID: " + str(testCaseId) + ", Test Run: " + str(self.runId) + ",  Test Script: " + testScriptName + ", Function: " + testFunctionName + ", Message: " + testOutputMessage)
        else:
            print("***Result: " + resString + ", TC ID: " + str(testCaseId) + ", Test Run: " + str(self.runId) + ",  Test Script: " + testScriptName + ", Function: " + testFunctionName)

        #report to TestRail
        if (not testOutputMessage) or (result):
                testOutputMessage = ""
        try:
            result = self.TestRailclient.send_post('add_result_for_case/%s/%s'%(str(self.runId), str(testCaseId)),  {'status_id': statusId, 'comment': "Test Script: " + testScriptName + ",    Function: " + testFunctionName + "\n\r\n\r" + testOutputMessage })
        except APIError:
            print("ERROR: Testrail API call for " + testScriptName + "::" + testFunctionName + "  failed for testrun " + str(self.runId))

    def getTotalRun(self):
        return self.testsRun

    def getTotalPassed(self):
        return self.testsPassed

    def getTotalFailed(self):
        return self.testsFailed

    def getOptionalOutputMessages(self, testCaseId, optionalOutputMessage):
        if verbose:
            print("optional: " + optionalOutputMessage)
        #get optional message from testrail
        case = self.TestRailclient.send_get("get_case/" + str(testCaseId))
        testOutputMessage = case["custom_customoutputmessage"]

        #if scripter defined an output message as well, concatenate it.
        if optionalOutputMessage and testOutputMessage:
            testOutputMessage += ",   " + optionalOutputMessage
        elif optionalOutputMessage:
            testOutputMessage = optionalOutputMessage

        return  testOutputMessage

    def assertTrue(self, proc, testCaseId, testFunctionName, testScriptName, optionalOutputMessage = ""):
        passResult = True

        testOutputMessage = self.getOptionalOutputMessages(testCaseId, optionalOutputMessage)

        try:
            assert proc == True
        except AssertionError:
            passResult = False
        finally:
            self.reportResult(passResult, testCaseId, testOutputMessage, testFunctionName, testScriptName)
        return passResult


    def assertFalse(self, proc, testCaseId, testFunctionName, testScriptName, optionalOutputMessage = ""):
        passResult = True

        testOutputMessage = "fix this"
        #testOutputMessage = self.getOptionalOutputMessages(testCaseId, optionalOutputMessage)

        try:
            assert proc == False
        except AssertionError:
            passResult = False
        finally:
            self.reportResult(passResult, testCaseId, testOutputMessage, testFunctionName, testScriptName)
        return passResult