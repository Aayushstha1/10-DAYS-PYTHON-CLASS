import random

def generate_art(width, height):
    art = ''
    for _ in range(height):
        row = ''
        for _ in range(width):
            # Generate a random ASCII character
<<<<<<< HEAD
            char = chr(random.randint(32, 126))  
=======
            char = chr(random.randint(32, 126))  # ASCII range of printable character
>>>>>>> e7db50f50fb8fbf57971e03923d5c5bbb670d431
            row += char
        art += row + '\n'
    return art

if __name__ == "__main__":
    width = 50
    height = 20
    ascii_art = generate_art(width, height)
    print(ascii_art)
