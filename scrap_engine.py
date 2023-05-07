from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import os 
from selenium.webdriver.common.action_chains import ActionChains


def scrap_init(url):
    chrome_options = Options()
    prefs = {'download.default_directory' : os.getcwd()}
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_experimental_option("detach", True)
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
    chrome_options.add_argument(f'user-agent={user_agent}')
    browser = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=chrome_options)
    browser.get(url)
    browser.maximize_window()
    return browser
    
def get_url(browser,url):
    browser.get(url)

def get_element_xpath(browser,xpath):
    try:
        element = browser.find_element(By.XPATH, xpath)
        return element

    except:
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

# browser = scrap_init("https://www.infomoney.com.br/cotacoes/b3/indice/ifix/historico/")   
# get_url(browser, "https://www.infomoney.com.br/cotacoes/b3/indice/ifix/historico/")
# buffer(50)
# # cookies = get_element_xpath(browser,"/html//cookies-policy[@class='hydrated']")
# # click(cookies)
# ifix_hist_table = get_element_xpath(browser,"//div[@id='quotes_history_wrapper']//button[@type='button']/span[.='Baixar arquivo']")
# buffer(3)
# actions = ActionChains(browser)
# actions.move_to_element(ifix_hist_table).perform()

# click(ifix_hist_table)

