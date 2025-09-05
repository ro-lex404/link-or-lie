import random

def get_random_links():
    # For now hardcode a pool; later replace with DB or API
    real_links = ["https://www.google.com", "https://github.com", "https://openai.com"]
    fake_links = ["http://go0gle.com-login.secure", "http://paypa1.com-checkout", "http://amaz0n-login.net"]

    real = random.choice(real_links)
    fake = random.choice(fake_links)
    # Shuffle so left/right aren’t always the same
    options = [("real", real), ("fake", fake)]
    random.shuffle(options)
    return options
