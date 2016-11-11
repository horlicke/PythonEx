__author__ = 'horlicke'

class MedNx_Locators():
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

