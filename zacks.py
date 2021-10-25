#importing Libraries
from selenium import webdriver
from random import randint
import pandas as pd
from bs4 import BeautifulSoup as bs
from time import sleep
import time

#Opening the web page with the help of webdriver
web = webdriver.Chrome(executable_path="/Users/0k/chromedriver")
web.maximize_window()
web.get('https://www.zacks.com/screening/stock-screener?icid=screening-screening-nav_tracking-zcom-main_menu_wrapper-stock_screener')
try:
    no=web.find_element_by_xpath('//p[text()="Consent"]')
    no.click()
except:
    pass
web.execute_script('window.scrollTo(0, (document.body.scrollHeight/2)-1000)')

#clicking on MyScreen button
frame = web.find_element_by_id("screenerContent")
web.switch_to.frame(frame)
my=web.find_element_by_xpath('//*[@id="my-screen-tab"]')
my.click()
sleep(1)
web.execute_script('window.scrollTo(0, (document.body.scrollHeight/2))')
try:
    username=web.find_element_by_xpath('//*[@id="username"]') #username textbox
    username.clear()
    username.send_keys("laboc57506@ampswipe.com") #typing the username given
    sleep(1)
    password=web.find_element_by_xpath('//*[@id="password"]') #password textbox
    password.clear()
    password.send_keys("msJ$eb8EJu72@Bj") #typing the password given
    sleep(1)
    #clicking on sign-in button
    signin=web.find_element_by_xpath('//*[text()="Sign In"]') 
    signin.click()
except:
    print("WAS ALREADY LOGINED/TRY AFTER LOGOUT IF NOT WORKING")
    pass
web.execute_script('window.scrollTo(0, (document.body.scrollHeight))')
singin=web.find_element_by_xpath('//button[@class="button"]')
singin.click()
sleep(3)
#Clicking on Run button
run=web.find_element_by_xpath('//*[text()="Run"]')
run.click()
sleep(3)
selectall=web.find_element_by_xpath('//input[@id="select_all_tickers"]')
selectall.click()
sleep(3)
#Finding the download button and then clicking on it
download=web.find_element_by_xpath('//*[@id="screener_table_wrapper"]/div[1]/a[1]')
download.click()