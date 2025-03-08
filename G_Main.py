# G_Main.py
import time
import sys
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Set up error logging
logging.basicConfig(filename='error_log.txt', level=logging.ERROR,
                    format='%(asctime)s %(levelname)s: %(message)s')

from B_FB_Login import get_facebook_session
import C_AutoReply as auto_reply
import D_MemeSender as meme_sender
import E_NameDetect as name_detect
import F_VoiceReply as voice_reply

def check_internet():
    """Check if internet is working."""
    import requests
    try:
        requests.get("https://www.google.com", timeout=5)
        return True
    except requests.ConnectionError:
        return False

def mark_messages_seen(driver):
    """
    Attempts to mark unread messages as seen by clicking an unread conversation.
    Note: XPath may need updates according to Facebook Messenger UI changes.
    """
    try:
        unread_elements = driver.find_elements(By.XPATH, "//*[contains(@aria-label, 'unread')]")
        if unread_elements:
            print("[Messenger] Unread message found. Clicking to mark as seen...")
            unread_elements[0].click()
            time.sleep(5)
            print("[Messenger] Message marked as seen.")
        else:
            print("[Messenger] No unread messages found.")
    except Exception as e:
        logging.error("Error marking messages seen: " + str(e))
        print("⚠️ Error marking messages as seen.")

def send_auto_reply(driver):
    """
    Sends an auto-reply in the currently open conversation.
    Note: XPath for the message input field may need updating.
    """
    try:
        input_box = driver.find_element(By.XPATH, "//div[@aria-label='Message' and @role='textbox']")
        input_box.click()
        time.sleep(1)
        reply_text = auto_reply.get_random_reply()
        input_box.send_keys(reply_text)
        input_box.send_keys(Keys.RETURN)
        print(f"[AutoReply] Sent reply: {reply_text}")
        return reply_text
    except Exception as e:
        logging.error("Error sending auto reply: " + str(e))
        print("⚠️ Error sending auto reply.")
        return None

def main():
    print("🔥 Mohit Bot Starting...")
    
    if not check_internet():
        print("❌ Internet disconnected! Exiting...")
        sys.exit(1)
    
    # Get Facebook session via manual login
    driver = get_facebook_session()
    if not driver:
        print("❌ Exiting... Login Failed.")
        sys.exit(1)
    else:
        print("✅ Login successful! Bot is now active.")
    
    # Navigate to Messenger
    try:
        driver.get("https://www.facebook.com/messages")
        time.sleep(10)
    except Exception as e:
        logging.error("Error navigating to Messenger: " + str(e))
        print("⚠️ Error navigating to Messenger.")
        driver.quit()
        sys.exit(1)
    
    # Mark messages as seen
    mark_messages_seen(driver)
    
    # Send auto-reply
    reply_text = send_auto_reply(driver)
    
    # Send a meme
    meme_sender.send_meme(driver)
    
    # Send a voice reply using the auto-reply text (if available)
    if reply_text:
        voice_reply.send_voice_reply(f"Voice: {reply_text}")
    
    print("🤖 Bot actions completed. Exiting in 10 seconds...")
    time.sleep(10)
    driver.quit()

if __name__ == "__main__":
    main()
