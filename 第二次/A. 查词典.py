import sys

lines = sys.stdin.read().splitlines()
n = int(lines[0])

translation = {dog: cat for cat, dog in (line.split() for line in lines[1 : n + 1])}
document_words = lines[n + 1 : -1]
translated = [translation.get(word, "dog") for word in document_words]
print("\n".join(translated))
