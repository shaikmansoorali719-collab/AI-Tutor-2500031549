word = input("Enter a word: ") or "python"

print("Word:", word)
print("Length of the word:",len(word))

Characters = list(word)

print("Characters in the word:", Characters)

pairs =list(zip(Characters, Characters[1:]))
print("Adjacent pairs:", pairs)