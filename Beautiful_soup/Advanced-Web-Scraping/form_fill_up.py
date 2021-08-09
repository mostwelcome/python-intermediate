from selenium import webdriver

CHROME_DRIVER_PATH = "D:\chromedriver_win32\chromedriver"

driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

driver.get('http://secure-retreat-92358.herokuapp.com/')
first_name = driver.find_element_by_name('fName')
first_name.send_keys('swag')

last_name = driver.find_element_by_name('lName')
last_name.send_keys('dutta')

email = driver.find_element_by_name('email')
email.send_keys('sdutta@gmail.com')

submit_button = driver.find_element_by_css_selector('form button')
submit_button.click()
