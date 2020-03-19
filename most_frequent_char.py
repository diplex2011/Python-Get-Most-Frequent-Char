"""The most frequent item in the sentence."""

from pprint import pprint

sentence = "There is nothing you can do that can`t be done!"

# 1. Use max function.
def most_frequent(sentence):
    # remove space from result first:
    sentence = "".join(sentence.split())
    return max((sentence), key=sentence.count)

print(most_frequent(sentence))
print()

# 2. Use dict (get items and its frequency in the sentence)
char_frequency = {}
for char in sentence:
    if char != " ":
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1

print(char_frequency)
print()

# Sort items:
char_frequency_sorted = sorted(
    char_frequency.items(), key=lambda kv: kv[1], reverse=True)
pprint(char_frequency_sorted)
print()

# Here we get our final result.
print(char_frequency_sorted[0])
