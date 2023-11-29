from selenium import webdriver
import os
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
script_directory = os.path.dirname(os.path.abspath(__file__))
Driver_path =  os.path.join(script_directory, 'assets', 'chromedriver.exe')
opt = Options()
opt.add_experimental_option("debuggerAddress", "localhost:8989")
driver = webdriver.Chrome(
    executable_path=Driver_path, chrome_options=opt)
driver.get("https://gurushots.com/challenges/my-challenges/current")
def wait(func):
    driver.implicitly_wait(10)
    def wrapper():
        return func
    return wrapper
def wait_for_elements():
    return driver.find_elements(By.CLASS_NAME, 'c-challenges-item__exposure__meter__arrow')
@wait
def run():
    try:
        elements = driver.find_elements(By.CLASS_NAME, 'c-challenges-item__exposure__meter__arrow')
        if elements:
            for div_element in elements:
                if div_element.is_displayed():
                    print(div_element.get_attribute("style"))
                    print("The div element is visible on the page.")
                else:
                    print("The div element is not visible on the page.")
        else:
            print("No elements found with the specified class.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
run()
driver.quit()
