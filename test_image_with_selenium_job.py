from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome(options=chrome_options)

driver.get('www.google.com')
source = driver.page_source
if "I'm Feelling Lucky" in source:
  print("Test passed")
else:
  print("Test failed")
driver.close()



