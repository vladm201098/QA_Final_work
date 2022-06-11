import configparser


config = configparser.ConfigParser()
config.read('QA_Final_work/configs/config.ini')

# admin_info
username_adm = config.get("admin_info", "username_adm")
password_adm = config.get("admin_info", "password_adm")
# user_info
username_user = config.get("user_info", "username_user")
password_user = config.get("user_info", "password_user")
# group
name_group = config.get('group', "name_group")
# logout
logout_text = config.get('logout', 'logout_info')
# welcome
welcome_admin = config.get('welcome', 'welcome_admin')
welcome_user = config.get('welcome', 'welcome_user')

