import configparser


config = configparser.ConfigParser()
config.read('QA_Final_work/configs/config.ini')

username_adm = config.get("admin_info", "username_adm")
password_adm = config.get("admin_info", "password_adm")
#password_false_adm = config.get("admin_info", "password_false_adm")

username_user = config.get("user_info", "username_user")
password_user = config.get("user_info", "password_user")
#password_false_user = config.get("user_info", "password_false_user")


