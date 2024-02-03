import random

def generate_compliment():
    compliments = [
        "You're amazing!",
        "You have a fantastic smile!",
        "You're a great friend!",
        "Your kindness is inspiring!",
        "You always bring positivity!",
        "You're incredibly talented!",
        "You're a true gem!",
    ]
    return random.choice(compliments)

if __name__ == "__main__":
    print("Hey there! Here's a compliment for you and your friend:")
    compliment = generate_compliment()
    print(compliment)
