import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import schedule
import yaml
import random
from selenium.webdriver.common.action_chains import ActionChains
import logging

logging.basicConfig(filename="log.txt", level=logging.DEBUG, format="%(asctime)s %(message)s")

def credentials():
    with open('credentials.yml', 'r') as f:
        try:
            logging.debug("credential file opened...")
            data = str(yaml.safe_load(f)).split("'")
            User = data[5]
            Pass = data[9]
            login_hint = data[13]
            restaurant_name = data[17]
            HACCPA_TIME = str(data[21])
            HACCPB_TIME = str(data[25])
            HACCPC_TIME = str(data[29])
            HACCPD_TIME = str(data[33])
            Daily_Travel_Path_AM_TIME = str(data[37])
            Daily_Travel_Path_PM_TIME = str(data[41])
            ManagerName = str(data[45])
            logging.debug("All credentials loaded...")
        except yaml.YAMLError as exc:
            print(exc)
            logging.error(exc)

    return User, Pass, login_hint, restaurant_name, HACCPA_TIME, HACCPB_TIME, HACCPC_TIME, HACCPD_TIME, Daily_Travel_Path_AM_TIME, Daily_Travel_Path_PM_TIME, ManagerName


def task():
    t1, t2, t3, t4, HACCPA_TIME, HACCPB_TIME, HACCPC_TIME, HACCPD_TIME, Daily_Travel_Path_AM_TIME, Daily_Travel_Path_PM_TIME, t5 = credentials()

# /-----------------------------------------------------HACCP log A----------------------------------------------------/
    # form id: 377033 and name: HACCP log A start
    def form_377033_LOGA():  # HACCP Log A (Opening)
        # /----------------------------------------------Restaurant login----------------------------------------------/
        userName, Password, login_hint, restaurant_name, temp1, temp2, temp3, temp4, temp5, temp6, ManagerName = credentials()
        logging.debug("form_377033_LOGA opened")
        print("#-------------Filling HACCP LOG A form-------------#")
        print(f"Restaurant number: {restaurant_name}")
        response = requests.post("https://www.zenput.com/get_sso_company_info/", json={"email": f"{login_hint}"})
        login_hint = login_hint.replace("@", "%40")
        inter_var = response.text
        x = inter_var.split(":")[7].split('"')[1]
        URL = f"https://zenput.auth0.com/authorize?client_id=vmFR5ePxkzh5UAJkijHZiKcZixJcERX6&connection=rbi-plk-prod&login_hint={login_hint}&sp_type=auth0&state={x}&scope=offline_access%20openid%20profile%20email&redirect_uri=https%3A%2F%2Fwww.zenput.com%2Fauth0_callback%2F&response_type=code&auth0Client=eyJuYW1lIjoiYXV0aDAuanMiLCJ2ZXJzaW9uIjoiOS4xMy4yIn0%3D"
        # print(f"URL: {URL}")
        driver = webdriver.Chrome()
        driver.get(URL)
        driver.find_element(By.ID, "okta-signin-username").send_keys(userName)
        driver.find_element(By.ID, "okta-signin-password").send_keys(Password)
        driver.find_element(By.ID, "okta-signin-submit").click()
        time.sleep(50)
        driver.find_element(By.XPATH, "//a[@id='oiw_btn']").click()
        time.sleep(20)
        # /----------------------------------------------Restaurant login----------------------------------------------/

        # form opening
        driver.find_element(By.XPATH, "//li//a[@class='navlink taskitem_container']//div[normalize-space()='HACCP Log A (Opening)']").click()
        time.sleep(20)
        driver.find_element(By.XPATH, "//div[@id='submit_form']").click()
        time.sleep(20)

        driver.find_element(By.XPATH, "//li[@id='field_215']//textarea").send_keys(ManagerName)
        time.sleep(1)
        # //li[@id='field_0']//div[2]//span
        driver.find_element(By.XPATH, "//li[@id='field_30']//input").send_keys(int(random.randint(34, 38)))
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_82']//input").send_keys(int(random.randint(34, 38)))
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_142']//input").send_keys(int(random.randint(34, 38)))
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_146']//input").send_keys(int(random.randint(34, 38)))
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_78']//input").send_keys(int(random.randint(34, 40)))
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_74']//input").send_keys(int(random.randint(34, 40)))
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_70']//input").send_keys(int(random.randint(34, 40)))
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_66']//input").send_keys(int(random.randint(-10, 0)))
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_62']//input").send_keys(int(random.randint(-10, 0)))
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_58']//input").send_keys(int(random.randint(160, 165)))
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_54']//input").send_keys(int(170))
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_50']//input").send_keys(int(340))
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_46']//input").send_keys(int(340))
        time.sleep(1)
        # driver.find_element(By.XPATH, "//li[@id='field_205']//input").send_keys(int(340))
        # driver.find_element(By.XPATH, "//li[@id='field_217']//input").send_keys(int(340))
        driver.find_element(By.XPATH, "//li[@id='field_42']//input").send_keys(int(340))
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_38']//input").send_keys(int(340))
        time.sleep(1)
        # driver.find_element(By.XPATH, "//li[@id='field_209']//input").send_keys(int(340))
        driver.find_element(By.XPATH, "//li[@id='field_34']//input").send_keys(int(340))
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_273']//input").send_keys(int(340))
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_222']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_228']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_224']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_223']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_157']//input").send_keys(int(random.randint(165, 169)))
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_161']//input").send_keys(int(random.randint(165, 169)))
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_165']//input").send_keys(int(random.randint(160, 170)))
        time.sleep(1)
        # driver.find_element(By.XPATH, "//li[@id='field_215']//textarea").send_keys("Abubakr")
        driver.find_element(By.XPATH, "//li[@id='field_169']//input").send_keys(int(random.randint(160, 170)))
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_173']//input").send_keys(int(random.randint(32, 38)))
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_179']//input").send_keys(int(random.randint(34, 40)))
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_183']//input").send_keys(int(random.randint(34, 40)))
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_187']//input").send_keys(int(random.randint(34, 38)))
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_193']//input").send_keys(int(random.randint(34, 40)))
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_197']//input").send_keys(int(random.randint(34, 40)))
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_268']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_272']//div//a//div[1]").click()  # button
        time.sleep(5)
        # div.signature_field
        canvas = driver.find_element(By.XPATH, "//div[@id='signature_base']//div[1]//div[@class = 'signature_field']")
        drawing = ActionChains(driver) \
            .click_and_hold(canvas) \
            .move_by_offset(-10, -15) \
            .move_by_offset(20, 32) \
            .move_by_offset(10, 25) \
            .release()
        drawing.perform()
        time.sleep(1)
        driver.find_element(By.XPATH, "//div[@id='signature_base']//a[2]").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//div[@id='submit_form']").click()  # button
        time.sleep(20)
        driver.close()
        logging.debug("form_377033_LOGA submitted")
        print("#-------------Successfully filled HACCP LOG A form-------------#")
    # form id: 377033 and name: HACCP log A end
# /-----------------------------------------------------HACCP log A----------------------------------------------------/

# /-----------------------------------------------------HACCP log B----------------------------------------------------/
    # form id: 377038 and name: HACCP log B start
    def form_377038_LOGB():  # HACCP Log B (Opening)
        # /----------------------------------------------Restaurant login----------------------------------------------/
        userName, Password, login_hint, restaurant_name, temp1, temp2, temp3, temp4, temp5, temp6, ManagerName = credentials()
        logging.debug("form_377038_LOGB opened")
        print("#-------------Filling HACCP LOG B form-------------#")
        print(f"Restaurant number: {restaurant_name}")
        response = requests.post("https://www.zenput.com/get_sso_company_info/", json={"email": f"{login_hint}"})
        login_hint = login_hint.replace("@", "%40")
        inter_var = response.text
        x = inter_var.split(":")[7].split('"')[1]
        URL = f"https://zenput.auth0.com/authorize?client_id=vmFR5ePxkzh5UAJkijHZiKcZixJcERX6&connection=rbi-plk-prod&login_hint={login_hint}&sp_type=auth0&state={x}&scope=offline_access%20openid%20profile%20email&redirect_uri=https%3A%2F%2Fwww.zenput.com%2Fauth0_callback%2F&response_type=code&auth0Client=eyJuYW1lIjoiYXV0aDAuanMiLCJ2ZXJzaW9uIjoiOS4xMy4yIn0%3D"
        # print(f"URL: {URL}")
        driver = webdriver.Chrome()
        driver.get(URL)
        driver.find_element(By.ID, "okta-signin-username").send_keys(userName)
        driver.find_element(By.ID, "okta-signin-password").send_keys(Password)
        driver.find_element(By.ID, "okta-signin-submit").click()
        time.sleep(50)
        driver.find_element(By.XPATH, "//a[@id='oiw_btn']").click()
        time.sleep(20)
        # /----------------------------------------------Restaurant login----------------------------------------------/

        # form opening
        driver.find_element(By.XPATH, "//li//a[@class='navlink taskitem_container']//div[normalize-space()='HACCP Log B']").click()
        time.sleep(20)
        driver.find_element(By.XPATH, "//div[@id='submit_form']").click()
        time.sleep(20)

        driver.find_element(By.XPATH, "//li[@id='field_213']//textarea").send_keys(ManagerName)
        time.sleep(1)
        # //li[@id='field_0']//div[2]//span
        driver.find_element(By.XPATH, "//li[@id='field_30']//input").send_keys(int(random.randint(34, 38)))
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_82']//input").send_keys(int(random.randint(34, 38)))
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_142']//input").send_keys(int(random.randint(34, 38)))
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_146']//input").send_keys(int(random.randint(34, 38)))
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_78']//input").send_keys(int(random.randint(34, 40)))
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_74']//input").send_keys(int(random.randint(34, 40)))
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_70']//input").send_keys(int(random.randint(34, 40)))
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_66']//input").send_keys(int(random.randint(-10, 0)))
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_62']//input").send_keys(int(random.randint(-10, 0)))
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_157']//input").send_keys(int(random.randint(165, 169)))
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_161']//input").send_keys(int(random.randint(165, 169)))
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_165']//input").send_keys(int(random.randint(160, 170)))
        time.sleep(1)
        # driver.find_element(By.XPATH, "//li[@id='field_215']//textarea").send_keys("Abubakr")
        driver.find_element(By.XPATH, "//li[@id='field_169']//input").send_keys(int(random.randint(160, 170)))
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_173']//input").send_keys(int(random.randint(32, 38)))
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_214']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_179']//input").send_keys(int(random.randint(34, 40)))
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_215']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_183']//input").send_keys(int(random.randint(34, 40)))
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_187']//input").send_keys(int(random.randint(34, 38)))
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_193']//input").send_keys(int(random.randint(34, 40)))
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_197']//input").send_keys(int(random.randint(34, 40)))
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_199']//div//a//div[1]").click()  # button
        time.sleep(5)
        # div.signature_field
        canvas = driver.find_element(By.XPATH, "//div[@id='signature_base']//div[1]//div[@class = 'signature_field']")
        drawing = ActionChains(driver) \
            .click_and_hold(canvas) \
            .move_by_offset(-10, -15) \
            .move_by_offset(20, 32) \
            .move_by_offset(10, 25) \
            .release()
        drawing.perform()
        time.sleep(1)
        driver.find_element(By.XPATH, "//div[@id='signature_base']//a[2]").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//div[@id='submit_form']").click()  # button
        time.sleep(20)
        driver.close()
        logging.debug("form_377038_LOGB submitted")
        print("#-------------Successfully filled HACCP LOG B form-------------#")
    # form id: 377038 and name: HACCP log B end
# /-----------------------------------------------------HACCP log B----------------------------------------------------/

# /-----------------------------------------------------HACCP log C----------------------------------------------------/
    # form id: 377423 and name: HACCP log C start
    def form_377423_LOGC():  # HACCP Log C (Opening)
        # /----------------------------------------------Restaurant login----------------------------------------------/
        userName, Password, login_hint, restaurant_name, temp1, temp2, temp3, temp4, temp5, temp6, ManagerName = credentials()
        logging.debug("form_377423_LOGC opened")
        print("#-------------Filling HACCP LOG C form-------------#")
        print(f"Restaurant number: {restaurant_name}")
        response = requests.post("https://www.zenput.com/get_sso_company_info/", json={"email": f"{login_hint}"})
        login_hint = login_hint.replace("@", "%40")
        inter_var = response.text
        x = inter_var.split(":")[7].split('"')[1]
        URL = f"https://zenput.auth0.com/authorize?client_id=vmFR5ePxkzh5UAJkijHZiKcZixJcERX6&connection=rbi-plk-prod&login_hint={login_hint}&sp_type=auth0&state={x}&scope=offline_access%20openid%20profile%20email&redirect_uri=https%3A%2F%2Fwww.zenput.com%2Fauth0_callback%2F&response_type=code&auth0Client=eyJuYW1lIjoiYXV0aDAuanMiLCJ2ZXJzaW9uIjoiOS4xMy4yIn0%3D"
        # print(f"URL: {URL}")
        driver = webdriver.Chrome()
        driver.get(URL)
        driver.find_element(By.ID, "okta-signin-username").send_keys(userName)
        driver.find_element(By.ID, "okta-signin-password").send_keys(Password)
        driver.find_element(By.ID, "okta-signin-submit").click()
        time.sleep(50)
        driver.find_element(By.XPATH, "//a[@id='oiw_btn']").click()
        time.sleep(20)
        # /----------------------------------------------Restaurant login----------------------------------------------/

        # form opening
        driver.find_element(By.XPATH, "//li//a[@class='navlink taskitem_container']//div[normalize-space()='HACCP Log C']").click()
        time.sleep(20)
        driver.find_element(By.XPATH, "//div[@id='submit_form']").click()
        time.sleep(20)

        driver.find_element(By.XPATH, "//li[@id='field_213']//textarea").send_keys(ManagerName)
        time.sleep(1)
        # //li[@id='field_0']//div[2]//span
        driver.find_element(By.XPATH, "//li[@id='field_30']//input").send_keys(int(random.randint(34, 38)))
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_82']//input").send_keys(int(random.randint(34, 38)))
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_142']//input").send_keys(int(random.randint(34, 38)))
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_146']//input").send_keys(int(random.randint(34, 38)))
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_78']//input").send_keys(int(random.randint(34, 40)))
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_74']//input").send_keys(int(random.randint(34, 40)))
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_70']//input").send_keys(int(random.randint(34, 40)))
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_66']//input").send_keys(int(random.randint(-10, 0)))
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_62']//input").send_keys(int(random.randint(-10, 0)))
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_58']//input").send_keys(int(161))
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_54']//input").send_keys(int(170))
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_50']//input").send_keys(int(340))
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_46']//input").send_keys(int(340))
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_42']//input").send_keys(int(340))
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_38']//input").send_keys(int(340))
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_34']//input").send_keys(int(340))
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_258']//input").send_keys(int(340))
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_157']//input").send_keys(int(165))
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_161']//input").send_keys(int(165))
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_165']//input").send_keys(int(random.randint(160, 170)))
        time.sleep(1)
        # driver.find_element(By.XPATH, "//li[@id='field_215']//textarea").send_keys("Abubakr")
        driver.find_element(By.XPATH, "//li[@id='field_169']//input").send_keys(int(random.randint(160, 170)))
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_173']//input").send_keys(int(random.randint(34, 38)))
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_179']//input").send_keys(int(random.randint(34, 40)))
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_183']//input").send_keys(int(random.randint(34, 40)))
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_221']//input").send_keys(int(random.randint(34, 38)))
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_224']//input").send_keys(int(random.randint(34, 40)))
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_227']//input").send_keys(int(random.randint(34, 40)))
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_199']//div//a//div[1]").click()  # button
        time.sleep(5)
        # div.signature_field
        canvas = driver.find_element(By.XPATH, "//div[@id='signature_base']//div[1]//div[@class = 'signature_field']")
        drawing = ActionChains(driver) \
            .click_and_hold(canvas) \
            .move_by_offset(-10, -15) \
            .move_by_offset(20, 32) \
            .move_by_offset(10, 25) \
            .release()
        drawing.perform()
        time.sleep(1)
        driver.find_element(By.XPATH, "//div[@id='signature_base']//a[2]").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//div[@id='submit_form']").click()  # button
        time.sleep(20)
        driver.close()
        logging.debug("form_377423_LOGC submitted")
        print("#-------------Successfully filled HACCP LOG C form-------------#")
    # form id: 377423 and name: HACCP log C end
# /-----------------------------------------------------HACCP log C----------------------------------------------------/

# /-----------------------------------------------------HACCP log D----------------------------------------------------/
    # form id: 377616 and name: HACCP log D start
    def form_377616_LOGD():  # HACCP Log D (Opening)
        # /----------------------------------------------Restaurant login----------------------------------------------/
        userName, Password, login_hint, restaurant_name, temp1, temp2, temp3, temp4, temp5, temp6, ManagerName = credentials()
        logging.debug("form_377616_LOGD opened")
        print("#-------------Filling HACCP LOG D form-------------#")
        print(f"Restaurant number: {restaurant_name}")
        response = requests.post("https://www.zenput.com/get_sso_company_info/", json={"email": f"{login_hint}"})
        login_hint = login_hint.replace("@", "%40")
        inter_var = response.text
        x = inter_var.split(":")[7].split('"')[1]
        URL = f"https://zenput.auth0.com/authorize?client_id=vmFR5ePxkzh5UAJkijHZiKcZixJcERX6&connection=rbi-plk-prod&login_hint={login_hint}&sp_type=auth0&state={x}&scope=offline_access%20openid%20profile%20email&redirect_uri=https%3A%2F%2Fwww.zenput.com%2Fauth0_callback%2F&response_type=code&auth0Client=eyJuYW1lIjoiYXV0aDAuanMiLCJ2ZXJzaW9uIjoiOS4xMy4yIn0%3D"
        # print(f"URL: {URL}")
        driver = webdriver.Chrome()
        driver.get(URL)
        driver.find_element(By.ID, "okta-signin-username").send_keys(userName)
        driver.find_element(By.ID, "okta-signin-password").send_keys(Password)
        driver.find_element(By.ID, "okta-signin-submit").click()
        time.sleep(50)
        driver.find_element(By.XPATH, "//a[@id='oiw_btn']").click()
        time.sleep(20)
        # /----------------------------------------------Restaurant login----------------------------------------------/

        # form opening
        driver.find_element(By.XPATH, "//li//a[@class='navlink taskitem_container']//div[normalize-space()='HACCP Log D (Closing)']").click()
        time.sleep(20)
        driver.find_element(By.XPATH, "//div[@id='submit_form']").click()
        time.sleep(20)

        driver.find_element(By.XPATH, "//li[@id='field_213']//textarea").send_keys(ManagerName)
        time.sleep(1)
        # //li[@id='field_0']//div[2]//span
        driver.find_element(By.XPATH, "//li[@id='field_30']//input").send_keys(int(random.randint(34, 38)))
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_82']//input").send_keys(int(random.randint(34, 38)))
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_142']//input").send_keys(int(random.randint(34, 38)))
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_146']//input").send_keys(int(random.randint(34, 38)))
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_78']//input").send_keys(int(random.randint(34, 40)))
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_74']//input").send_keys(int(random.randint(34, 40)))
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_70']//input").send_keys(int(random.randint(34, 40)))
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_66']//input").send_keys(int(random.randint(-10, 0)))
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_62']//input").send_keys(int(random.randint(-10, 0)))
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_199']//div//a//div[1]").click()  # button
        time.sleep(5)
        # div.signature_field
        canvas = driver.find_element(By.XPATH, "//div[@id='signature_base']//div[1]//div[@class = 'signature_field']")
        drawing = ActionChains(driver) \
            .click_and_hold(canvas) \
            .move_by_offset(-10, -15) \
            .move_by_offset(20, 32) \
            .move_by_offset(10, 25) \
            .release()
        drawing.perform()
        time.sleep(1)
        driver.find_element(By.XPATH, "//div[@id='signature_base']//a[2]").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//div[@id='submit_form']").click()  # button
        time.sleep(20)
        driver.close()
        logging.debug("form_377616_LOGD submitted")
        print("#-------------Successfully filled HACCP LOG D form-------------#")
    # form id: 377616 and name: HACCP log D end
# /-----------------------------------------------------HACCP log D----------------------------------------------------/

# /-----------------------------------------------Daily Travel Path (AM)-----------------------------------------------/
    # form id: 377997 and name: Daily Travel Path - Brand Standard (AM pre-rush) start
    def form_377997_AM():  # Daily Travel Path - Brand Standard (AM pre-rush)
        # /----------------------------------------------Restaurant login----------------------------------------------/
        userName, Password, login_hint, restaurant_name, temp1, temp2, temp3, temp4, temp5, temp6, ManagerName = credentials()
        logging.debug("form_377997_AM opened")
        print("#-------------Filling Daily Travel Path (AM pre-rush) form-------------#")
        print(f"Restaurant number: {restaurant_name}")
        response = requests.post("https://www.zenput.com/get_sso_company_info/", json={"email": f"{login_hint}"})
        login_hint = login_hint.replace("@", "%40")
        inter_var = response.text
        x = inter_var.split(":")[7].split('"')[1]
        URL = f"https://zenput.auth0.com/authorize?client_id=vmFR5ePxkzh5UAJkijHZiKcZixJcERX6&connection=rbi-plk-prod&login_hint={login_hint}&sp_type=auth0&state={x}&scope=offline_access%20openid%20profile%20email&redirect_uri=https%3A%2F%2Fwww.zenput.com%2Fauth0_callback%2F&response_type=code&auth0Client=eyJuYW1lIjoiYXV0aDAuanMiLCJ2ZXJzaW9uIjoiOS4xMy4yIn0%3D"
        # print(f"URL: {URL}")
        driver = webdriver.Chrome()
        driver.get(URL)
        driver.find_element(By.ID, "okta-signin-username").send_keys(userName)
        driver.find_element(By.ID, "okta-signin-password").send_keys(Password)
        driver.find_element(By.ID, "okta-signin-submit").click()
        time.sleep(50)
        driver.find_element(By.XPATH, "//a[@id='oiw_btn']").click()
        time.sleep(20)
        # /----------------------------------------------Restaurant login----------------------------------------------/

        # form opening
        driver.find_element(By.XPATH, "//li//a[@class='navlink taskitem_container']//div[normalize-space()='Daily Travel Path - Brand Standard (AM pre-rush)']").click()
        time.sleep(20)
        driver.find_element(By.XPATH, "//div[@id='submit_form']").click()
        time.sleep(20)
        driver.find_element(By.XPATH, "//li[@id='field_2']//textarea").send_keys(ManagerName)
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_3']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_30']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_29']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_28']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_27']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_26']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_25']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_24']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_23']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_22']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_21']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_20']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_19']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_18']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_119']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_120']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_16']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_15']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_14']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_13']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_12']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_11']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_10']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_9']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_8']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_7']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_6']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_5']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_121']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_122']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_123']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_4']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_37']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_36']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_35']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_39']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_38']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_42']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_40']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_44']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_43']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_46']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_45']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_48']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_47']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_50']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_125']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_52']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_51']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_54']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_53']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_126']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_56']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_55']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_58']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_57']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_60']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_59']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_65']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_127']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//div[@id='submit_form']").click()  # button
        time.sleep(20)
        driver.close()
        logging.debug("form_377997_AM submitted")
        print("#-------------Successfully filled Daily Travel Path (AM pre-rush) form-------------#")
    # form id: 377997 and name: Daily Travel Path - Brand Standard (AM pre-rush) end
# /-----------------------------------------------Daily Travel Path (AM)-----------------------------------------------/

# /-----------------------------------------------Daily Travel Path (PM)-----------------------------------------------/
    # form id: 377997 and name: Daily Travel Path - Brand Standard (PM pre-rush) start
    def form_377997_PM():  # Daily Travel Path - Brand Standard (PM pre-rush)
        # /----------------------------------------------Restaurant login----------------------------------------------/
        userName, Password, login_hint, restaurant_name, temp1, temp2, temp3, temp4, temp5, temp6, ManagerName = credentials()
        logging.debug("form_377997_PM opened")
        print("#-------------Filling Daily Travel Path (PM pre-rush) form-------------#")
        print(f"Restaurant number: {restaurant_name}")
        response = requests.post("https://www.zenput.com/get_sso_company_info/", json={"email": f"{login_hint}"})
        login_hint = login_hint.replace("@", "%40")
        inter_var = response.text
        x = inter_var.split(":")[7].split('"')[1]
        URL = f"https://zenput.auth0.com/authorize?client_id=vmFR5ePxkzh5UAJkijHZiKcZixJcERX6&connection=rbi-plk-prod&login_hint={login_hint}&sp_type=auth0&state={x}&scope=offline_access%20openid%20profile%20email&redirect_uri=https%3A%2F%2Fwww.zenput.com%2Fauth0_callback%2F&response_type=code&auth0Client=eyJuYW1lIjoiYXV0aDAuanMiLCJ2ZXJzaW9uIjoiOS4xMy4yIn0%3D"
        # print(f"URL: {URL}")
        driver = webdriver.Chrome()
        driver.get(URL)
        driver.find_element(By.ID, "okta-signin-username").send_keys(userName)
        driver.find_element(By.ID, "okta-signin-password").send_keys(Password)
        driver.find_element(By.ID, "okta-signin-submit").click()
        time.sleep(50)
        driver.find_element(By.XPATH, "//a[@id='oiw_btn']").click()
        time.sleep(20)
        # /----------------------------------------------Restaurant login----------------------------------------------/

        # form opening
        driver.find_element(By.XPATH, "//li//a[@class='navlink taskitem_container']//div[normalize-space()='Daily Travel Path - Brand Standard (PM pre-rush)']").click()
        time.sleep(20)
        driver.find_element(By.XPATH, "//div[@id='submit_form']").click()
        time.sleep(20)
        #
        driver.find_element(By.XPATH, "//li[@id='field_2']//textarea").send_keys(ManagerName)
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_3']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_30']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_29']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_28']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_27']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_26']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_25']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_24']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_23']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_22']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_21']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_20']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_19']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_18']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_119']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_120']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_16']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_15']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_14']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_13']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_12']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_11']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_10']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_9']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_8']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_7']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_6']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_5']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_121']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_122']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_123']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_4']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_37']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_36']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_35']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_39']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_38']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_42']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_40']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_44']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_43']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_46']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_45']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_48']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_47']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_50']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_125']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_52']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_51']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_54']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_53']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_126']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_56']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_55']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_58']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_57']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_60']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_59']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_65']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//li[@id='field_127']//button[@value='true']").click()  # button
        time.sleep(1)
        driver.find_element(By.XPATH, "//div[@id='submit_form']").click()  # button
        time.sleep(20)
        driver.close()
        logging.debug("form_377997_PM submitted")
        print("#-------------Successfully filled Daily Travel Path (PM pre-rush) form-------------#")
    # form id: 377997 and name: Daily Travel Path - Brand Standard (PM pre-rush) end
# /-----------------------------------------------Daily Travel Path (PM)-----------------------------------------------/


    schedule.every().day.at(HACCPA_TIME).do(form_377033_LOGA)  # 9:15
    schedule.every().day.at(Daily_Travel_Path_AM_TIME).do(form_377997_AM)  # 11:15
    schedule.every().day.at(HACCPB_TIME).do(form_377038_LOGB)  # 13:15
    schedule.every().day.at(Daily_Travel_Path_PM_TIME).do(form_377997_PM)  # 16:15
    schedule.every().day.at(HACCPC_TIME).do(form_377423_LOGC)  # 17:15
    schedule.every().day.at(HACCPD_TIME).do(form_377616_LOGD)  # 20:15



    while True:
        schedule.run_pending()


def main():
    task()


if __name__ == "__main__":
    main()
