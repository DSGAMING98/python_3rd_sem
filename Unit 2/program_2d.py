"""Program 2D: Generate and verify a six-digit OTP."""

import os
import random
import secrets

seed = os.getenv("LAB_DEMO_SEED")
if seed is None:
    otp = "".join(str(secrets.randbelow(10)) for _ in range(6))
else:
    rng = random.Random(int(seed))  # Reproducible demonstration only.
    otp = "".join(str(rng.randrange(10)) for _ in range(6))

print("OTP GENERATOR")
print("Generated OTP:", otp)
entry = input("Enter OTP to verify: ").strip()
print("OTP verified successfully!" if entry == otp else "Incorrect OTP.")
