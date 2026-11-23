#BPE tokenization using Pre-trained GPT2 tokenizer

from transformers import AutoTokenizer
from collections import Counter

tokenizer = AutoTokenizer.from_pretrained("gpt2")

text = input("Enter a Sentence:") or "I love learning python"

tokens = tokenizer.tokenize(text)
token_ids = tokenizer.convert_tokens_to_ids(tokens)

print("Original Sentence:", text)
print("BPE Tokens:",tokens)
print("Token IDs:",token_ids)
print("Length of Tokens:",len(tokens))