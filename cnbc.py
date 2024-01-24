from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import pandas as pd
import pickle
import pyautogui
import keyboard as kbd # importing keyboard module
import time
import pyautogui
from pathvalidate import is_valid_filename
from collections import OrderedDict

chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory" : 'C:\\Users\\sudha\\Downloads\\Predictive Analysis'}
chromeOptions.add_experimental_option("prefs",prefs)
chromeOptions.add_argument("window-size=1200x600")
driver = webdriver.Chrome(options=chromeOptions)
url=f'https://www.cnbc.com/search/?query=google%20financial%20news&qsearchterm=google%20financial%20news'
data={}
# df=pd.read_csv("News_Data.csv")
df_list=[]
driver.get(url)

time.sleep(3)
last_height = driver.execute_script("return document.body.scrollHeight")
# print(driver.find_elements("xpath","/div[@class='SearchResult-searchResultContent']/div/a"))
for i in range(1,1000):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    headlines=driver.find_element("xpath",f'/html/body/div[4]/div/div[1]/div[3]/div/div/div/div/div/div[2]/div/section/div/div[2]/div/div[2]/div/div/div[2]/div/div/div[2]/div[{i}]/div/div[2]/div[2]/a')
    driver.get_screenshot_as_file("screenshot.png")
    try:
        date=driver.find_element("xpath",f'/html/body/div[4]/div/div[1]/div[3]/div/div/div/div/div/div[2]/div/section/div/div[2]/div/div[2]/div/div/div[2]/div/div/div[2]/div[{i}]/div/div[2]/span/span[2]')
    except:
        date=driver.find_element("xpath",f'/html/body/div[4]/div/div[1]/div[3]/div/div/div/div/div/div[2]/div/section/div/div[2]/div/div[2]/div/div/div[2]/div/div/div[2]/div[{i}]/div/div[2]/span/span')

    data={"headlines":[headlines.text],"date":[date.text]}

    driver.get(headlines.get_attribute("href"))
    time.sleep(3)
    l=[]
    # try:
        
    content=driver.find_elements("xpath",'//p')
    for j in content:
        l.append(j.text)
    data.update({"content":[' '.join(l)]})   
    # except:
    #     data.update({"content":[' '.join(l)]})
    #     df_list.append(pd.DataFrame(data=data))
    #     pd.concat(df_list).to_csv("News_Data.csv")
    #     driver.get(url)
    #     time.sleep(3)
    #     print("in")
    #     continue
    df_list.append(pd.DataFrame(data=data))
    pd.concat(df_list).to_csv("News_Data.csv")
    driver.get(url)
    
    time.sleep(3)
    

