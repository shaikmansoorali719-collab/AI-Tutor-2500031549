# word level tokenization
text = input("Enter a sentence: ") or "I love learning python"
print("Text",text)
tokens = text.split()
print("Length of tokens:",len(tokens))
print("Tokens:",tokens)
