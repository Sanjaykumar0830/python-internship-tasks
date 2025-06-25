text = "Hello, how are you?"
vowels = 'aeiouAEIOU'
c = sum(1 for ch in text if ch in vowels)
print("Input String:", text)
print("Number of vowels:", c)
