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
driver.get(url)
time.sleep(3)
data={}
df_list=[]
merged=[]
for i in range(1,1000):
    headlines=driver.find_element("xpath",f'/html/body/div[4]/div/div[1]/div[3]/div/div/div/div/div/div[2]/div/section/div/div[2]/div/div[2]/div/div/div[2]/div/div/div[2]/div[{i}]/div/div[2]/div[2]/a')
    data={"headlines":[headlines.text]}
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
    time.sleep(2)


