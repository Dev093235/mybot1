# C_AutoReply.py
import random

# Sample list of flirty messages (extend this list as needed)
FLIRTY_MESSAGES = [
    "Tumhari muskaan meri zindagi hai!",
    "Aaj tum bahut pyaari lag rahi ho!",
    "Dil karta hai, tumse bas baat karun!",
    "Mujhe tumhari baatein yaad aati hain!",
    "Tumhari aankhon mein kuch khaas baat hai!"
    # ... add more messages here to reach 1000+ if desired
]

def get_random_reply():
    return random.choice(FLIRTY_MESSAGES)

def check_messages(session, messages):
    """
    Auto-reply function.
    For each received message, prints a random flirty reply.
    (Replace dummy logic with actual messaging integration as needed.)
    """
    for msg in messages:
        text, sender = msg
        reply = get_random_reply()
        print(f"[AutoReply] Replying to {sender}: {reply}")
    return

if __name__ == "__main__":
    dummy_messages = [("Hello bot!", "Rahul"), ("Kya haal hai?", "Pooja")]
    check_messages(None, dummy_messages)
