word = str(input("Enter your word: "))

vowels = ["a","e","i","o","u"]

for letter in word:
  if letter in vowels:
    desc = "is a vowel"
  else:
    desc = "is a consonant"
  
  print(f"{letter} {desc}")