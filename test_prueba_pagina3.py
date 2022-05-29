import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import requests
from urllib.parse import urljoin
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter

pytest_plugins = ["docker_compose"]

# Invoking this fixture: 'function_scoped_container_getter' starts all services
@pytest.fixture(scope="function")
def wait_for_api(function_scoped_container_getter):
    """Wait for the api from my_api_service to become responsive"""
    request_session = requests.Session()
    retries = Retry(total=5,
                    backoff_factor=0.1,
                    status_forcelist=[500, 502, 503, 504])
    request_session.mount('http://', HTTPAdapter(max_retries=retries))

    service = function_scoped_container_getter.get("web").network_info[0]
    api_url = "http://%s:%s/" % (service.hostname, service.host_port)
    assert request_session.get(api_url)
    return request_session, api_url

def test_prueba_pagina3(wait_for_api):
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


