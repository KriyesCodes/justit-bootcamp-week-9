word = str(input("Enter your word: "))

vowels = ["a","e","i","o","u"]
consonants = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z"]

for letter in word:
  if letter.lower() in vowels:
    desc = "is a vowel"
  elif letter.lower() in consonants:
    desc = "is a consonant"
  else:
    desc = "is not a valid letter"
  
  print(f"{letter} {desc}")