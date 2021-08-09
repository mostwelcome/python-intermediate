from selenium import webdriver
from selenium.webdriver.common.keys import Keys

CHROME_DRIVER_PATH = "D:\chromedriver_win32\chromedriver"

driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

driver.get('https://en.wikipedia.org/wiki/Main_Page')
article_count = driver.find_element_by_css_selector('#articlecount a')

# article_count.click()

all_ports = driver.find_element_by_link_text('All portals')

# all_ports.click()

search = driver.find_element_by_name('search')

search.send_keys('python')
search.send_keys(Keys.ENTER)
