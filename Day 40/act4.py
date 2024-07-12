# Write a Python program that prints long text, converts it to a list,
#and prints all the words and the frequency of each word
# Define the long text
text = """Iam persuing Advanced Diploma in It Networking
and Cloud from NAtional Skill Training Institute Trivandrum."""

# Convert the text to a list of words
words = text.lower().split()
word_freq = {}
for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1
print("List of words:")
print(words)
print("\nFrequency of each word:")
for word, freq in word_freq.items():
    print(f"{word}: {freq}")
