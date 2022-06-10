import configparser


config = configparser.ConfigParser()
config.read('QA_Final_work/configs/config.ini')

username_true_adm = config.get("admin_info", "username_adm")
password_true_adm = config.get("admin_info", "password_adm")
#password_false_adm = config.get("admin_info", "password_false_adm")

username_true_user = config.get("user_info", "username_user")
password_true_user = config.get("user_info", "password_user")
#password_false_user = config.get("user_info", "password_false_user")



# search_bar = config.get("main_page", "search_bar")
# search_string = config.get("main_page", "search_str")
# tabs_names = config.get("main_page", "tabs_names")
# account_info = config.get("login_page", "account_info")
# error_text = config.get("login_page", "error_text")
# cart_empty = config.get("cart_page", "cart_empty")
# quantity = config.get("cart_page", "quantity_of_goods")
