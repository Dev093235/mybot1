# D_MemeSender.py
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def send_meme(driver):
    """
    Dummy meme sender.
    Sends a sample meme link in the current Messenger conversation.
    Note: The XPath used here may need updates based on Facebook's UI.
    """
    meme_link = "https://i.imgur.com/your_sample_meme.jpg"
    try:
        # Locate the message input field (update the XPath as per actual Messenger UI)
        input_box = driver.find_element(By.XPATH, "//div[@aria-label='Message' and @role='textbox']")
        input_box.click()
        time.sleep(1)
        input_box.send_keys(meme_link)
        input_box.send_keys(Keys.RETURN)
        print(f"[MemeSender] Meme sent: {meme_link}")
    except Exception as e:
        print(f"[MemeSender] Error sending meme: {e}")
    return

if __name__ == "__main__":
    print("Run this function via the main bot script.")
