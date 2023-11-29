import os
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import random
script_directory = os.path.dirname(os.path.abspath(__file__))
print(script_directory)
Driver_path =  os.path.join(script_directory, 'assets', 'chromedriver.exe')
opt = Options()
opt.add_experimental_option("debuggerAddress", "localhost:8989")

if(os.path.exists(Driver_path)):
    print("path is there")
    driver = webdriver.Chrome(
    executable_path=Driver_path, chrome_options=opt)
    actions = ActionChains(driver)
    driver.get("https://gurushots.com/challenges/my-challenges/current")
    driver.implicitly_wait(10)
    Angle_className = "c-challenges-item__exposure__meter__arrow"
    VoteBtn_ClassName = "c-challenges-item__btn--s--"
    CloseAdClassName = "fs-close-button fs-close-button-sticky"
    AdElementClassName="fs-sticky-slot-element"
    AngleElements = driver.find_elements(By.CLASS_NAME,Angle_className)
    VoteBtns = driver.find_elements(By.CLASS_NAME,VoteBtn_ClassName)
    # button_element = driver.find_element(By.XPATH,"//button[@aria-label='Close Ad']")
    # button_element.click() 
 
    anglesNow = []
    print(AngleElements)
    for element in AngleElements:
        style_attribute = element.get_attribute("style")
        #  '(' is at 17 
        anglesNow.append(style_attribute[18:style_attribute.index('d')])
    print(anglesNow)
    for index, deg in enumerate(anglesNow):
        print((deg))
        if float(deg)<90.0:
            driver.execute_script("arguments[0].click();", VoteBtns[index])
            driver.implicitly_wait(10)
            wait = WebDriverWait(driver, 10)
            modal_element = wait.until(EC.presence_of_element_located((By.XPATH, "//body[1]/app-root[1]/div[1]/div[1]/gs-modals[1]/div[1]")))
            driver.implicitly_wait(10)
            button_inside_modal = modal_element.find_element(By.XPATH,"//body[1]/app-root[1]/div[1]/div[1]/gs-modals[1]/div[1]/modal-vote[1]/div[4]/div[1]/div[1]/div[1]")
            button_inside_modal.click()
            driver.implicitly_wait(10)


            # removing the title 
            titleClass ="modal-vote__challenge-title"
            driver.execute_script("arguments[0].style.display = 'none';",   driver.find_element(By.CLASS_NAME,titleClass))
            # Clking the photos 
            MeterArrClass= "modal-vote__exposure-meter__arrow"
            AllPhotosClassName ="modal-vote__photo"
            driver.implicitly_wait(10)

            ArrayofPhotos = driver.find_elements(By.CLASS_NAME,AllPhotosClassName)
            print(len(ArrayofPhotos))
            rans = [] 
            x= 0
            for i in range(1,len(ArrayofPhotos)):
                driver.implicitly_wait(1)
                arrow = driver.find_element(By.CLASS_NAME,MeterArrClass)
                style_attribute = arrow.get_attribute("style")
                if style_attribute[18:style_attribute.index('d')]=="90":
                    break
                if i%2==0 and i not in rans:
                    rans.append(i)
                    try:
                        ArrayofPhotos[i].click()
                        driver.implicitly_wait(10)

                    except:
                        print("Something came infront")
            # here we click submit
            driver.implicitly_wait(2)
            SubmitClass = "/html[1]/body[1]/app-root[1]/div[1]/div[1]/gs-modals[1]/div[1]/modal-vote[1]/div[3]/div[2]/span[1]"
            modal_element.find_element(By.XPATH,SubmitClass).click()
            print("submited")
            # clicking Done after voding
            driver.implicitly_wait(2)
            ModelClassClass= "modal-vote__close"
            driver.implicitly_wait(2)
            driver.find_element(By.XPATH,"/html[1]/body[1]/app-root[1]/div[1]/div[1]/gs-modals[1]/div[1]/modal-vote[1]/div[4]/div[1]/div[2]/div[2]").click()
            print("Closed")

        else:
            print("this challenge is voted!")
    driver.quit()
else:
    print ("path not valid")
