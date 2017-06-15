__author__ = 'horlicke'

debug = False

class Testdata:
    #login data
    USERNAME    = "qa_admin_user"
    PASSWORD    = "password"
    ROLE        = "admin"

    BAD_PASSWORD = "verybadpw"

    TEST_RAIL_URL  = "https://anx.testrail.com"
    TEST_RAIL_USER = "horlicke@anx.com"
    TEST_RAIL_PW   = "ANX123$"

    #GET with Shellshock hack
    HTTP_GET_MESSAGE = ("GET / HTTP/1.1\r\n"
           "Host: webtop.positivenetworks.net\r\n"
           "Connection: keep-alive\r\n"
           "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8\r\n"
           "Upgrade-Insecure-Requests: 1\r\n"
           "User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36\r\n"
           "Accept-Encoding: gzip, deflate, sdch\r\n"
           "Accept-Language: () { :; }; /bin/bash -c \'cd /tmp;touch tempo.txt;cat tempo.txt > eddie.txt'\r\n"
           "\r\n"
           )

    SERVER_HOST = "192.168.50.171"
    SERVER_PORT = 80

    #REST_WEBSERVICE_URL = "http://api.openweathermap.org/data/2.5/forecast/city?q=Cary%2C+NC&id=524901&APPID=e31e364ee359ec61df04412552301ced"
    WEATHER_WEBSERVICE_URL_FOR_TESTING = "http://api.openweathermap.org/data/2.5/forecast?q=london&id=524901&APPID=e31e364ee359ec61df04412552301ced"

    def __init__(self, product):
        self.product = product
        if (debug):
            print("Init testdata object, product = " + product)


class MedNx_Testdata(Testdata):
    #PORTAL_URL  = "http://autoprintqa.anx.com:28080/login"
    #USERNAME    = "uTestAdmin"
    #PASSWORD    = "Password99"
    #CLIENT_USERNAME    = "AutoClientUser"
    #CLIENT_PASSWORD    = "Password99"
    #PORTAL_URL  = "http://barracuda-pp.anx.com:28080/autoprint/login"
    #PORTAL_URL  = "http://autoprintqa.anx.com:28080/login"
    PORTAL_URL  = "http://192.168.54.8:28080/login"
    CLIENT_USERNAME   = "AutoClientUser"
    CLIENT_PASSWORD   = "Password99"
    #CLIENT_USERNAME   = "Jason_Client"
    #CLIENT_PASSWORD   = "MedNX2015"
    ADMIN_USERNAME    = "uTestAdmin"
    ADMIN_PASSWORD    = "Password99"
    PARTNER_USERNAME  = "AutoPartnerUser"
    PARTNER_PASSWORD = "Password99"

#Pre-production DB
    DB_USERNAME = 'report_ro'
    DB_HOST     = '192.168.54.136'
    DB_NAME     = 'autoprint'
    DB_PASSWORD = 'APReport14'

#QA DB
    DB_USERNAME = 'autoprintUser'
    DB_HOST     = '192.168.54.5'
    DB_NAME     = 'autoprint'
    DB_PASSWORD = 'Admin123'

    USER_ROLE_SELECT_ROLE_TEXT = "Select Role..."
    USER_ROLE_ADMIN_TEXT       = "ANX Administrator"
    USER_ROLE_PARTNER_TEXT     = "Partner Administrator"
    USER_ROLE_CLIENT_TEXT      = "Client"

    #tenant/partners
    STATUS_PAGE_Labcorp                        = "Labcorp"

    #Division
    STATUS_PAGE_Southeast                      = "Southeast"
    STATUS_PAGE_Atlantic                       = "Atlantic"
    STATUS_PAGE_West                           = "West"
    STATUS_PAGE_Northeast                      = "Northeast"
    STATUS_PAGE_Mid_America                    = "Mid-America"
    STATUS_PAGE_Central_North                  = "Central North"
    USER_DIVISION_SELECT_ROLE_TEXT             = "Select Division..."

    #tenant/partners
    STATUS_PAGE_ANXLabs                        = "ANXLabs"

    #Divisions
    STATUS_PAGE_US_Atlantic                    = "US Atlantic"
    STATUS_PAGE_US_Central_North               = "US Central North"
    STATUS_PAGE_US_Mid_America                 = "US Mid-America"
    STATUS_PAGE_US_Northeast                   = "US Northeast"
    STATUS_PAGE_US_Southeast                   = "US Southeast"
    STATUS_PAGE_US_West                        = "US West"

    USER_DIVISION_SELECT_ROLE_TEXT             = "Select Division..."

    LABCORP_SITE_Under_Test                    = "00_OpenText_Test_Site"

    STATUS_PAGE_Total_Nodes_Label_Text         = "Total Nodes"
    STATUS_PAGE_Nodes_Activated_Label_Text     = "Nodes Activated"
    STATUS_PAGE_Online_Label_Text              = "Online"
    STATUS_PAGE_Offline_Short_Label_Text       = "Offline > 20 min & < 3 days"
    STATUS_PAGE_Offline_Long_Label_Text        = "Offline => 3 days"
    STATUS_PAGE_Nodes_Not_Activated_Label_Text = "Nodes Not Activated"
    STATUS_PAGE_Nodes_With_Errors_Label_Text   = "Nodes with Errors Last 24 Hours"
    STATUS_PAGE_View_Nodes_Button_Text         = "View Nodes"

    USER_LIST_First_Name_Header = "First Name"
    USER_LIST_Last_Name_Header  = "Last Name"
    USER_LIST_User_Name_Header  = "Username"
    USER_LIST_Role_Header       = "Role"
    USER_LIST_Phone_Header      = "Telephone"
    USER_LIST_Email_Header      = "Email"

    USERS_LIST_MAIN_BREADCRUMB_TEXT    = "Users"
    USERS_LIST_SECOND_BREADCRUMB_TEXT  = "List"

#use for 1.3 (Non multitenancy version)
class MedNx_Testdata_1_3(Testdata):
    #PORTAL_URL  = "http://autoprintqa.anx.com:28080/login"
    #USERNAME    = "uTestAdmin"
    #PASSWORD    = "Password99"
    #CLIENT_USERNAME    = "AutoClientUser"
    #CLIENT_PASSWORD    = "Password99"
    PORTAL_URL  = "http://barracuda-pp.anx.com:28080/autoprint/login"
    #PORTAL_URL  = "http://autoprintqa.anx.com:28080/login"
    CLIENT_USERNAME   = "AutoClientUser"
    CLIENT_PASSWORD   = "Password99"
    #CLIENT_USERNAME   = "Jason_Client"
    #CLIENT_PASSWORD   = "MedNX2015"
    ADMIN_USERNAME    = "uTestAdmin"
    ADMIN_PASSWORD    = "Password99"
    PARTNER_USERNAME  = "AutoPartnerUser"
    PARTNER_PASSWORD = "Password99"

    DB_USERNAME = 'report_ro'
    DB_HOST     = '192.168.54.136'
    DB_NAME     = 'autoprint'
    DB_PASSWORD = 'APReport14'

    USER_ROLE_SELECT_ROLE_TEXT = "Select role..."
    USER_ROLE_ADMIN_TEXT       = "ANX Administrator"
    USER_ROLE_PARTNER_TEXT     = "Partner Administrator"
    USER_ROLE_CLIENT_TEXT      = "Client"

    USERS_LIST_MAIN_BREADCRUMB_TEXT    = "Users"
    USERS_LIST_SECOND_BREADCRUMB_TEXT  = "List"


class PPro_Testdata(Testdata):
    PORTAL_URL = "http://192.168.50.166"
    USERNAME    = "qa_admin_user_PPro"
    PASSWORD    = "password_PPro"


#def assignTestData(product):
#    if (product == "MedNx"):
#        return MedNx_Testdata
#    elif (product == "PPro"):
#        return PPro_Testdata
#    else:
#        return Testdata

