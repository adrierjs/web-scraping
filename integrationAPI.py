import undetected_chromedriver as uc
import time

options = uc.ChromeOptions()
options.headless = True
driver = uc.Chrome(use_subprocess=True, options=options)
driver.get("https://steamdb.info/sales/")
driver.maximize_window()
time.sleep(20)
driver.save_screenshot("validation.png")
data_site = driver.page_source
driver.close()
