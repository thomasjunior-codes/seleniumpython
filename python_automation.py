from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

fromInputbutton = "//input[@data-cy='fromCity']"
toInputbutton = "//input[@data-cy='toCity']"
fromText = "//input[@placeholder='From']"
toText = "//input[@placeholder='To']"
close_popup = "//a[contains(@id,'notification-close-div')]"

def waitforelement(xpath):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.XPATH, xpath))
    )

def click(xpath):
    waitforelement(xpath)
    driver.find_element(By.XPATH, xpath).click()

def sendText(xpath, text):
    waitforelement(xpath)
    driver.find_element(By.XPATH, xpath).send_keys(text)

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.makemytrip.com/")
driver.maximize_window()
time.sleep(5)
# click(close_popup)
# click(fromInputbutton)
# sendText(fromText,"Tirupati")
# click("//p[.='Tirupati, India']")
# sendText(toText,"Mumbai")
# click("//p[.='Mumbai, India']")
# click("//div[@aria-label='Tue Oct 11 2022']")
# click("//span[@class='langCardClose']")
# click("//p[@data-cy='submit']")
#
# waitforelement("//div[@class='listingRhs']/p")
# print(driver.find_element(By.XPATH, "//div[@class='listingRhs']/p").get_attribute("text"))
print("done")