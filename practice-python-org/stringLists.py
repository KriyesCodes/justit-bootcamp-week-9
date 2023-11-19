def isPalindrome(s):
  return s == s[::-1]

candidate = str(input("Enter candidate string: "))

if isPalindrome(candidate):
  print(f"'{candidate}' is a palindrome")
else:
  print(f"'{candidate}' is not a palindrome")