# F_VoiceReply.py
import pyttsx3

def send_voice_reply(text):
    """
    Generates a voice reply using pyttsx3.
    """
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)
    engine.setProperty("volume", 1.0)
    engine.say(text)
    engine.runAndWait()
    print(f"[VoiceReply] Voice reply generated for: {text}")

if __name__ == "__main__":
    send_voice_reply("Tumhari baat sun kar dil khush ho gaya!")
