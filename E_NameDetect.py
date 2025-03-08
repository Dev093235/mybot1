# E_NameDetect.py
def detect_name(message):
    """
    Dummy name detection.
    Checks for known names in the message and returns a personalized greeting.
    """
    known_names = ["Rahul", "Priya", "Mohit"]
    for name in known_names:
        if name.lower() in message.lower():
            return f"Hey {name}, kaise ho?"
    return "Hi there!"

if __name__ == "__main__":
    user_msg = input("Enter a message: ")
    print(detect_name(user_msg))
