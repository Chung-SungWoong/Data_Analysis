"""
selenium의 webdriver 활용
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service       # selenium 오류 해결위해 다운
from webdriver_manager.chrome import ChromeDriverManager
"""
def set_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver
"""

driver = webdriver.Chrome('/Users/chung_sungwoong/Downloads/chromedriver')

url = 'https://www.naver.com/'

html = driver.page_source
driver.get(html)