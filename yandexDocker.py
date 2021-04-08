from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

class H_W():

    def test(self):
        baseUrl = "https://yandex.ru/"
        driver = webdriver.Remote(command_executor="http://localhost:4444/wd/hub",desired_capabilities={ "browserName": "firefox"})
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        parenthandle = driver.current_window_handle
        print(parenthandle) #15

        mail = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                           "//div[text() = 'Почта']"))).click()
        time.sleep(2)

        handles = driver.window_handles

        for handle in handles:
            print(handle)
            if handle not in parenthandle:
                driver.switch_to_window(handle)
                print(handle)
                time.sleep(2)
                login = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID,
                                                                                    "passp-field-login"))).send_keys(
                    "userqatest@yandex.ru")
                enter1 = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                     "//button[@type='submit']"))).click()
                passwd = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                     "//input[ @ id = 'passp-field-passwd']"))).send_keys(
                    "qwer12345")
                enter2 = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,
                                                                                     "//button[@type='submit']"))).click()

                # not_now_btn = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-t='button:pseudo']"))).click()
                driver.quit()


ff = H_W()
ff.test()