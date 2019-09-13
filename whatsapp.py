from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time

driver = webdriver.Chrome('chromedriver.exe')
driver.get("https://web.whatsapp.com/") 
wait = WebDriverWait(driver, 600) 

target = '"[TARGET-NAME]"' #Target Name can be a phone number/friends name/group name
string = "Hello String sent using Python!!!"
x_arg = '//span[contains(@title,' + target + ')]'
group_title = wait.until(EC.presence_of_element_located(( 
    By.XPATH, x_arg))) 
print(group_title)
print ("Wait for few seconds")
group_title.click() 
inp_xpath = '//div[@class="input"][@dir="auto"][@data-tab="1"]'

message = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]
for i in range(10):
    message.send_keys(string)
    sendbutton = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')[0]
    sendbutton.click()
    time.sleep(1)

driver.close()
