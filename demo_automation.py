import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


def configurate_driver():
    global driver
    options = Options()
    options.add_argument("start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    # browser = webdriver.Chrome(executable_path=r"/home/mmarrari/demo_browser_automation/chromedriver")
    # browser.maximize_window()
    driver.get('http://localhost:8080/pagina1.html')
    time.sleep(3)


def navigate_to_page2():
    global wait, link_to_press
    wait = WebDriverWait(driver, 20)
    wait.until(EC.element_to_be_clickable((By.ID, 'link1')))
    link_to_press = driver.find_element(By.ID, 'link1')
    link_to_press.click()
    time.sleep(3)


def navigate_to_page3():
    global link_to_press
    wait.until(EC.element_to_be_clickable((By.XPATH, '//a[1]')))
    link_to_press = driver.find_element(By.XPATH, '//a[1]')
    link_to_press.click()
    time.sleep(3)


def close_and_quit_browser():
    driver.close()
    driver.quit()


configurate_driver()

navigate_to_page2()

navigate_to_page3()

close_and_quit_browser()
