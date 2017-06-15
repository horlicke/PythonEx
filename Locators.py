__author__ = 'horlicke'

class MedNx_Locators():
    #### login page locators
    LOGIN_PAGE_Login_Button        = ".login_btn"
    LOGIN_PAGE_Username_Edit_Field = "#username_id"
    LOGIN_PAGE_Password_Edit_Field = "#password_id"
    LOGIN_PAGE_ANX_Login_Logo      = "#login_logo"
    LOGIN_PAGE_ANX_Main_Image      = ".login_left"
    LOGIN_PAGE_ANX_Error_Text      = ".errors"
    LOGIN_PAGE_Invalid_Login_Text  = "html/body/div[2]/div/div[3]/form/div/div/p"

    #landing page locators
    #LANDING_PAGE_breadcrumb = "html/body/table/tbody/tr/td[1]/div/div/div[2]/h1/a"
    LANDING_PAGE_breadcrumb = ".breadcrumb"
    FIRST_LEVEL_BREADCRUMB = "html/body/div[3]/div/div[1]/div/ol/li[1]/a"
    SECOND_LEVEL_BREADCRUMB = "html/body/div[3]/div/div[1]/div/ol/li[2]/a"


    LANDING_PAGE_Logout_Button ="html/body/div[2]/div/div/div[2]/p[1]/a"

    #navigation bar locators
    # html/body/table/tbody/tr/td[1]/div/div/div[1]/div[2]/ul/li[1]/a   or .current>a
    NAV_BAR_Users_Button = "html/body/div[2]/div/div/div[2]/ul/li[1]/a"
    NAV_BAR_Users_Button_List = "html/body/div[2]/div/div/div[2]/ul/li[1]/ul/li[1]/a"
    NAV_BAR_Users_Button_Add = "html/body/div[2]/div/div/div[2]/ul/li[1]/ul/li[2]/a"
    NAV_BAR_Sites_Button = "html/body/div[2]/div/div/div[2]/ul/li[2]/a"
    NAV_BAR_Sites_Button_List = "html/body/div[2]/div/div/div[2]/ul/li[2]/ul/li[1]/a"
    NAV_BAR_Site_Button_Add = "html/body/div[2]/div/div/div[2]/ul/li[2]/ul/li[2]/a"
    NAV_BAR_Reports_Button = "html/body/div[2]/div/div/div[2]/ul/li[4]/a"
    NAV_BAR_Status_Button = "html/body/div[2]/div/div/div[2]/ul/li[5]/a"
    NAV_BAR_Search_Button = "html/body/div[2]/div/div/div[2]/ul/li[6]/a"
    NAV_BAR_Print_Stream_Button = "html/body/div[2]/div/div/div[2]/ul/li[3]/a"

    CLIENT_NAV_BAR_Reports_Button = "html/body/div[2]/div/div/div[2]/ul/li[4]/a"
    CLIENT_NAV_BAR_Status_Button = "html/body/div[2]/div/div/div[2]/ul/li[5]/a"
    CLIENT_NAV_BAR_Search_Button = "html/body/div[2]/div/div/div[2]/ul/li[6]/a"

    USERS_LIST_ROLE_Dropdown_Button = "html/body/div[3]/div/div[2]/div/div/div/form/div/div[1]/div/div/button"
    USERS_LIST_ROLE_Dropdown_Selection_None = "html/body/div[3]/div/div[2]/div/div/div/form/div/div[1]/div/ul/li[1]/a"
    USERS_LIST_ROLE_Dropdown_Selection_Admin = "html/body/div[3]/div/div[2]/div/div/div/form/div/div[1]/div/ul/li[2]/a"
    USERS_LIST_ROLE_Dropdown_Selection_Partner = "html/body/div[3]/div/div[2]/div/div/div/form/div/div[1]/div/ul/li[3]/a"
    USERS_LIST_ROLE_Dropdown_Selection_Client = "html/body/div[3]/div/div[2]/div/div/div/form/div/div[1]/div/ul/li[4]/a"
    USERS_LIST_ROLE_Dropdown_Selection_PartnerP = "html/body/div[3]/div/div[2]/div/div/div/form/div/div[1]/div/ul/li[2]/a"
    USERS_LIST_ROLE_Dropdown_Selection_ClientP = "html/body/div[3]/div/div[2]/div/div/div/form/div/div[1]/div/ul/li[3]/a"
    USER_LIST_Table_Header = "html/body/div[3]/div/div[3]/div/div/header/h1"
    USER_LIST_Table_Add_Button = "html/body/div[3]/div/div[3]/div/div/header/div/button"
    USER_LIST_Table_FirstName_Header = "html/body/div[3]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div[1]/div[2]/div[1]/div[1]"
    USER_LIST_Table_LastName_Header =  "html/body/div[3]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div[2]/div[2]/div[1]/div[1]"
    USER_LIST_Table_UserName_Header =  "html/body/div[3]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div[3]/div[2]/div[1]/div[1]"
    USER_LIST_Table_Role_Header     =  "html/body/div[3]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div[4]/div[2]/div[1]/div[1]"
    USER_LIST_Table_Phone_Header    =  "html/body/div[3]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div[5]/div[2]/div[1]/div[1]"
    USER_LIST_Table_Email_Header    =  "html/body/div[3]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div[6]/div[2]/div[1]/div[1]"
    USER_LIST_Table_Blank_Header    =  "html/body/div[3]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div[7]/div[2]/div[1]/div[1]"
    USER_LIST_Table_FirstName_Filter_Button = "html/body/div[3]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div[1]/div[2]/div[1]/div[1]/div"
    USER_LIST_Table_LastName_Filter_Button = "html/body/div[3]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div"
    USERS_LIST_ROLE_Division_Button = "html/body/div[3]/div/div[2]/div/div/div/form/div/div[3]/div/div/button"
    USERS_LIST_DIVISION_Dropdown_Selection_NoneP          = "html/body/div[3]/div/div[2]/div/div/div/form/div/div[3]/div/ul/li[1]/a"
    USERS_LIST_DIVISION_Dropdown_Selection_AtlanticP      = "html/body/div[3]/div/div[2]/div/div/div/form/div/div[3]/div/ul/li[2]/a"
    USERS_LIST_DIVISION_Dropdown_Selection_CentralNorthP  = "html/body/div[3]/div/div[2]/div/div/div/form/div/div[3]/div/ul/li[3]/a"
    USERS_LIST_DIVISION_Dropdown_Selection_Mid_AmerP      = "html/body/div[3]/div/div[2]/div/div/div/form/div/div[3]/div/ul/li[4]/a"
    USERS_LIST_DIVISION_Dropdown_Selection_NortheastP     = "html/body/div[3]/div/div[2]/div/div/div/form/div/div[3]/div/ul/li[5]/a"
    USERS_LIST_DIVISION_Dropdown_Selection_SoutheastP     = "html/body/div[3]/div/div[2]/div/div/div/form/div/div[3]/div/ul/li[6]/a"
    USERS_LIST_DIVISION_Dropdown_Selection_WestP          = "html/body/div[3]/div/div[2]/div/div/div/form/div/div[3]/div/ul/li[7]/a"
    USERS_LIST_SITE_Dropdown_Button = "html/body/div[3]/div/div[2]/div/div/div/form/div/div[4]/div/div/button"
    USERS_PAGE_Go_Button = "html/body/div[3]/div/div[2]/div/div/div/form/div/div[6]/div/button"

    STATUS_PAGE_Lab_Dropdown_Button = "html/body/div[3]/div[2]/div/div/div/form/div/div[2]/div/div/button"
    STATUS_PAGE_Dropdown_Beg = "//a[contains(text(), '"
    STATUS_PAGE_Dropdown_End = "')]"
    STATUS_PAGE_Div_Dropdown_Button       = "html/body/div[3]/div[2]/div/div/div/form/div/div[3]/div/div/button"
    STATUS_PAGE_Division_Label            = "html/body/div[3]/div[3]/div/div/header/h1/span"
    STATUS_PAGE_Total_Nodes_Label         = "html/body/div[3]/div[3]/div/div/div/div/div/div/div[2]/div[1]/div[1]"
    STATUS_PAGE_Nodes_Activated_Label     = "html/body/div[3]/div[3]/div/div/div/div/div/div/div[2]/div[2]/div[1]"
    STATUS_PAGE_Online_Label              = "html/body/div[3]/div[3]/div/div/div/div/div/div/div[2]/div[3]/div"
    STATUS_PAGE_Offline_Short_Label       = "html/body/div[3]/div[3]/div/div/div/div/div/div/div[2]/div[4]/div"
    STATUS_PAGE_Offline_Long_Label        = "html/body/div[3]/div[3]/div/div/div/div/div/div/div[2]/div[5]/div"
    STATUS_PAGE_Nodes_Not_Activated_Label = "html/body/div[3]/div[3]/div/div/div/div/div/div/div[2]/div[6]/div"
    STATUS_PAGE_Nodes_With_Errors_Label   = "html/body/div[3]/div[3]/div/div/div/div/div/div/div[2]/div[7]/div"
    STATUS_PAGE_View_Nodes_Button         = "html/body/div[3]/div[3]/div/div/header/div/button"

    STATUS_PAGE_Total_Nodes_Number          = "html/body/div[3]/div[3]/div/div/div/div/div/div/div[2]/div[1]/div[2]"
    STATUS_PAGE_Nodes_Activated_Number      = "html/body/div[3]/div[3]/div/div/div/div/div/div/div[2]/div[2]/div[2]"
    STATUS_PAGE_Online_Number               = "html/body/div[3]/div[3]/div/div/div/div/div/div/div[2]/div[3]/a/div"
    STATUS_PAGE_Offline_Short_Number        = "html/body/div[3]/div[3]/div/div/div/div/div/div/div[2]/div[4]/a/div"
    STATUS_PAGE_Offline_Long_Number         = "html/body/div[3]/div[3]/div/div/div/div/div/div/div[2]/div[5]/a/div"
    STATUS_PAGE_Nodes_Not_Activated_Number  = "html/body/div[3]/div[3]/div/div/div/div/div/div/div[2]/div[6]/a/div"
    STATUS_PAGE_Nodes_With_Errors_Number    = "html/body/div[3]/div[3]/div/div/div/div/div/div/div[2]/div[7]/a/div"

class MedNx_Locators_1_3():
    #### login page locators
    LOGIN_PAGE_Login_Button        = ".login_btn"
    LOGIN_PAGE_Username_Edit_Field = "#username_id"
    LOGIN_PAGE_Password_Edit_Field = "#password_id"
    LOGIN_PAGE_ANX_Login_Logo      = "#login_logo"
    LOGIN_PAGE_ANX_Main_Image      = ".login_left"
    LOGIN_PAGE_ANX_Error_Text      = ".errors"
    LOGIN_PAGE_Invalid_Login_Text  = "html/body/div[1]/div/div[3]/form/div/div/p"

    #landing page locators
    #LANDING_PAGE_breadcrumb = "html/body/table/tbody/tr/td[1]/div/div/div[2]/h1/a"
    LANDING_PAGE_breadcrumb = "#breadcrumb"
    LANDING_PAGE_Logout_Button =".logout"

    FIRST_LEVEL_BREADCRUMB = "html/body/div[3]/div/div[1]/div/ol/li[1]/a"
    SECOND_LEVEL_BREADCRUMB = "html/body/div[3]/div/div[1]/div/ol/li[2]/a"

    #navigation bar locators
    # html/body/table/tbody/tr/td[1]/div/div/div[1]/div[2]/ul/li[1]/a   or .current>a
    NAV_BAR_Users_Button = ".current>a"
    NAV_BAR_Sites_Button = "html/body/table/tbody/tr/td[1]/div/div/div[1]/div[2]/ul/li[2]/a"
    NAV_BAR_Reports_Button = "html/body/table/tbody/tr/td[1]/div/div/div[1]/div[2]/ul/li[3]/a"
    NAV_BAR_Status_Button = "html/body/table/tbody/tr/td[1]/div/div/div[1]/div[2]/ul/li[4]/a"
    NAV_BAR_Search_Button = "html/body/table/tbody/tr/td[1]/div/div/div[1]/div[2]/ul/li[5]/a"

    USERS_LIST_ROLE_Dropdown_Button = ".k-icon.k-i-arrow-s"
    USERS_LIST_ROLE_Dropdown_Selection_None = "html/body/div[1]/div/ul/li[1]"
    USERS_LIST_ROLE_Dropdown_Selection_Admin = "html/body/div[1]/div/ul/li[2]"
    USERS_LIST_ROLE_Dropdown_Selection_Partner = "html/body/div[1]/div/ul/li[3]"
    USERS_LIST_ROLE_Dropdown_Selection_Client = "html/body/div[1]/div/ul/li[4]"

    USERS_PAGE_Go_Button = "html/body/table/tbody/tr/td[1]/div/div/div[3]/div/button"

class PPro_Locators():
    #### login page locators
    LOGIN_PAGE_Login_Button        = "html/body/center/form/table/tbody/tr[2]/td/table/tbody/tr[5]/td/input"
    LOGIN_PAGE_Username_Edit_Field = "#userName"
    LOGIN_PAGE_Password_Edit_Field = "#password"

