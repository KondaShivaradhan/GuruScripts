from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import os
import chromedriver_autoinstaller
from assets.Operations import *
classNames = {
    "Angle_className": "c-challenges-item__exposure__meter__arrow",
    "VoteBtn_ClassName": "action-button-gen",
    "VoteParents_ClassName": "c-challenges-item__exposure__footer",
    "CloseAdClassName": "fs-close-button fs-close-button-sticky",
    "AdElementClassName": "fs-sticky-slot-element",
    "cardsClosebtnsClassName": "c-cards__close"
}
chromeVersion = get_chrome_browser_version()
versionNums = chromeVersion.split(".")
script_directory = os.path.dirname(os.path.abspath(__file__))
Driver_path = os.path.join(
    script_directory, "assets", versionNums[0], 'chromedriver.exe')
opt = Options()
opt.add_experimental_option("debuggerAddress", "localhost:8989")

if os.path.exists(Driver_path):
    driver = webdriver.Chrome(
        executable_path=Driver_path, chrome_options=opt)
    driver.get("https://gurushots.com/challenges/my-challenges/current")
    driver.implicitly_wait(10)

    cardsClosebtns = driver.find_elements(
        By.CLASS_NAME, classNames["cardsClosebtnsClassName"])
    closeCards(cardsClosebtns=cardsClosebtns)
    AngleElements = driver.find_elements(
        By.CLASS_NAME, classNames["Angle_className"])
    VoteParents = driver.find_elements(
        By.CLASS_NAME, classNames["VoteParents_ClassName"])
    voteModalXpath = "//body[1]/app-root[1]/div[1]/div[1]/gs-modals[1]/div[1]"
    LetsGoBtnXpath = "//body[1]/app-root[1]/div[1]/div[1]/gs-modals[1]/div[1]/modal-vote[1]/div[4]/div[1]/div[1]/div[1]"
    # get All available voting btns
    VoteBtns = getvoteBtns(VoteParents=VoteParents)
    anglesNow = []
    for element in AngleElements:
        style_attribute = element.get_attribute("style")
        anglesNow.append(style_attribute[18:style_attribute.index('d')])
    print(anglesNow)
    for index, deg in enumerate(anglesNow):
        print((deg))
        if float(deg) < 90.0:
            print("Clicking on "+str(index+1)+" vote btn")
            VoteBtns[index].click()
            driver.implicitly_wait(10)
            print("waiting for something")
            wait = WebDriverWait(driver, 100)
            modal_element = wait.until(EC.presence_of_element_located(
                (By.XPATH, voteModalXpath)))
            print("modal might be up")

            driver.implicitly_wait(10)
            print("Trying to find Lets go btn inside model")

            button_inside_modal = modal_element.find_element(
                By.XPATH, LetsGoBtnXpath)

            button_inside_modal.click()
            print("Cicked on the Lets go btn")

            driver.implicitly_wait(10)

            # removing the title
            titleClass = "modal-vote__challenge-title"
            driver.execute_script("arguments[0].style.display = 'none';",   driver.find_element(
                By.CLASS_NAME, titleClass))
            # Clking the photos
            MeterArrClass = "modal-vote__exposure-meter__arrow"
            AllPhotosClassName = "modal-vote__photo"
            driver.implicitly_wait(10)

            ArrayofPhotos = driver.find_elements(
                By.CLASS_NAME, AllPhotosClassName)
            print(len(ArrayofPhotos))
            rans = []
            x = 0
            for i in range(1, len(ArrayofPhotos)):
                driver.implicitly_wait(1)
                arrow = driver.find_element(By.CLASS_NAME, MeterArrClass)
                style_attribute = arrow.get_attribute("style")
                if style_attribute[18:style_attribute.index('d')] == "90":
                    break
                if i % 2 == 0 and i not in rans:
                    rans.append(i)
                    try:
                        ArrayofPhotos[i].click()
                        time.sleep(0.3)
                        driver.implicitly_wait(10)

                    except:
                        print("Something came infront")
            # here we click submit
            driver.implicitly_wait(20)
            # SubmitClass = "/html[1]/body[1]/app-root[1]/div[1]/div[1]/gs-modals[1]/div[1]/modal-vote[1]/div[3]/div[2]/span[1]"
            SubmitClass = wait.until(EC.presence_of_element_located(
                (By.XPATH, "/html[1]/body[1]/app-root[1]/div[1]/div[1]/gs-modals[1]/div[1]/modal-vote[1]/div[3]/div[2]/span[1]")))
            # modal_element.find_element(By.XPATH, SubmitClass).click()
            SubmitClass.click()
            print("submited")
            # clicking Done after voding
            driver.implicitly_wait(22)
            ModelClassClass = "modal-vote__close"
            driver.implicitly_wait(22)
            driver.find_element(
                By.XPATH, "/html[1]/body[1]/app-root[1]/div[1]/div[1]/gs-modals[1]/div[1]/modal-vote[1]/div[4]/div[1]/div[2]/div[2]").click()
            print("Closed")

        else:
            print("this challenge is voted!")
    driver.quit()
else:
    print("Error with the driver path")
