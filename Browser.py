import csv 
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 


"""place your path here in the executable path"""
driver = webdriver.Chrome(executable_path = r"C:\Users\Lenovo\Documents\astaqc\selenium\Drivers\chromedriver.exe")


BASE_URL = "https://google.com"
""" Base_URL is been passed to driver"""
driver.get(BASE_URL) 

search = "spanish flu filetype:pdf"
search_box = driver.find_element_by_xpath("//*[@id='tsf']/div[2]/div[1]/div[1]/div/div[2]/input").send_keys(search,Keys.RETURN)

""" All the href will be stored in results """

def GetLinks():
    for a in driver.find_elements_by_xpath("//a"):
        """ Finding the element by using xpath """ 
        href = a.get_attribute("href") ### Getting all the href and storing the list 
        print(href)
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        driver.find_element_by_xpath('/html/body/div[5]/div[2]/div[9]/div[1]/div[2]/div/div[5]/div[2]/span[1]/div')

GetLinks()


driver.close()