from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


def scrap_init(url):
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
    chrome_options.add_argument(f'user-agent={user_agent}')
    browser = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=chrome_options)
    browser.get(url)
    return browser
    
def get_url(browser,url):
    browser.get(url)

def get_element_xpath(browser,xpath):
    try:
        element = browser.find_element(By.XPATH, xpath)
        return element

    except:
        print("Unable to fetch")
        pass
    
    

def click(element):
    element.click()

def send_keys(element, text):
    element.send_keys(text)

def buffer(seconds):
    time.sleep(seconds)

def strip(element):
    try:
        num = element.text
        return num

    except:
        num = 'null'
        return num