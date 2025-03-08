# Mohit Bot

This repository contains a Facebook bot that performs the following actions:
- **Manual Login:** Opens Firefox for manual login.
- **Auto-Reply:** Sends random flirty replies (extend FLIRTY_MESSAGES to 1000+ messages as needed).
- **Meme Sending:** Sends a sample meme link in Messenger.
- **Name Detection:** Detects names from messages for personalized replies.
- **Voice Reply:** Generates a Hinglish voice reply using pyttsx3.
- **Error Logging:** Errors are logged to `error_log.txt`.

## Repository Structure

- **data/A_Cookies.json:** (Optional) Cookies file for cookies-based login.
- **B_FB_Login.py:** Facebook login module (supports manual, cookies, and email login).
- **C_AutoReply.py:** Auto-reply module.
- **D_MemeSender.py:** Meme sender module.
- **E_NameDetect.py:** Name detection module.
- **F_VoiceReply.py:** Voice reply module.
- **G_Main.py:** Main script to run the bot.
- **H_Requirements.txt:** Python dependencies.
- **I_README.md:** This file.

## Setup

1. **Clone the Repository:**
   ```sh
   git clone https://github.com/YourUsername/MyBot.git
