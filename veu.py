#Importing libraries
from selenium import webdriver
from random import randint
import pandas as pd
from bs4 import BeautifulSoup as bs
from time import sleep
import time
#Getting webdriver from its directory
web = webdriver.Chrome(executable_path="C:/Users/0k/chromedriver.exe")
web.set_window_size(800,900)

#Opening the webpage using chromedriver
web.get('https://www.zacks.com/funds/etf/veu/holding')

web.execute_script('window.scrollTo(0, (document.body.scrollHeight/2)-500)')
pg=web.find_element_by_xpath('//*[@id="etf_holding_table_length"]/label/select')
pg.click()
no=web.find_element_by_xpath('//*[text()="100"]')
no.click()

#using while loop to access table data from every page 
#pages 1-37
k=0
tables=[]
tables.append(["Security Name","Symbol","Shares","Weight(%)","52 Wk Change(%)","Report"])
while k <= 37:
    k=k+1
    html=web.page_source
    soup =  bs(html, "html.parser")

    table=soup.find("table",{'id':'etf_holding_table'}) #finding table with the help of id

    rows=soup.find_all("tr",{'role':'row'}) 

    for i in range(103):
        i=rows[i]
        col=i.find_all("td")
        val=[]
        for j in col:
            val.append(j.text)
        if len(val)>1:
            tables.append(val)
    login=web.find_element_by_xpath('//*[text()="Next"]')
    login.click()
    sleep(2)
len(tables)
df=pd.DataFrame(tables[1:],columns=tables[0]) # storing extracted data into dataframe
df.to_excel(r"C:\Users\Admin\Desktop\VEU.xlsx")#converting dataframe to excel file