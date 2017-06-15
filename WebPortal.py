__author__ = 'horlicke'
import Locators
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from applitools.eyes import Eyes
import time
import Testdata

debug = False
############################################################
### Parent portal class
############################################################
class Portal:
    def __init__(self, browser, product, url):
        self.browser = browser
        self.product = product
        self.url     = url
        self.testdata = Testdata.MedNx_Testdata


        if (debug):
            print("Init Portal, product: " + self.product)
        global _locators
        if (product == "MedNx"):
            _locators = Locators.MedNx_Locators
        elif (product == "PPro"):
            _locators = Locators.PPro_Locators
            #print(_testdata.USERNAME)
        else: #default to MedNx locators
            _locators = Locators.MedNx_Locators

        if (browser == "Chrome"):
            self.driver = webdriver.Chrome()
        elif (browser == "IE"):
            self.driver = webdriver.Ie("C:\IEDriverServer.exe")
        else:
            self.driver = webdriver.Firefox()

        self.driver.implicitly_wait(10) # seconds

    def getDriver(self):
        return self.driver

    def setDriver(self, newDriver):
        self.oldDriver = self.driver
        self.driver = newDriver


    def openLoginScreen(self):
        if (debug):
            print ("Portal.openLoginScreen: Use webdriver to open browser and go to webtop url")
        self.driver.get(self.url)


    def Login(self, username, password):
        if debug:
            print ("\nPortal Login with username: " + username + ", password: " + password)
        element = self.findElement(_locators.LOGIN_PAGE_Username_Edit_Field)
        element.clear()
        element.send_keys(username)

        element = self.findElement(_locators.LOGIN_PAGE_Password_Edit_Field)
        element.clear()
        element.send_keys(password)

        self.findElement(_locators.LOGIN_PAGE_Login_Button).click()

    def Logout(self):
        self.findElement(_locators.LANDING_PAGE_Logout_Button).click()
        time.sleep(5)

    def closeWebdriver(self):
        if (debug):
            print("Close Webdriver")
        self.driver.close()

    #def getWebDriver(self):
    #    return self.driver
    def findElement(self, locator):
        if (locator[0]=="#") :
            internalLocator = locator[1:]

            if (debug):
                print("locator = " + locator + ", internal locator = " + internalLocator)
            return self.driver.find_element_by_id(internalLocator)
        elif (locator[0]=="."):
            #internalLocator = locator[1:]
            internalLocator = locator
            if (debug):
                print("locator = " + locator + ", internal locator = " + internalLocator)
            return self.driver.find_element_by_css_selector(internalLocator)
        else:
            internalLocator = locator
            if (debug):
                print("locator = " + locator + ", internal locator = " + internalLocator)
            return self.driver.find_element_by_xpath(internalLocator)

    def findElementsByText(self, text):
        locator = "//div[contains(.,"+ text + ")]"
        print ("LLLocatore: " + locator)
        return self.driver.find_elements_by_xpath(locator)

## MedNx Portal classe, inherits from Portal class
class MedNx_Portal(Portal):

    def OnLandingPage(self, userType):

        if userType == 'client':
            #breadcrumbString = "Node Status"  #only for 1.3.  In 1.4, it was changed to just "Status"
            breadcrumbString = "Status"
        else:
            breadcrumbString = "Status"

        locator = _locators.LANDING_PAGE_breadcrumb

        try:
            element = self.findElement(locator)
            return element.text == breadcrumbString
        except:
            return False

    def OnClientStatusPage(self):

        breadcrumbString = "Status"

        locator = _locators.LANDING_PAGE_breadcrumb
        try:
            element = self.findElement(locator)
            return element.text == breadcrumbString
        except:
            return False

    def OnClientPrintStreamPage(self):

        breadcrumbString = "Print Stream"

        locator = _locators.LANDING_PAGE_breadcrumb
        try:
            element = self.findElement(locator)
            return element.text == breadcrumbString
        except:
            return False


    def OnClientReportsPage(self):
        breadcrumbString = "Reports"

        try:
            element = self.findElement(_locators.LANDING_PAGE_breadcrumb)
            return element.text == breadcrumbString
        except:
            return False

    def UsersTableHeaderIsCorrect(self, roleText):

        expectedText = "Users with role " + roleText

        try:
            element = self.findElement(_locators.USER_LIST_Table_Header)
            if (element.text != expectedText):
                print("Element text: " + element.text + ", Expected text: " + expectedText)
            return element.text == expectedText
        except:
            print("Error:TableHeaderIsCorrect() - Can't find element: " + _locators.USER_LIST_Table_Header)
            return False

    def UsersListPageSiteDropdownIsDisabled(self):
        try:
            return (not self.findElement(_locators.USERS_LIST_SITE_Dropdown_Button).is_enabled())
        except:
            print("Error::UsersListPageSiteDropdownIsDisabled().  Locator: " + _locators.USERS_LIST_SITE_Dropdown_Button)
            return False

    def ListTableFirstNameColumnHeaderIsCorrect(self, expectedColumnHeaderText):
        passed = True
        try:
            element = self.findElement(_locators.USER_LIST_Table_FirstName_Header)
            if (element.text != expectedColumnHeaderText):
                print("Error: Element text: " + element.text + ", Expected text: " + expectedColumnHeaderText)
                passed = False

            try:
                if (not self.findElement(_locators.USER_LIST_Table_FirstName_Filter_Button).is_enabled()):
                    print("Error: Filter button is not enabled.")
                    passed = False
            except:
                print("Error:ListTableFirstNameColumnHeaderIsCorrect() - Can't find filter element: " + _locators.USER_LIST_Table_FirstName_Filter_Button)

            return passed
        except:
            print("Error:ListTableFirstNameColumnHeaderIsCorrect() - Can't find element: " + _locators.USER_LIST_Table_FirstName_Header)
            return False

    def ListTableLastNameColumnHeaderIsCorrect(self, expectedColumnHeaderText):
        passed = True
        try:
            element = self.findElement(_locators.USER_LIST_Table_LastName_Header)
            if (element.text != expectedColumnHeaderText):
                print("Error: Element text: " + element.text + ", Expected text: " + expectedColumnHeaderText)
                passed = False

            try:
                if (not self.findElement(_locators.USER_LIST_Table_LastName_Filter_Button).is_enabled()):
                    print("Error: Filter button is not enabled.")
                    passed = False
            except:
                print("Error:ListTableLastNameColumnHeaderIsCorrect() - Can't find filter element: " + _locators.USER_LIST_Table_LastName_Filter_Button)
            return passed
        except:
            print("Error:ListTableLastNameColumnHeaderIsCorrect() - Can't find element: " + _locators.USER_LIST_Table_LastName_Header)
            return False

    def ListTableUserNameColumnHeaderIsCorrect(self, expectedColumnHeaderText):
        try:
            element = self.findElement(_locators.USER_LIST_Table_UserName_Header)
            if (element.text != expectedColumnHeaderText):
                print("Element text: " + element.text + ", Expected text: " + expectedColumnHeaderText)
            return element.text == expectedColumnHeaderText
        except:
            print("Error:ListTableUserNameColumnHeaderIsCorrect() - Can't find element: " + _locators.USER_LIST_Table_UserName_Header)
            return False

    def ListTableRoleColumnHeaderIsCorrect(self, expectedColumnHeaderText):
        try:
            element = self.findElement(_locators.USER_LIST_Table_Role_Header)
            if (element.text != expectedColumnHeaderText):
                print("Element text: " + element.text + ", Expected text: " + expectedColumnHeaderText)
            return element.text == expectedColumnHeaderText
        except:
            print("Error:ListTableRoleColumnHeaderIsCorrect() - Can't find element: " + _locators.USER_LIST_Table_Role_Header)
            return False

    def ListTablePhoneColumnHeaderIsCorrect(self, expectedColumnHeaderText):
        try:
            element = self.findElement(_locators.USER_LIST_Table_Phone_Header)
            if (element.text != expectedColumnHeaderText):
                print("Element text: " + element.text + ", Expected text: " + expectedColumnHeaderText)
            return element.text == expectedColumnHeaderText
        except:
            print("Error:ListTablePhoneColumnHeaderIsCorrect() - Can't find element: " + _locators.USER_LIST_Table_Phone_Header)
            return False

    def ListTableEmailColumnHeaderIsCorrect(self, expectedColumnHeaderText):
        try:
            element = self.findElement(_locators.USER_LIST_Table_Email_Header)
            if (element.text != expectedColumnHeaderText):
                print("Element text: " + element.text + ", Expected text: " + expectedColumnHeaderText)
            return element.text == expectedColumnHeaderText
        except:
            print("Error:ListTableEmailColumnHeaderIsCorrect() - Can't find element: " + _locators.USER_LIST_Table_Email_Header)
            return False

    def ListTableBlankColumnHeaderIsCorrect(self, expectedColumnHeaderText):
        try:
            element = self.findElement(_locators.USER_LIST_Table_Blank_Header)
            if (element.text != expectedColumnHeaderText):
                print("Element text: " + element.text + ", Expected text: " + expectedColumnHeaderText)
            return element.text == expectedColumnHeaderText
        except:
            print("Error:ListTableBlankColumnHeaderIsCorrect() - Can't find element: " + _locators.USER_LIST_Table_Blank_Header)
            return False

    def AddUserButtonDisplays(self, expectedText):
        result = True
        try:
            element = self.findElement(_locators.USER_LIST_Table_Add_Button)
            if not element.is_enabled():
                return False
            return element.text == expectedText
        except:
            print("Error:AddUserButtonDisplays() - Can't find element: " + _locators.USER_LIST_Table_Add_Button)
            return False



    def IsANXLogoDisplayed(self):
        try:
            self.findElement(_locators.LOGIN_PAGE_ANX_Login_Logo)
            return True
        except:
            return False

    def IsMainImageDisplayed(self):
        try:
            self.findElement(_locators.LOGIN_PAGE_ANX_Main_Image)
            return True
        except:
            return False

    def IsErrorTextDisplayed(self):
        try:
            element = self.findElement(_locators.LOGIN_PAGE_ANX_Error_Text)
            #print(element.text)
            return element.text == "Status"
        except:
            return False

    def IsInvalidLoginTextDisplayed(self):
        try:
            element = self.findElement(_locators.LOGIN_PAGE_Invalid_Login_Text)
            return element.text == "Login Failed. Please try again."
        except:
            return False

    def GoToUsersListPage(self):
        try:
            self.findElement(_locators.NAV_BAR_Users_Button).click()
            self.findElement(_locators.NAV_BAR_Users_Button_List).click()
        except:
            print("Error::GoToUsersPage(): Can't find locator")
            return False

    def GoToUsersPage(self):
        try:
            self.findElement(_locators.NAV_BAR_Users_Button_List).click()
        except:
            return False

    def GoToSitesPage(self):
        try:
            self.findElement(_locators.NAV_BAR_Sites_Button_List).click()
        except:
            return False

    def GoToReportsPage(self):
        try:
            print("Click on Reports in nav bar...")
            self.findElement(_locators.NAV_BAR_Reports_Button).click()

        except:
            print("Eror::GoToReportsPage()")
            return False

    def GoToStatusPage(self):
        try:
            self.findElement(_locators.NAV_BAR_Status_Button).click()
        except:
            print("Eror::GoToStatusPage()")
            return False

    def GoToPrintStreamPage(self):
        try:
            self.findElement(_locators.NAV_BAR_Print_Stream_Button).click()
        except:
            print("Eror::GoToPrintStreamPage()")
            return False


    def GoToSearchPage(self):
        try:
            self.findElement(_locators.NAV_BAR_Search_Button).click()
        except:
            return False


    def HoverOverUsersButtonInNavBar(self):
        element = self.findElement(_locators.NAV_BAR_Users_Button)

        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()


    def HoverOverSitesButtonInNavBar(self):
        element = self.findElement(_locators.NAV_BAR_Sites_Button)

        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def UnHover(self):
        element = self.findElement(_locators.NAV_BAR_Users_Button)

        action = ActionChains(self.driver).move_to_element(element)
        action.perform()
        action.move_by_offset(375,10);
        action.perform();

    def SelectUserList(self):
        try:
            self.findElement(_locators.NAV_BAR_Users_Button_List).click()
        except:
            print("Error:SelectUserList() - Can't find element: " + _locators.NAV_BAR_Users_Button_List)
            return False

    def IsFirstLevelBreadCrumbCorrect(self, expectedText):
        result = True
        locator = _locators.FIRST_LEVEL_BREADCRUMB
        try:
            if (expectedText != self.findElement(locator).text):
                print("FAILURE: Expected First Level is " + self.findElement(locator).text)
                result = False
        except:
            print("Error:IsFirstLevelBreadCrumbCorrect() - Can't find element: " + locator)
            return False
        finally:
            return result

    def IsSecondLevelBreadCrumbCorrect(self, expectedText):
        result = True
        locator = _locators.SECOND_LEVEL_BREADCRUMB
        try:
            if (expectedText != self.findElement(locator).text):
                print("FAILURE: Expected First Level is " + self.findElement(locator).text)
                result = False
        except:
            print("Error:IsSecondLevelBreadCrumbCorrect() - Can't find element: " + locator)
            return False
        finally:
            return result

    def ClickRoleDropdown(self):
        try:
            self.findElement(_locators.USERS_LIST_ROLE_Dropdown_Button).click()
        except:
            print("Error:ClickRoleDropdown- Can't find element: " + _locators.USERS_LIST_ROLE_Dropdown_Button)
            return False

    def ClickDivisionDropdown(self):
        try:
            self.findElement(_locators.USERS_LIST_ROLE_Division_Button).click()
        except:
            print("Error:ClickDivisionDropdown- Can't find element: " + _locators.USERS_LIST_ROLE_Division_Button)
            return False

    def ClickSiteDropdownOnUsersListPage(self):
        try:
            self.findElement(_locators.USERS_LIST_SITE_Dropdown_Button).click()
        except:
            print("Error:ClickSiteDropdownOnUsersListPage- Can't find element: " + _locators.USERS_LIST_SITE_Dropdown_Button)
            return False

    def GetDropDownOptionTextAdmin(self):
        text1 = self.findElement(_locators.USERS_LIST_ROLE_Dropdown_Selection_None).text
        text2 = self.findElement(_locators.USERS_LIST_ROLE_Dropdown_Selection_Admin).text
        text3 = self.findElement(_locators.USERS_LIST_ROLE_Dropdown_Selection_Partner).text
        text4 = self.findElement(_locators.USERS_LIST_ROLE_Dropdown_Selection_Client).text
        return (text1, text2, text3, text4)

    def GetDropDownOptionTextAdminP(self):
        text1 = self.findElement(_locators.USERS_LIST_ROLE_Dropdown_Selection_None).text
        text2 = self.findElement(_locators.USERS_LIST_ROLE_Dropdown_Selection_PartnerP).text
        text3 = self.findElement(_locators.USERS_LIST_ROLE_Dropdown_Selection_ClientP).text
        return (text1, text2, text3)

    def GetDivisionDropDownOptionTextsP(self):
        text1 = self.findElement(_locators.USERS_LIST_DIVISION_Dropdown_Selection_NoneP).text
        text2 = self.findElement(_locators.USERS_LIST_DIVISION_Dropdown_Selection_AtlanticP).text
        text3 = self.findElement(_locators.USERS_LIST_DIVISION_Dropdown_Selection_CentralNorthP ).text
        text4 = self.findElement(_locators.USERS_LIST_DIVISION_Dropdown_Selection_Mid_AmerP ).text
        text5 = self.findElement(_locators.USERS_LIST_DIVISION_Dropdown_Selection_NortheastP ).text
        text6 = self.findElement(_locators.USERS_LIST_DIVISION_Dropdown_Selection_SoutheastP).text
        text7 = self.findElement(_locators.USERS_LIST_DIVISION_Dropdown_Selection_WestP).text
        return (text1, text2, text3, text4, text5, text6, text7)


    def TableHeaderIsCorrect(self, roleType):
        locator = _locators.USER_LIST_Table_Header
        if roleType == 'partner':
            expectedText = "Users with role Partner Administrator"
        else:
            expectedText = "Users with role ANX Administrator"
        try:
            element = self.findElement(locator)
            return element.text == expectedText
        except:
            print("Error:TableHeaderIsCorrect() - Can't find element: " + locator)
            return False


    def SelectRoleP(self, roleType):
        if roleType == 'partner':
            locator = _locators.USERS_LIST_ROLE_Dropdown_Selection_PartnerP
        else:
            locator = _locators.USERS_LIST_ROLE_Dropdown_Selection_ClientP
        try:
            self.findElement(locator).click()
        except:
            print("Error:SelectRoleP() - Can't find element: " + locator)
            return False

    def SelectDivisionP(self, division):
        if division == 'Southeast':
            locator = _locators.USERS_LIST_DIVISION_Dropdown_Selection_SoutheastP
        else:
            print("SW ERROR: " + division + " not supported yet.")
            return False
        try:
            self.findElement(locator).click()
        except:
            print("Error:SelectRoleP() - Can't find element: " + locator)
            return False

    def SelectSiteP(self, site):
        site = "\'" + site + "\'"

        try:
            elements = self.findElementsByText(site)
            elements[0].click()
        except:
            print("Error:SelectSiteP() - Can't find element for site " + site)
            return False

    def GoButtonExists(self):
        try:
            return(self.findElement(_locators.USERS_PAGE_Go_Button).is_displayed())
        except:
            print("Error::GoButtonExists() Locator: " + _locators.USERS_PAGE_Go_Button)
            return False

    def GoButtonEnabled(self):
        try:
            return self.findElement(_locators.USERS_PAGE_Go_Button).is_enabled()
        except:
            print("Error::GoButtonEnabled().  Locator: " + _locators.USERS_PAGE_Go_Button)
            return False

    def StatusPage_SelectLab(self, LabName):
        try:
            self.findElement(_locators.STATUS_PAGE_Lab_Dropdown_Button).click()
            locator = _locators.STATUS_PAGE_Dropdown_Beg + LabName + _locators.STATUS_PAGE_Dropdown_End
            self.findElement(locator).click()
            time.sleep(2)
        except:
            print("Error:ClickRoleDropdown- Can't find element: " + _locators.STATUS_PAGE_Lab_Dropdown_Button)
            return False

    def StatusPage_SelectDivision(self, DivisionName):
        try:
            self.findElement(_locators.STATUS_PAGE_Div_Dropdown_Button).click()
            locator = _locators.STATUS_PAGE_Dropdown_Beg + DivisionName + _locators.STATUS_PAGE_Dropdown_End
            self.findElement(locator).click()
        except:
            print("Error:StatusPage_SelectDivision()- Can't find element: " + locator)
            return False

    def DivsionLabelShows(self, DivisionName):
        try:
            locator = _locators.STATUS_PAGE_Division_Label
            element = self.findElement(locator)
            return element.text == DivisionName
        except:
            print("Error:DivsionLabelShows()- Can't find element: " + locator)
            return False

    def TotalNodesLabelShows(self, labelText):
        try:
            locator = _locators.STATUS_PAGE_Total_Nodes_Label
            element = self.findElement(locator)
            return element.text == labelText
        except:
            print("Error:TotalNodesLabelShows- Can't find element: " + locator)
            return False

    def IsViewNodesButtonShowingAndActive(self, buttonText):
        try:
            locator = _locators.STATUS_PAGE_View_Nodes_Button
            element = self.findElement(locator)
            if (element.text != buttonText):
                print("Element text: " + element.text + ", Expected text: " + buttonText)
            return element.text == buttonText
        except:
            print("Error:IsViewNodesButtonShowingAndActive()- Can't find element: " + locator)
            return False

    def IsLabelShowing(self, labelText):
        if (labelText == self.testdata.STATUS_PAGE_Total_Nodes_Label_Text):
            locator = _locators.STATUS_PAGE_Total_Nodes_Label
        elif (labelText == self.testdata.STATUS_PAGE_Nodes_Activated_Label_Text):
            locator = _locators.STATUS_PAGE_Nodes_Activated_Label
        elif (labelText == self.testdata.STATUS_PAGE_Online_Label_Text):
            locator = _locators.STATUS_PAGE_Online_Label
        elif (labelText == self.testdata.STATUS_PAGE_Offline_Short_Label_Text):
            locator = _locators.STATUS_PAGE_Offline_Short_Label
        elif (labelText == self.testdata.STATUS_PAGE_Offline_Long_Label_Text):
            locator = _locators.STATUS_PAGE_Offline_Long_Label
        elif (labelText == self.testdata.STATUS_PAGE_Nodes_Not_Activated_Label_Text):
            locator = _locators.STATUS_PAGE_Nodes_Not_Activated_Label
        elif (labelText == self.testdata.STATUS_PAGE_Nodes_With_Errors_Label_Text):
            locator = _locators.STATUS_PAGE_Nodes_With_Errors_Label
        else:
            print("Unknown label")
            return False
        try:
            element = self.findElement(locator)
            if (element.text != labelText):
                print("Element text: " + element.text + ", Expected text: " + labelText)
            return element.text == labelText
        except:
            print("Error:IsLabelShowing()- Can't find element: " + locator)
            return False

    def IsNumberShowing(self, labelText):
        if (labelText == self.testdata.STATUS_PAGE_Total_Nodes_Label_Text):
            locator = _locators.STATUS_PAGE_Total_Nodes_Number
        elif (labelText == self.testdata.STATUS_PAGE_Nodes_Activated_Label_Text):
            locator = _locators.STATUS_PAGE_Nodes_Activated_Number
        elif (labelText == self.testdata.STATUS_PAGE_Online_Label_Text):
            locator = _locators.STATUS_PAGE_Online_Number
        elif (labelText == self.testdata.STATUS_PAGE_Offline_Short_Label_Text):
            locator = _locators.STATUS_PAGE_Offline_Short_Number
        elif (labelText == self.testdata.STATUS_PAGE_Offline_Long_Label_Text):
            locator = _locators.STATUS_PAGE_Offline_Long_Number
        elif (labelText == self.testdata.STATUS_PAGE_Nodes_Not_Activated_Label_Text):
            locator = _locators.STATUS_PAGE_Nodes_Not_Activated_Number
        elif (labelText == self.testdata.STATUS_PAGE_Nodes_With_Errors_Label_Text):
            locator = _locators.STATUS_PAGE_Nodes_With_Errors_Number
        else:
            print("Error: IsNumberShowing(): Unknown label")
            return False
        try:
            element = self.findElement(locator)
            intElement = int(element.text)
            if (intElement >= 0) and (intElement<1500):
                return True
            else:
                print("Error:IsNumberShowing()- Number out of range: %d", locator)
                return False
        except:
            print("Error:IsNumberShowing()- Can't find element: " + locator)
            return False


    def TotalNodesEqualActivatedPlusInactivatedNodes(self):
        try:
            totalNodes = int(self.findElement(_locators.STATUS_PAGE_Total_Nodes_Number).text)
            activatedNodes = int(self.findElement(_locators.STATUS_PAGE_Nodes_Activated_Number).text)
            unactivatedNodes = int(self.findElement(_locators.STATUS_PAGE_Nodes_Not_Activated_Number).text)
            if totalNodes != (activatedNodes+unactivatedNodes):
                print("Error::TotalNodesEqualActivatedPlusInactivatedNodes(): TotalNodes: %d, activatedNodes: %d, unactivatedNodes:%d", totalNodes, activatedNodes, unactivatedNodes)
            return totalNodes == (activatedNodes+unactivatedNodes)
        except:
            print("Error:TotalNodesEqualActivatedPlusInactivatedNodes()")
            return False

    def ActivatedNodesEqualOnlinePlusOffline(self):
        try:
            activatedNodes = int(self.findElement(_locators.STATUS_PAGE_Nodes_Activated_Number).text)
            onlineNodes = int(self.findElement(_locators.STATUS_PAGE_Online_Number).text)
            offlineShortNodes = int(self.findElement(_locators.STATUS_PAGE_Offline_Short_Number).text)
            offlineLongNodes = int(self.findElement(_locators.STATUS_PAGE_Offline_Long_Number).text)
            if activatedNodes != (onlineNodes + offlineShortNodes + offlineLongNodes):
                print("Error::ActivatedNodesEqualOnlinePlusOffline(): ActivatedNodes, online Nodes, offline short, offlinelong: ", activatedNodes, onlineNodes, offlineShortNodes, offlineLongNodes )
            return activatedNodes == (onlineNodes + offlineShortNodes + offlineLongNodes)
        except:
            print("Error:ActivatedNodesEqualOnlinePlusOffline()")
            return False

#                         _webPortal.ActivatedNodesEqualOnlinePlusOffline()


class Eyeballs:
    def  __init__(self):
        self.Eye_object = Eyes()
        self.Eye_object.api_key = 'o9td1ASLhzIOi6GCUGOPcTuUTBNzyyQAdFtwgoJhjLc110'
        #self.Eye_object.save_failed_tests = True

    def openEyes(self, driver):
        #returns new webdriver
        return self.Eye_object.open(driver=driver, app_name='Applitools', test_name='Test Web Page', viewport_size={'width': 1024, 'height': 768})

    def closeEyes(self):
        self.Eye_object.close()

    def abortEyesIfNotClosed(self):
        self.Eye_object.abort_if_not_closed()

    def check_window(self, pageName):
        self.Eye_object.check_window(pageName)

class PPro_Portal(Portal):

    def dummy(self):
        print("Dummy")

