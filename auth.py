from selenium import webdriver
from selenium.webdriver.common.by import By


import os
from dotenv import load_dotenv

import logging

load_dotenv()
URL = os.getenv('SITE_URL')
def authorize(LOGIN, PASSWORD):
    success = False
    login_key = False
    password_key = False
    driver = webdriver.Firefox()
    try:
        driver.get(URL)
    except Exception as e:
        logging.info(f'Error opening site {URL}')
    try:
        entry_button = driver.find_element(By.CSS_SELECTOR, '.profile__bar-login')
        entry_button.click()
        logging.info(f'Click on entry button success')
    except Exception as e:
        logging.info(f'Error find entry_button')
    try:
        login_item = driver.find_element(By.CSS_SELECTOR, '#id_login')
        login_item.clear()
        login_item.send_keys(LOGIN)
        login_key = True
        logging.info(f'Successfuly found login_item')
    except Exception as e:
        logging.info(f'Error find login_item')

    try:
        password_item = driver.find_element(By.CSS_SELECTOR, '#id_password')
        password_item.clear()
        password_item.send_keys(PASSWORD)
        password_key = True
        logging.info(f'Successfuly found password_item')
    except Exception as e:
        logging.info('Error find password_item')

    if password_key and login_key:
        try:
            auth_button = driver.find_element(By.CSS_SELECTOR, '.btn')
            auth_button.click()
            flag = driver.find_element(By.CSS_SELECTOR, '.profile__bar-username')
            if flag:
                logging.info('Authorization success')
                success = True
            else:
                logging.info('Incorrect login or password')
        except Exception as e:
            logging.error('Error authorization')

    driver.close()
    return success

