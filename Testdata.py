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
    TEST_RAIL_PW   = "S1lverado$"

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

    REST_WEBSERVICE_URL = "http://api.openweathermap.org/data/2.5/forecast/city?q=Cary%2C+NC&id=524901&APPID=e31e364ee359ec61df04412552301ced"


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
    PORTAL_URL  = "http://barracuda-pp.anx.com:28080/autoprint/login"
    #PORTAL_URL  = "http://autoprintqa.anx.com:28080/autoprint/login"
    CLIENT_USERNAME   = "Jason_Client"
    CLIENT_PASSWORD   = "MedNX2015"
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

