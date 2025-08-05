def is_palindrome(s):
    s = s.lower().replace(" ", "")  # Normalize the string by lowering case and removing spaces
    return s == s[::-1]  # Check if the string is equal to its reverse

# Example usage
word = "racecar"
print(f"Is '{word}' a palindrome? {is_palindrome(word)}")
