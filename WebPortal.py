__author__ = 'horlicke'
import Locators
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from applitools.eyes import Eyes
import time

debug = False
############################################################
### Parent portal class
############################################################
class Portal:
    def __init__(self, browser, product, url):
        self.browser = browser
        self.product = product
        self.url     = url


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


## MedNx Portal classe, inherits from Portal class
class MedNx_Portal(Portal):

    def OnLandingPage(self, userType):
        if userType == 'client':
            breadcrumbString = "Node Status"
        else:
            breadcrumbString = "Status"

        try:
            element = self.findElement(_locators.LANDING_PAGE_breadcrumb)
            return element.text == breadcrumbString
        except:
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

    def GoToUsersPage(self):
        try:
            self.findElement(_locators.NAV_BAR_Users_Button).click()
        except:
            return False

    def GoToSitesPage(self):
        try:
            self.findElement(_locators.NAV_BAR_Sites_Button).click()
        except:
            return False

    def GoToReportsPage(self):
        try:
            self.findElement(_locators.NAV_BAR_Reports_Button).click()
        except:
            return False

    def GoToStatusPage(self):
        try:
            self.findElement(_locators.NAV_BAR_Status_Button).click()
        except:
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

    def ClickRoleDropdown(self):
        try:
            self.findElement(_locators.USERS_LIST_ROLE_Dropdown_Button).click()
        except:
            return False

    def GetDropDownOptionTextAdmin(self):
        text1 = self.findElement(_locators.USERS_LIST_ROLE_Dropdown_Selection_None).text
        text2 = self.findElement(_locators.USERS_LIST_ROLE_Dropdown_Selection_Admin).text
        text3 = self.findElement(_locators.USERS_LIST_ROLE_Dropdown_Selection_Partner).text
        text4 = self.findElement(_locators.USERS_LIST_ROLE_Dropdown_Selection_Client).text
        return (text1, text2, text3, text4)


    def SelectRole(self, roleType):
        if roleType == 'admin':
            locator = _locators.USERS_LIST_ROLE_Dropdown_Selection_Admin
        elif roleType == 'client':
            locator = _locators.USERS_LIST_ROLE_Dropdown_Selection_Client
        else:
            locator = _locators.USERS_LIST_ROLE_Dropdown_Selection_Partner
        try:
            self.findElement(_locators.USERS_LIST_ROLE_Button).click()
        except:
            return False

    def GoButtonExists(self):
        try:
            return(self.findElement(_locators.USERS_PAGE_Go_Button).is_displayed())
        except:
            return False

    def GoButtonEnabled(self):
        try:
            return (self.findElement(_locators.USERS_PAGE_Go_Button).is_enabled())
        except:
            return False

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

