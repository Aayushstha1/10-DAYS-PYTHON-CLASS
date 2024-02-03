import random

def generate_friend_compliment(friend_name):
    compliments = [
        f"{friend_name}, you're an incredible friend!",
        f"Your positivity always brightens my day, {friend_name}!",
        f"I appreciate your loyalty, {friend_name}!",
        f"{friend_name}, you have a heart of gold!",
        f"Your kindness is truly remarkable, {friend_name}!",
        f"{friend_name}, you make friendship feel effortless!",
        f"I'm grateful to have a friend like you, {friend_name}!",
    ]
    return random.choice(compliments)

if __name__ == "__main__":
    friend_name = input("Enter your friend's name: ")
    compliment = generate_friend_compliment(friend_name)
    print(f"Hey {friend_name}! Here's a compliment for you:")
    print(compliment)
