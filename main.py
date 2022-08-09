import time
import selenium.webdriver
import selenium
from selenium.webdriver.common.by import By

driver = selenium.webdriver.Firefox()
driver.get("https://sugang.knu.ac.kr")
driver.implicitly_wait(5000)

login_info = {
    "studentNo": "",
    "id": "",
    "passwd": ""
}

lectures = []

while True:
    if driver.current_url == "https://sugang.knu.ac.kr/login.knu":
        login_form_studnetNo = driver.find_element(by=By.XPATH, value="//*[@id=\"stdno\"]")
        login_form_id = driver.find_element(by=By.XPATH, value="//*[@id=\"userId\"]")
        login_form_passwd = driver.find_element(by=By.XPATH, value="//*[@id=\"pssrd\"]")
        login_button = driver.find_element(by=By.XPATH, value="//*[@id=\"btn_login\"]")

        login_form_studnetNo.send_keys(login_info["studentNo"])
        login_form_id.send_keys(login_info["id"])
        login_form_passwd.send_keys(login_info["passwd"])
        time.sleep(3)
        login_button.click()
        driver.implicitly_wait(5000)
        time.sleep(5)

    else:
        sugangpack_button = driver.find_element(by=By.XPATH, value="//*[@id=\"tabs2\"]")
        sugangpack_button.click()

        time.sleep(1)
        sugangpack_lectures = driver.find_element(by=By.XPATH, value="//*[@id=\"grid01\"]").find_elements(by=By.TAG_NAME, value="tr")
        count = 0
        for sugangpack_lecture in sugangpack_lectures:
            count = count + 1

        if count < 1:
            break
        else:
            for sugangpack_lecture in sugangpack_lectures:
                name = sugangpack_lecture.find_elements(by=By.TAG_NAME, value="td")[3].text
                max = int(sugangpack_lecture.find_elements(by=By.TAG_NAME, value="td")[10].text)
                current = int(sugangpack_lecture.find_elements(by=By.TAG_NAME, value="td")[11].text)
                print(name + " " + str(max) + " " + str(current))

                if max < current:
                    sugangpack_apple_button = sugangpack_lecture.find_element(by=By.TAG_NAME, value="a")
                    sugangpack_apple_button.click()
                    alert = driver.switch_to.alert
                    alert.accept()
                    driver.implicitly_wait(5000)
                    time.sleep(5)
                    alert = driver.switch_to.alert
                    alert.accept()
                    time.sleep(1)

        driver.refresh()

driver.close()
