"""Program 5c: Dice simulator using the random module."""

import os
import random

seed = os.getenv("LAB_DEMO_SEED")
rng = random.Random(int(seed)) if seed is not None else random.SystemRandom()

print("DICE SIMULATOR")
while True:
    choice = input("Press Enter to roll or Q to quit: ").strip().lower()
    if choice == "q":
        print("Thank you for playing")
        break
    print("Dice rolled:", rng.randint(1, 6))
