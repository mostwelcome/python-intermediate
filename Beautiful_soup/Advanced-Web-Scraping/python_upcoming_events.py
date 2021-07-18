from selenium import webdriver

CHROME_DRIVER_PATH = "D:\chromedriver_win32\chromedriver"

driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

driver.get('https://www.python.org/')

event_times = driver.find_elements_by_css_selector(".event-widget time")
event_names = driver.find_elements_by_css_selector(".event-widget li a")

for time in event_times:
    print(time.text)

for names in event_names:
    print(names.text)

event_dict = {event_times[i].text: event_names[i].text for i in range(len(event_times))}

print(event_dict)

driver.quit()
