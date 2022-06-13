import configparser


config = configparser.ConfigParser()
config.read('/home/vladislav/QA_Final_work/configs/config.ini')

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
logout_page = config.get('logout', 'logout_page')
# welcome
welcome_admin = config.get('welcome', 'welcome_admin')
welcome_user = config.get('welcome', 'welcome_user')
# date and time
datetime = config.get('date_and_time', 'datetime_first_post_img')
# admin page
go_to_admin = config.get('main_page', 'go_to_admin')