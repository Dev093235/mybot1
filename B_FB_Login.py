# B_FB_Login.py
import time
import json
import os
import requests
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

def get_session_manual():
    """
    Launches Firefox for manual login.
    A visible browser window will open; log in manually within 40 seconds.
    """
    options = Options()
    options.headless = False  # Must be False for manual login
    options.add_argument("--disable-gpu")
    
    # Use a unique user data directory to avoid conflicts.
    profile_path = f"/tmp/firefox_profile_manual_{int(time.time())}"
    options.add_argument(f"--user-data-dir={profile_path}")
    
    try:
        print("🚀 Launching Firefox for manual login...")
        driver = webdriver.Firefox(options=options)
        driver.get("https://www.facebook.com")
        print("⏳ Please manually log in to Facebook within 40 seconds...")
        time.sleep(40)
        if "home" in driver.current_url or "profile.php" in driver.current_url:
            print("✅ Manual login successful!")
            return driver
        else:
            print("❌ Manual login failed!")
            driver.quit()
            return None
    except Exception as e:
        print(f"⚠️ Error during manual login: {e}")
        return None

def get_session_cookies():
    """
    Loads cookies from data/A_Cookies.json (expected as a dictionary)
    and creates a requests.Session with those cookies.
    Expected JSON format:
    {
      "c_user": "your_user_id",
      "xs": "your_xs_cookie_value"
    }
    """
    try:
        with open("data/A_Cookies.json", "r", encoding="utf-8") as f:
            cookies = json.load(f)
        if not isinstance(cookies, dict):
            raise ValueError("Invalid cookies format! Expected a dictionary.")
        session = requests.Session()
        session.cookies.set("c_user", cookies.get("c_user", ""), domain=".facebook.com")
        session.cookies.set("xs", cookies.get("xs", ""), domain=".facebook.com")
        print("✅ Cookies-based session created!")
        return session
    except Exception as e:
        print(f"❌ Error loading cookies: {e}")
        return None

def get_session_email():
    """
    Uses email and password to login to Facebook using Selenium.
    Set environment variables FB_EMAIL and FB_PASSWORD.
    """
    EMAIL = os.getenv("FB_EMAIL")
    PASSWORD = os.getenv("FB_PASSWORD")
    if not EMAIL or not PASSWORD:
        print("❌ FB_EMAIL or FB_PASSWORD environment variables not set!")
        return None

    options = Options()
    options.headless = False  # Visible browser for login and CAPTCHA handling
    options.add_argument("--disable-gpu")
    
    profile_path = f"/tmp/firefox_profile_email_{int(time.time())}"
    options.add_argument(f"--user-data-dir={profile_path}")
    
    try:
        print("🚀 Launching Firefox for email/password login...")
        driver = webdriver.Firefox(options=options)
        driver.get("https://www.facebook.com/login")
        time.sleep(5)
        email_elem = driver.find_element("id", "email")
        pass_elem = driver.find_element("id", "pass")
        email_elem.send_keys(EMAIL)
        pass_elem.send_keys(PASSWORD)
        pass_elem.submit()
        print("⏳ Waiting for login to complete (60 sec)...")
        time.sleep(60)
        if "home" in driver.current_url or "profile.php" in driver.current_url:
            print("✅ Email/Password login successful!")
            return driver
        else:
            print("❌ Email/Password login failed!")
            driver.quit()
            return None
    except Exception as e:
        print(f"⚠️ Error during email/password login: {e}")
        return None

def get_facebook_session():
    """
    Returns a Facebook session based on the LOGIN_METHOD environment variable.
    Options:
      - "manual"   : Manual login via Firefox (default)
      - "cookies"  : Cookies-based login using data/A_Cookies.json
      - "email"    : Email/Password login using environment variables FB_EMAIL and FB_PASSWORD
    """
    method = os.getenv("LOGIN_METHOD", "manual").lower()
    if method == "manual":
        return get_session_manual()
    elif method == "cookies":
        return get_session_cookies()
    elif method == "email":
        return get_session_email()
    else:
        print("❌ Invalid LOGIN_METHOD specified!")
        return None

if __name__ == "__main__":
    session = get_facebook_session()
