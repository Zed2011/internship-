#!/usr/bin/env python
# coding: utf-8

# In[2]:


from bs4 import BeautifulSoup
import requests
import pandas as pd 
import selenium
from selenium.webdriver.common.by import By  
from selenium import webdriver
import warnings
warnings.filterwarnings('ignore')
import time
import re
from selenium.common.exceptions import NoSuchElementException


# In[4]:


driver=webdriver.Chrome()
driver.get("https://en.wikipedia.org/wiki/List_of_most-viewed_YouTube_videos")


# In[12]:


name=[]
rank=[]
artist=[]
upload_data=[]
views=[]
try:
    a = driver.find_elements(By.XPATH, '//table[@class="wikitable sortable jquery-tablesorter"]/tbody/tr/td[2]')
    for i in a[0:30]:
        name.append(i.text)
except NoSuchElementException:
    name.append("-")
try:
    a = driver.find_elements(By.XPATH, '//table[@class="wikitable sortable jquery-tablesorter"]/tbody/tr/td[3]')
    for i in a[0:30]:
        artist.append(i.text)
except NoSuchElementException:
    artist.append("-")
try:
    a = driver.find_elements(By.XPATH, '//table[@class="wikitable sortable jquery-tablesorter"]/tbody/tr/td[4]')
    for i in a[0:30]:
        views.append(i.text)
except NoSuchElementException:
    views.append("-")
try:
    a = driver.find_elements(By.XPATH, '//table[@class="wikitable sortable jquery-tablesorter"]/tbody/tr/td[5]')
    for i in a[0:30]:
        upload_data.append(i.text)
except NoSuchElementException:
    upload_data.append("-")    
    


# In[19]:


youtube=pd.DataFrame({"Name":name,"Artist":artist,"Views":views,"Upload_data":upload_data})


# In[14]:


youtube


# In[24]:


driver=webdriver.Chrome()
driver.get("https://www.bcci.tv/")
but=driver.find_element(By.XPATH,"/html/body/nav/div[1]/div[2]/ul[1]/li[2]/a")
but.click()
time.sleep(5) 


# In[35]:


Match=[] 
Series=[]
Place=[]
Date=[]
Time =[]
try:
    a = driver.find_elements(By.XPATH, '//h5[@class="match-tournament-name ng-binding"]')
    for i in a:
        Match.append(i.text)
except NoSuchElementException:
    Match.append("-")
try:
    a = driver.find_elements(By.XPATH, '//div[@class="match-card-middle d-flex"]')
    for i in a:
        Series.append(i.text)
except NoSuchElementException:
    Series.append("-")
try:
    a = driver.find_elements(By.XPATH, '//span[@class="ng-binding ng-scope"]')
    for i in a:
        Place.append(i.text)
except NoSuchElementException:
    Place.append("-")
try:
    a = driver.find_elements(By.XPATH, '//div[@class="match-dates ng-binding"]')
    for i in a:
        Date.append(i.text)
except NoSuchElementException:
    Date.append("-")
try:
    a = driver.find_elements(By.XPATH, '//div[@class="match-time no-margin ng-binding"]')
    for i in a:
        Time.append(i.text)
except NoSuchElementException:
    Time.append("-")


# In[39]:


se=[]
for i in Series:
    s=i.replace('\n','')
    se.append(s)
fix=pd.DataFrame({"MatchTitle":se,"Series":Match,"Place":Place,"Date":Date,"Time":Time})  
fix


# In[53]:


driver=webdriver.Chrome()
driver.get('https://statisticstimes.com/')
but=driver.find_element(By.XPATH,'/html/body/div[2]/div[1]/div[2]/div[2]/button')
but.click()
buti=driver.find_element(By.XPATH,'/html/body/div[2]/div[1]/div[2]/div[2]/div/a[3]')
buti.click()
time.sleep(5)
buta=driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[2]/ul/li[1]/a')
buta.click()


# In[54]:


Rank=[]
State=[]
GSDP=[]
GSDP1=[]
Share=[]
GDP =[]
try:
    a = driver.find_elements(By.XPATH, '//table[@class="display dataTable"]/tbody/tr/td[1]')
    for i in a:
        Rank.append(i.text)
except NoSuchElementException:
    Rank.append("-")
try:
    a = driver.find_elements(By.XPATH, '//table[@class="display dataTable"]/tbody/tr/td[2]')
    for i in a:
        State.append(i.text)
except NoSuchElementException:
    State.append("-")
try:
    a = driver.find_elements(By.XPATH, '//table[@class="display dataTable"]/tbody/tr/td[4]')
    for i in a:
        GSDP.append(i.text)
except NoSuchElementException:
    GSDP.append("-")
try:
    a = driver.find_elements(By.XPATH, '//table[@class="display dataTable"]/tbody/tr/td[3]')
    for i in a:
        GSDP1.append(i.text)
except NoSuchElementException:
    GSDP1.append("-")    
try:
    a = driver.find_elements(By.XPATH, '//table[@class="display dataTable"]/tbody/tr/td[5]')
    for i in a:
        Share.append(i.text)
except NoSuchElementException:
    Share.append("-")    
try:
    a = driver.find_elements(By.XPATH, '//table[@class="display dataTable"]/tbody/tr/td[6]')
    for i in a:
        GDP.append(i.text)
except NoSuchElementException:
    GDP.append("-")    


# In[61]:


gdp=pd.DataFrame({"Rank":Rank[0:34],"State":State[0:34],"GSDP(18-19)-at current prices":GSDP[0:34],"GSDP(19-20)- at current prices":GSDP1[0:34],
"Share(18-19)":Share[0:34],"GDP($ billion)":GDP[0:34]})
gdp


# In[17]:


driver=webdriver.Chrome()
driver.get('https://www.billboard.com/charts/hot-100/')


# In[50]:


Song=[] 
Artist=[]
Lastweek=[]  
Peak =[]
Weeks=[] 
try:
    a=driver.find_elements(By.XPATH,'//ul[@class="lrv-a-unstyle-list lrv-u-flex lrv-u-height-100p lrv-u-flex-direction-column@mobile-max"]/li/h3')
    for i in a[0:100]:
        Song.append(i.text)
except NoSuchElementException:
    Song.append("-")
try:
    a=driver.find_elements(By.XPATH,'//ul[@class="lrv-a-unstyle-list lrv-u-flex lrv-u-height-100p lrv-u-flex-direction-column@mobile-max"]/li[1]/span')
    for i in a[0:100]:
        Artist.append(i.text)
except NoSuchElementException:
    Artist.append("-")
    
try:
    a=driver.find_elements(By.XPATH,'//ul[@class="lrv-a-unstyle-list lrv-u-flex lrv-u-height-100p lrv-u-flex-direction-column@mobile-max"]/li[4]/span')
    for i in a[0:100]:
        Lastweek.append(i.text)
except NoSuchElementException:
    Lastweek.append("-")
try:
    a=driver.find_elements(By.XPATH,'//ul[@class="lrv-a-unstyle-list lrv-u-flex lrv-u-height-100p lrv-u-flex-direction-column@mobile-max"]/li[5]/span')
    for i in a[0:100]:
        Peak.append(i.text)
except NoSuchElementException:
    Artist.append("-")
try:
    a=driver.find_elements(By.XPATH,'//ul[@class="lrv-a-unstyle-list lrv-u-flex lrv-u-height-100p lrv-u-flex-direction-column@mobile-max"]/li[6]/span')
    for i in a[0:100]:
        Weeks.append(i.text)
except NoSuchElementException:
    Weeks.append("-")    


# In[55]:


songs=pd.DataFrame({"SongName":Song,"Artist":Artist,"Lastweekrank":Lastweek,"Peak rank":Peak,"Week on board":Weeks})


# In[56]:


songs


# In[62]:


driver=webdriver.Chrome()
driver.get('https://www.theguardian.com/news/datablog/2012/aug/09/best-selling-books-all-time-fifty-shades-grey-compare')


# In[63]:


Book=[] 
Author=[] 
Volumes=[]  
Publisher=[] 
Genre =[]
try:
    a=driver.find_elements(By.XPATH,'//table[@class="in-article sortable"]/tbody/tr/td[2]')
    for i in a:
        Book.append(i.text)
except NoSuchElementException:
    Book.append(i.text)
try:
    a=driver.find_elements(By.XPATH,'//table[@class="in-article sortable"]/tbody/tr/td[3]')
    for i in a:
        Author.append(i.text)
except NoSuchElementException:
    Author.append(i.text)
try:
    a=driver.find_elements(By.XPATH,'//table[@class="in-article sortable"]/tbody/tr/td[4]')
    for i in a:
        Volumes.append(i.text)
except NoSuchElementException:
    Volumes.append(i.text)
try:
    a=driver.find_elements(By.XPATH,'//table[@class="in-article sortable"]/tbody/tr/td[5]')
    for i in a:
        Publisher.append(i.text)
except NoSuchElementException:
    Publisher.append(i.text)
try:
    a=driver.find_elements(By.XPATH,'//table[@class="in-article sortable"]/tbody/tr/td[6]')
    for i in a:
        Genre.append(i.text)
except NoSuchElementException:
    Genre.append(i.text)    


# In[67]:


Booklist=pd.DataFrame({"Book Name":Book,"Author Name":Author,"Volumes Sold":Volumes,"Publisher":Publisher,"Genre":Genre})


# In[68]:


Booklist


# In[2]:


driver=webdriver.Chrome()
driver.get("https://www.imdb.com/list/ls095964455/")


# In[9]:


Name=[] 
Year=[]
Genre =[]
Run=[] 
Ratings =[]
Votes =[]

a=driver.find_elements(By.XPATH,'//h3[@class="lister-item-header"]/a')
for i in a:
    Name.append(i.text)
    
a=driver.find_elements(By.XPATH,'//span[@class="lister-item-year text-muted unbold"]')
for i in a:
    Year.append(i.text)

a=driver.find_elements(By.XPATH,'//p[@class="text-muted text-small"]/span[5]')
for i in a:
    Genre.append(i.text)

a=driver.find_elements(By.XPATH,'//p[@class="text-muted text-small"]/span[3]')
for i in a:
    Run.append(i.text)

a=driver.find_elements(By.XPATH,'//div[@class="ipl-rating-widget"]/div/span[2]')
for i in a:
    Ratings.append(i.text)

a=driver.find_elements(By.XPATH,'//span[@name="nv"]')
for i in a:
    Votes.append(i.text)
    


# In[10]:


list=pd.DataFrame({"Name": Name,"Year":Year,"Genre":Genre,"Rating":Ratings,"Votes":Votes})


# In[11]:


list


# In[41]:


driver=webdriver.Chrome()
driver.get("https://archive.ics.uci.edu/")
but=driver.find_element(By.XPATH,'/html/body/div/div[1]/div[1]/main/div/div[1]/div/div/div/a[1]')
but.click()
but2=driver.find_element(By.XPATH,'/html/body/div/div[1]/div[1]/main/div/div[2]/div[1]/div/label[2]/div[2]/span[2]')
time.sleep(2)
but2.click()


# In[48]:


Dataset=[] 
Data=[] 
Task=[] 
Attribute=[] 
Noi=[] 
Noa=[] 
Year=[] 
try:
    a=driver.find_elements(By.XPATH,'//a[@class="link-hover link text-xl font-semibold"]')
    for i in a:
        Dataset.append(i.text)
except NoSuchElementException:
    Dataset.append(i.text)

try:
    a=driver.find_elements(By.XPATH,'//div[@class="col-span-3 flex items-center gap-2"][2]/span')
    for i in a:
        Data.append(i.text)
except NoSuchElementException:
    Data.append(i.text)
try:
    a=driver.find_elements(By.XPATH,'//div[@class="col-span-3 flex items-center gap-2"][1]/span')
    for i in a:
        Task.append(i.text)
except NoSuchElementException:
    Task.append(i.text)
    
try:
    a=driver.find_elements(By.XPATH,'//tbody[@class="border"]/tr/td[2]')
    for i in a:
        Attribute.append(i.text)
except NoSuchElementException:
    Attribute.append(i.text)
try:
    a=driver.find_elements(By.XPATH,'//div[@class="col-span-3 flex items-center gap-2"][3]/span')
    for i in a:
        Noi.append(i.text)
except NoSuchElementException:
    Noi.append(i.text)
try:
    a=driver.find_elements(By.XPATH,'//div[@class="col-span-3 flex items-center gap-2"][4]/span')
    for i in a:
        Noa.append(i.text)
except NoSuchElementException:
    Noa.append(i.text)
try:
    a=driver.find_elements(By.XPATH,'//tbody[@class="border"]/tr/td[3]')
    for i in a:
        Year.append(i.text)
except NoSuchElementException:
    Year.append(i.text)    


# In[49]:


ml=pd.DataFrame({ "Dataset name":Dataset,
"Data type":Data, 
"Task":Task, 
"Attribute type":Attribute, 
"No of instances":Noi, 
"No of attribute":Noa,
"Year":Year })


# In[50]:


ml


# In[52]:


driver=webdriver.Chrome()
driver.get("https://github.com/")
but=driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/header/div/div[2]/div/nav/ul/li[3]/button')
but.click()
but2=driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/header/div/div[2]/div/nav/ul/li[3]/div/div[3]/ul/li[2]/a')
time.sleep(2)
but2.click()


# In[82]:


Repository=[]
Repositoryd=[] 
Language=[]
b=[]
a=driver.find_elements(By.XPATH,'//span[@class="text-normal"]')
for i in a:
    Repository.append(i.text)
b=[item.rstrip(' /') for item in Repository ]
a=driver.find_elements(By.XPATH,'//p[@class="col-9 color-fg-muted my-1 pr-4"]')
for i in a:
    Repositoryd.append(i.text)

a=driver.find_elements(By.XPATH,'//span[@itemprop="programmingLanguage"]')
for i in a:
    Language.append(i.text)        


# In[84]:


github=pd.DataFrame({"Repository":b,
"Repository Discriptions":Repositoryd,
"Language":Language})


# In[85]:


github

