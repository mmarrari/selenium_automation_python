import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

pytest_plugins = ['docker_compose']

def test_prueba_pagina3():
    options = Options()
    options.add_argument("start-maximized")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get('http://localhost:8080/pagina1.html')
    time.sleep(3)
    wait = WebDriverWait(driver, 20)
    wait.until(EC.element_to_be_clickable((By.ID, 'link1')))
    link_to_press = driver.find_element(By.ID, 'link1')
    link_to_press.click()
    time.sleep(3)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//a[1]')))
    link_to_press = driver.find_element(By.XPATH, '//a[1]')
    link_to_press.click()
    time.sleep(3)
    value_to_test = driver.find_element(By.ID, 'test_value')
    assert value_to_test.text == "Todo bien"


