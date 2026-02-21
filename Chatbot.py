from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def f(w, m):
    i = w.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input, textarea")))
    i.send_keys(m + Keys.RETURN)

s = Service("C:/selenium/chromedriver.exe")
d = webdriver.Chrome(service=s)
d.maximize_window()
d.get("https://paywatchapp.nftqa1.rezoomex.in/?technology=javaj2ee&experience=4-6&year=2024")
w = WebDriverWait(d, 60)

try:
    c = w.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='Open chat']")))
    d.execute_script("arguments[0].click();", c)
    
    qs = ["Hello", "What is the hourly rate for Python developers with 5 years of experience?", "Tell me a joke", "What is the hourly rate for Go developers with 10 years experience in Antarctica?", "What is the hourly rate for Python developers with -1 years experience?", "Show hourly rate distribution for Java developers in Hyderabad."]
    
    for q in qs:
        f(w, q)
        time.sleep(4)

    x = w.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='Close chat'], .chat-close-button")))
    d.execute_script("arguments[0].click();", x)
    time.sleep(3)

    c = w.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='Open chat']")))
    d.execute_script("arguments[0].click();", c)
    time.sleep(2)

    print("Status:", "Hello" in d.page_source)

    x = w.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='Close chat']")))
    d.execute_script("arguments[0].click();", x)

except:
    pass
finally:
    d.quit()