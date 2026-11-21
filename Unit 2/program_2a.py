"""Program 2a: Number guessing game."""

import os
import random

seed = os.getenv("LAB_DEMO_SEED")
rng = random.Random(int(seed)) if seed is not None else random.SystemRandom()
secret = rng.randint(1, 10)

print("NUMBER GUESSING GAME (1 to 10)")
for attempt in range(1, 6):
    try:
        guess = int(input(f"Guess {attempt}/5: "))
    except ValueError:
        print("Enter an integer.")
        continue

    if guess == secret:
        print(f"Correct! You guessed the number in {attempt} attempts.")
        break

    print("Too low!" if guess < secret else "Too high!")
else:
    print(f"Game over. The number was {secret}.")
