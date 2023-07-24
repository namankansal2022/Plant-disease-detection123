from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from random import randint


chromedriver_path = 'C:/Users/JACOB/Downloads/chromedriver_win32 (1)/chromedriver.exe' 
webdriver = webdriver.Chrome(executable_path=chromedriver_path)
sleep(2)
webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(3)

username = webdriver.find_element_by_name('username')
username.send_keys('MYUSERNAME')
password = webdriver.find_element_by_name('password')
password.send_keys('MYPASSWORD')

button_login = webdriver.find_element_by_css_selector('#react-root > section > main > div > article > div > div > div > form > div > button.sqdOP.L3NKy.y3zKF')
button_login.click()

sleep(4)

notnow = webdriver.find_element_by_css_selector('#react-root > section > main > div > div > div > div > button.sqdOP.yWX7d.y3zKF')
notnow.click()

sleep (4)

postnotifications = webdriver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
postnotifications.click()

sleep(3)

mydms = webdriver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[2]/a/svg')
mydms.click()

search = webdriver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
search.send_keys('INSTAGRAM_USERNAME')

sleep(2)

foundit = webdriver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a/div/div[2]/div/span')
foundit.click()

sleep(3)