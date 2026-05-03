# TASK #2
# Count Vowels and Consonants in a Sentence

sentence = input("Enter a sentence: ").lower()

vow = 0
cons = 0

for letter in sentence:
    if letter.isalpha():   # check for the letter
        if letter in "aeiou":
            vow += 1
        else:
            cons += 1

print("The number of Vowels in the Sentence =", vow)
print("The number of Consonants in the Sentence =", cons)