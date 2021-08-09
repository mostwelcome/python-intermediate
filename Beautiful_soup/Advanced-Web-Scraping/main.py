from selenium import webdriver

CHROME_DRIVER_PATH = "D:\chromedriver_win32\chromedriver"

driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

driver.get(
    'https://www.amazon.in/Elina-Women-Shorts-RM-DB162_Black-Green_Small/dp/B08G8CBH3B/?_encoding=UTF8&pd_rd_w=FnhKn&pf_rd_p=69d15ffa-a452-4296-bc93-f6cb35154b06&pf_rd_r=1ZAH04QYB4DEP3P5R7JH&pd_rd_r=3938454f-7d72-47d5-b2c3-5886c7b4a2aa&pd_rd_wg=H0AnX&ref_=pd_gw_cr_cartx')

price = driver.find_element_by_id('priceblock_ourprice')

print(price.text)

# close a tab
# driver.close()

# closes entire browser
driver.quit()
