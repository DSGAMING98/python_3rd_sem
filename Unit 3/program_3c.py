"""Program 3c: Word-frequency counter using a dictionary."""

import re

text = input("Enter a sentence: ").lower()
words = re.findall(r"[a-z0-9']+", text)
frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print("WORD FREQUENCY")
for word in sorted(frequency):
    print(f"{word}: {frequency[word]}")
print("Total words:", len(words))
