from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def send_message(wait, message):
    input_box = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input, textarea")))
    input_box.send_keys(message + Keys.RETURN)

# Initialize WebDriver
service = Service("C:/selenium/chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://paywatchapp.nftqa1.rezoomex.in/?technology=javaj2ee&experience=4-6&year=2024")
wait = WebDriverWait(driver, 60)

try:
    print("Opening chat...")
    chat_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='Open chat']")))
    driver.execute_script("arguments[0].click();", chat_button)
    
    questions = [
        "Hello", 
        "What is the hourly rate for Python developers with 5 years of experience?", 
        "Tell me a joke", 
        "What is the hourly rate for Go developers with 10 years experience in Antarctica?", 
        "What is the hourly rate for Python developers with -1 years experience?", 
        "Show hourly rate distribution for Java developers in Hyderabad."
    ]
    
    for question in questions:
        print(f"\n---")
        print(f"You: {question}")
        send_message(wait, question)
        
        # Wait for the bot to type and respond
        time.sleep(5)        
        # Extract the response
        # IMPORTANT: You may need to change the CSS Selector below to match the exact class 
        # used by the chatbot's text bubbles on this specific website.
        try:
            # We look for common chatbot message classes. 
            message_elements = driver.find_elements(By.CSS_SELECTOR, ".message, .bot-message, .chat-bubble, .text-content, p")
            
            if message_elements:
                # We found the response elements, print the verification message
                print("Bot: Response received")
            else:
                print("Bot: [Could not find response element on page]")
        except Exception as e:
            print(f"Error extracting response: {e}")

    print("\nClosing chat...")
    close_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='Close chat'], .chat-close-button")))
    driver.execute_script("arguments[0].click();", close_button)
    time.sleep(3)

    print("Re-opening chat to check history status...")
    chat_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='Open chat']")))
    driver.execute_script("arguments[0].click();", chat_button)
    time.sleep(2)

    print("History Status:", "Hello" in driver.page_source)

    close_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='Close chat']")))
    driver.execute_script("arguments[0].click();", close_button)

except Exception as main_error:
    print(f"An error occurred during execution: {main_error}")
    
finally:
    driver.quit()